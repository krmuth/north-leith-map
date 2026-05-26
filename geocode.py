#!/usr/bin/env python3
"""
Geocode feature addresses via Nominatim and update src/features.py.

Usage:
    python geocode.py                     # geocode all features
    python geocode.py leith-fort citadel  # geocode specific feature IDs
    python geocode.py --dry-run           # show results without writing
"""

import re
import ssl
import sys
import time
import argparse
from math import radians, cos, sin, asin, sqrt
from pathlib import Path

import certifi
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

sys.path.insert(0, str(Path(__file__).parent))
from src.features import FEATURES

try:
    from geopy.geocoders import Nominatim
    from geopy.exc import GeocoderTimedOut, GeocoderServiceError
except ImportError:
    sys.exit("geopy not installed — run: uv pip install geopy==2.4.1")

LEITH_LAT, LEITH_LON = 55.9752, -3.1793
MAX_KM = 8  # reject results more than this far from Leith centre


def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return 2 * R * asin(sqrt(a))


def try_geocode(gc, query):
    try:
        result = gc.geocode(query, country_codes="gb", exactly_one=True, timeout=10)
        time.sleep(1.1)  # Nominatim policy: max 1 req/sec
        if result:
            dist = haversine_km(result.latitude, result.longitude, LEITH_LAT, LEITH_LON)
            if dist <= MAX_KM:
                return result, dist
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"    geocoder error: {e}")
        time.sleep(3)
    return None, None


def geocode_feature(gc, f):
    address = f["address"]

    # Try 1: full address as-is
    result, dist = try_geocode(gc, address)
    if result:
        return result, dist, address

    # Try 2: first component + Edinburgh Scotland (handles vague addresses)
    parts = [p.strip() for p in address.split(",")]
    if len(parts) >= 2:
        simplified = f"{parts[0]}, Edinburgh, Scotland"
        result, dist = try_geocode(gc, simplified)
        if result:
            return result, dist, simplified

    return None, None, address


def update_features_py(updates):
    path = Path("src/features.py")
    src = path.read_text(encoding="utf-8")

    for fid, new_lat, new_lon in updates:
        id_marker = f'"id": "{fid}"'
        id_pos = src.find(id_marker)
        if id_pos == -1:
            print(f"  [warn] '{fid}' not found in src/features.py")
            continue

        # Scope replacement to this feature's dict block only
        block_end = src.find("\n    },", id_pos)
        if block_end == -1:
            block_end = len(src)

        block = src[id_pos:block_end]
        block = re.sub(r'"lat":\s*[-\d.]+', f'"lat": {new_lat}', block)
        block = re.sub(r'"lon":\s*[-\d.]+', f'"lon": {new_lon}', block)
        src = src[:id_pos] + block + src[block_end:]

    path.write_text(src, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Geocode feature addresses via Nominatim")
    parser.add_argument("ids", nargs="*", help="Feature IDs to geocode (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Show results without writing")
    args = parser.parse_args()

    target_ids = set(args.ids) if args.ids else None
    features = [f for f in FEATURES if target_ids is None or f["id"] in target_ids]

    if not features:
        sys.exit("No matching features found.")

    gc = Nominatim(user_agent="north-leith-history-map/1.0 contact=muthgpt@gmail.com")

    updates = []
    failures = []

    print(f"Geocoding {len(features)} feature(s) via Nominatim...\n")

    for f in features:
        print(f"  {f['id']}")
        print(f"    address : {f['address']}")
        if f["lat"] is not None:
            print(f"    current : {f['lat']}, {f['lon']}")
        else:
            print(f"    current : (no coordinates)")

        result, dist, query_used = geocode_feature(gc, f)

        if result:
            new_lat = round(result.latitude, 6)
            new_lon = round(result.longitude, 6)
            print(f"    result  : {new_lat}, {new_lon}  ({dist:.2f} km from Leith centre)")
            print(f"    match   : {result.address[:90]}")
            if query_used != f["address"]:
                print(f"    query   : {query_used}")
            updates.append((f["id"], new_lat, new_lon))
        else:
            print(f"    [FAILED] no result within {MAX_KM} km")
            failures.append(f["id"])

        print()

    print(f"Results: {len(updates)} geocoded, {len(failures)} failed.")

    if args.dry_run:
        print("Dry run — nothing written.")
        return

    if not updates:
        print("Nothing to write.")
        return

    update_features_py(updates)
    print(f"Updated {len(updates)} feature(s) in src/features.py.")

    if failures:
        print(f"\nFailed to geocode: {', '.join(failures)}")
        print("Check addresses or place manually via the drag editor.")

    print("\nRun 'python build.py' to regenerate outputs.")


if __name__ == "__main__":
    main()
