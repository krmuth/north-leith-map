#!/usr/bin/env python3
"""Build all map outputs from the North Leith feature dataset."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from src.features import FEATURES

OUT_KML      = Path("docs/kml")
OUT_GEOJSON  = Path("docs/geojson")
OUT_SHP      = Path("docs/shapefiles")
OUT_MAP      = Path("docs")

CATEGORY_COLOURS = {
    "religious":   "#7b1fa2",
    "educational": "#1565c0",
    "welfare":     "#546e7a",
    "maritime":    "#00695c",
    "civic":       "#c62828",
    "commercial":  "#e65100",
    "residential": "#4e342e",
    "memorial":    "#827717",
    "military":    "#37474f",
}
GLADSTONE_COLOUR = "#ffb300"
ACCENT_COLOUR    = "#ffb300"  # gold


def hex_to_kml(hex_colour, alpha="ff"):
    """Convert #RRGGBB to KML AABBGGRR."""
    h = hex_colour.lstrip("#")
    r, g, b = h[0:2], h[2:4], h[4:6]
    return f"{alpha}{b}{g}{r}"


# ---------------------------------------------------------------------------
# KML
# ---------------------------------------------------------------------------

def build_kml(features):
    import simplekml

    kml = simplekml.Kml(name="North Leith Neighbourhood History")
    gladstone_folder    = kml.newfolder(name="Gladstone Imprint")
    neighbourhood_folder = kml.newfolder(name="Wider Neighbourhood")

    skipped = 0
    for f in features:
        if f["lat"] is None:
            print(f"    [KML] skipping {f['id']} — no coordinates")
            skipped += 1
            continue

        folder = gladstone_folder if f["gladstone"] else neighbourhood_folder

        raw_colour = GLADSTONE_COLOUR if f["gladstone"] else CATEGORY_COLOURS.get(f["category"], "#888888")
        alpha = "88" if f["status"] == "demolished" else "ff"
        kml_colour = hex_to_kml(raw_colour, alpha=alpha)

        pnt = folder.newpoint(name=f["name"], coords=[(f["lon"], f["lat"])])
        pnt.style.iconstyle.color  = kml_colour
        pnt.style.iconstyle.scale  = 1.3 if f["gladstone"] else 1.0
        pnt.style.labelstyle.color = kml_colour

        if f["date_from"]:
            pnt.timespan.begin = str(f["date_from"])
        if f["date_to"]:
            pnt.timespan.end = str(f["date_to"])

        date_str = str(f["date_from"])
        if f["date_to"]:
            date_str += f"–{f['date_to']}"

        tags = []
        if f["gladstone"]:
            tags.append(f'<span style="color:{GLADSTONE_COLOUR}">&#11035; Gladstone</span>')
        if f["colonial_link"]:
            tags.append("Colonial link")
        if f["listed"] != "unlisted":
            tags.append(f"Listed {f['listed']}")

        sources_html = "".join(f"<li>{s}</li>" for s in f["sources"])
        tags_html = " &nbsp;&middot;&nbsp; ".join(tags) if tags else ""

        pnt.description = (
            f"<![CDATA["
            f"<b>{f['name']}</b><br/>"
            f"<i>{f['address']}</i><br/>"
            f"{date_str} &nbsp;|&nbsp; {f['category'].title()} &nbsp;|&nbsp; {f['status'].title()}<br/>"
            f"{tags_html}"
            f"<hr/>{f['description']}"
            f"<hr/><small><b>Sources</b><ul>{sources_html}</ul></small>"
            f"]]>"
        )

    out = OUT_KML / "north-leith.kml"
    kml.save(str(out))
    count = len([f for f in features if f["lat"] is not None])
    print(f"  KML        → {out}  ({count} features)")


# ---------------------------------------------------------------------------
# GeoJSON
# ---------------------------------------------------------------------------

def build_geojson(features):
    fc = {"type": "FeatureCollection", "features": []}

    for f in features:
        if f["lat"] is None:
            continue
        props = {k: v for k, v in f.items() if k not in ("lat", "lon")}
        props["sources"] = "; ".join(f["sources"])
        fc["features"].append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [round(f["lon"], 6), round(f["lat"], 6)]},
            "properties": props,
        })

    out = OUT_GEOJSON / "north-leith.geojson"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(fc, fh, ensure_ascii=False, indent=2)
    print(f"  GeoJSON    → {out}  ({len(fc['features'])} features)")
    return fc


# ---------------------------------------------------------------------------
# Shapefile
# ---------------------------------------------------------------------------

def build_shapefile(features):
    import geopandas as gpd
    from shapely.geometry import Point

    rows = []
    for f in features:
        if f["lat"] is None:
            continue
        rows.append({
            "id":        f["id"],
            "name":      f["name"],
            "category":  f["category"],
            "date_from": f["date_from"],
            "date_to":   f["date_to"],
            "address":   f["address"],
            "listed":    f["listed"],
            "gladstone": f["gladstone"],
            "col_link":  f["colonial_link"],   # colonial_link > 10 chars
            "descript":  f["description"][:254],
            "sources":   "; ".join(f["sources"])[:254],
            "status":    f["status"],
            "geometry":  Point(f["lon"], f["lat"]),
        })

    gdf = gpd.GeoDataFrame(rows, crs="EPSG:4326")
    out = OUT_SHP / "north-leith.shp"
    gdf.to_file(str(out))
    print(f"  Shapefile  → {out}  ({len(rows)} features)")


# ---------------------------------------------------------------------------
# Leaflet HTML map
# ---------------------------------------------------------------------------

def build_map(features):
    feature_list = []

    for f in features:
        if f["lat"] is None:
            continue
        colour   = CATEGORY_COLOURS.get(f["category"], "#888888")
        date_str = str(f["date_from"])
        if f["date_to"]:
            date_str += f"–{f['date_to']}"
        feature_list.append({
            "id":            f["id"],
            "name":          f["name"],
            "dates":         date_str,
            "address":       f["address"],
            "status":        f["status"],
            "listed":        f["listed"],
            "gladstone":     f["gladstone"],
            "colonial_link": f["colonial_link"],
            "description":   f["description"],
            "colour":        colour,
            "lat":           round(f["lat"], 6),
            "lon":           round(f["lon"], 6),
        })

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>North Leith Neighbourhood History</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@400;500;600&family=Work+Sans:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Zilla Slab', Georgia, serif; background: #f5f0e8; }}
    #map {{ height: 100vh; width: 100%; }}

    .leaflet-control-layers {{
      border-radius: 5px !important;
      font-family: 'Work Sans', sans-serif;
      font-size: 0.78rem;
    }}
    .leaflet-control-layers-toggle {{
      background-size: 20px 20px;
      border-radius: 5px !important;
    }}

    #title {{
      position: absolute; top: 12px; left: 50%; transform: translateX(-50%);
      z-index: 1000; background: #fff; padding: 8px 22px; border-radius: 6px;
      font-family: 'Zilla Slab', Georgia, serif;
      font-size: 1.1rem; font-weight: 500; letter-spacing: 0.01em;
      white-space: nowrap; color: #222; cursor: pointer;
      box-shadow: 0 1px 5px rgba(0,0,0,0.12);
    }}

    #edit-toggle {{
      position: absolute; top: 12px; right: 12px; z-index: 1001;
      background: #fff; border: none; cursor: pointer; border-radius: 5px;
      padding: 7px 14px; font-family: 'Zilla Slab', Georgia, serif;
      font-size: 0.85rem; font-weight: 500; letter-spacing: 0.02em; color: #333;
      box-shadow: 0 1px 5px rgba(0,0,0,0.12);
    }}
    #edit-toggle:hover {{ background: #f5f5f5; }}
    #edit-toggle.active {{ background: {ACCENT_COLOUR}; color: #fff; }}

    #corrections {{
      position: absolute; top: 44px; right: 12px; z-index: 1000;
      background: #fff; padding: 12px 14px; width: 280px; border-radius: 6px;
      box-shadow: 0 1px 5px rgba(0,0,0,0.12);
      font-family: 'Work Sans', sans-serif; font-size: 0.78rem; color: #333;
      display: none; max-height: calc(100vh - 80px); overflow-y: auto;
    }}
    #corrections h3 {{ font-size: 0.75rem; margin-bottom: 6px; color: #999; letter-spacing: 0.05em; }}
    #coord-display {{
      font-family: monospace; font-size: 0.75rem; color: #555;
      margin-bottom: 10px; min-height: 1.4em;
    }}
    .ed-section {{ margin-top: 12px; padding-top: 10px; border-top: 1px solid #eee; }}
    .ed-label {{ font-size: 0.7rem; color: #aaa; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 8px; }}
    .ed-note {{ font-size: 0.72rem; color: #777; margin-bottom: 8px; line-height: 1.5; }}
    .btn-row {{ display: flex; gap: 6px; margin-bottom: 6px; }}
    .ed-btn {{
      flex: 1; padding: 5px 8px; background: #f5f5f5; color: #333;
      border: 1px solid #ddd; cursor: pointer; font-family: 'Work Sans', sans-serif;
      font-size: 0.75rem; letter-spacing: 0.02em; border-radius: 4px;
    }}
    .ed-btn:hover {{ background: #eaeaea; }}
    .ed-btn.amber {{ background: {ACCENT_COLOUR}; color: #fff; border-color: {ACCENT_COLOUR}; }}
    .ed-btn.amber:hover {{ background: #e6a200; }}
    #new-name, #new-notes {{
      width: 100%; padding: 5px 7px; margin-bottom: 6px;
      font-family: 'Work Sans', sans-serif; font-size: 0.78rem;
      border: 1px solid #ddd; color: #333; border-radius: 3px;
    }}
    #new-notes {{ height: 64px; resize: vertical; }}
    .ed-pre {{
      margin-top: 6px; font-family: monospace; font-size: 0.68rem;
      background: #f5f5f5; padding: 6px; border-radius: 3px; white-space: pre-wrap;
      word-break: break-all; max-height: 160px; overflow-y: auto;
      display: none; color: #333;
    }}

    .leaflet-popup-content-wrapper {{
      border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      font-family: 'Zilla Slab', Georgia, serif;
    }}
    .leaflet-popup-content {{ margin: 14px 16px; }}
    .popup-name  {{ font-size: 0.95rem; font-weight: 600; color: #111; margin-bottom: 3px; }}
    .popup-meta  {{ font-family: 'Work Sans', sans-serif; font-size: 0.72rem; color: #777; margin-bottom: 10px; }}
    .popup-desc  {{ font-size: 0.82rem; line-height: 1.65; color: #333; max-width: 300px; }}
    .popup-tags  {{ margin-top: 10px; display: flex; flex-wrap: wrap; gap: 4px; }}
    .tag {{
      font-family: 'Work Sans', sans-serif;
      font-size: 0.67rem; padding: 2px 7px; border-radius: 4px;
      border: 1px solid; display: inline-block;
    }}
    .popup-coords {{ margin-top: 8px; font-family: monospace; font-size: 0.68rem; color: #aaa; }}

    #legend {{
      position: absolute; bottom: 30px; left: 12px; z-index: 1000;
      background: #fff; padding: 12px 14px; border-radius: 6px;
      box-shadow: 0 1px 5px rgba(0,0,0,0.12);
      font-family: 'Zilla Slab', Georgia, serif; font-size: 0.82rem; color: #333;
    }}
    .legend-item {{ font-family: 'Work Sans', sans-serif; display: flex; align-items: center; gap: 8px; line-height: 1.9; }}
    .swatch {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }}
    .legend-rule {{ border: none; border-top: 1px solid #e8e8e8; margin: 6px 0; }}
    .legend-note {{ font-family: 'Work Sans', sans-serif; font-size: 0.7rem; color: #999; margin-top: 4px; }}
  </style>
</head>
<body>
  <div id="title">North Leith</div>

  <button id="edit-toggle" onclick="toggleEditor()">Edit</button>

  <div id="corrections">
    <h3>COORDINATE EDITOR</h3>
    <div id="coord-display">Click map for coordinates</div>

    <div class="ed-section">
      <div class="ed-label">Corrections</div>
      <p class="ed-note">Drag a marker to move it. Click a marker in edit mode to record its position.</p>
      <div class="btn-row">
        <button class="ed-btn amber" onclick="exportCorrections()">Export</button>
        <button class="ed-btn" onclick="clearCorrections()">Clear</button>
      </div>
      <pre id="export-out" class="ed-pre"></pre>
    </div>

    <div class="ed-section">
      <div class="ed-label">New markers</div>
      <input id="new-name" type="text" placeholder="Name" />
      <textarea id="new-notes" placeholder="Notes / description to look up later"></textarea>
      <div class="btn-row">
        <button id="add-marker-btn" class="ed-btn" onclick="toggleAddMode()">+ Place marker</button>
      </div>
      <div class="btn-row">
        <button class="ed-btn amber" onclick="exportNewMarkers()">Export new</button>
        <button class="ed-btn" onclick="clearNewMarkers()">Clear new</button>
      </div>
      <pre id="new-export-out" class="ed-pre"></pre>
    </div>

    <div class="ed-section">
      <div class="ed-label">Submit</div>
      <p class="ed-note">Opens your mail client with corrections pre-filled. Nothing is sent automatically.</p>
      <div class="btn-row">
        <button class="ed-btn amber" onclick="submitAll()">Submit by email</button>
      </div>
    </div>
  </div>

  <div id="map"></div>

  <div id="legend">
    {chr(10).join(
      f'<div class="legend-item"><span class="swatch" style="background:{c}"></span>{cat.title()}</div>'
      for cat, c in CATEGORY_COLOURS.items()
    )}
    <hr class="legend-rule"/>
    <div class="legend-note">Faded = demolished</div>
  </div>

  <script>
    const FEATURES = {json.dumps(feature_list, ensure_ascii=False)};

    var map = L.map('map', {{ center: [55.9752, -3.1793], zoom: 16 }});
    document.getElementById('title').addEventListener('click', function() {{
      map.setView([55.9752, -3.1793], 16);
    }});

    const modernLayer = L.tileLayer(
      'https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png',
      {{
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/">CARTO</a>',
        subdomains: 'abcd', maxZoom: 20,
      }}
    );

    // NLS OS 25-inch Scotland 1892–1905 — scotland_1 tileset covers Leith
    const os25Layer = L.tileLayer(
      'https://mapseries-tilesets.s3.amazonaws.com/25_inch/scotland_1/{{z}}/{{x}}/{{y}}.png',
      {{
        attribution: '&copy; <a href="https://maps.nls.uk">National Library of Scotland</a> — OS 25-inch Scotland 1892–1905',
        maxZoom: 18, minZoom: 1, opacity: 1.0,
      }}
    );

    modernLayer.addTo(map);

    L.control.layers(
      {{
        'Modern (CartoDB)':         modernLayer,
        'OS 25-inch 1892–1905':     os25Layer,
      }},
      null,
      {{ position: 'bottomright', collapsed: true }}
    ).addTo(map);

    const LS_CORR = 'nlm-corrections';
    const LS_NEW  = 'nlm-new-markers';
    const SUBMIT_EMAIL = 'north.leith.maps@gmail.com';

    const corrections = JSON.parse(localStorage.getItem(LS_CORR) || '{{}}');
    const newMarkers  = [];
    let   addMode     = false;

    function saveStorage() {{
      localStorage.setItem(LS_CORR, JSON.stringify(corrections));
      const serialisable = newMarkers.map(function(e) {{
        const {{ _marker, ...rest }} = e; return rest;
      }});
      localStorage.setItem(LS_NEW, JSON.stringify(serialisable));
    }}

    function placeNewMarker(entry) {{
      newMarkers.push(entry);
      const m = L.marker([entry.lat, entry.lon], {{
        icon: makeNewIcon(), draggable: true,
      }});
      entry._marker = m;
      const popupHtml = '<b>' + entry.name + '</b>' +
        (entry.notes ? '<br/><span style="font-size:0.8em;color:#555">' + entry.notes + '</span>' : '') +
        '<br/><button class="del-new-marker" style="margin-top:7px;font-size:0.75em;' +
        'padding:2px 8px;cursor:pointer;border:1px solid #ddd;border-radius:3px;' +
        'background:#fff;color:#a00">&#x2715; Remove</button>';
      m.bindPopup(popupHtml);
      m.on('popupopen', function() {{
        const btn = m.getPopup().getElement().querySelector('.del-new-marker');
        if (btn) btn.onclick = function() {{ deleteNewMarker(entry.id); }};
      }});
      m.on('dragend', function() {{
        const p = this.getLatLng();
        entry.lat = +p.lat.toFixed(6);
        entry.lon = +p.lng.toFixed(6);
        document.getElementById('coord-display').textContent =
          entry.lat + ', ' + entry.lon;
        saveStorage();
      }});
      m.addTo(map);
    }}

    function deleteNewMarker(id) {{
      const idx = newMarkers.findIndex(function(e) {{ return e.id === id; }});
      if (idx === -1) return;
      newMarkers[idx]._marker.remove();
      newMarkers.splice(idx, 1);
      saveStorage();
    }}

    // Restore new markers from previous session
    JSON.parse(localStorage.getItem(LS_NEW) || '[]').forEach(placeNewMarker);

    map.on('click', function(e) {{
      const lat = e.latlng.lat.toFixed(6);
      const lon = e.latlng.lng.toFixed(6);
      document.getElementById('coord-display').textContent = lat + ', ' + lon;

      if (addMode) {{
        const name  = document.getElementById('new-name').value.trim() || 'New marker';
        const notes = document.getElementById('new-notes').value.trim();
        placeNewMarker({{ id: 'new-' + Date.now(), name, notes, lat: +lat, lon: +lon }});
        saveStorage();

        addMode = false;
        document.getElementById('add-marker-btn').classList.remove('amber');
        map.getContainer().style.cursor = '';
      }}
    }});

    function makeIcon(colour) {{
      const size = 14;
      return L.divIcon({{
        className: '',
        html: `<div style="width:${{size}}px;height:${{size}}px;background:${{colour}};border-radius:50%;border:2px solid rgba(255,255,255,0.85);box-shadow:0 1px 4px rgba(0,0,0,0.22);cursor:grab"></div>`,
        iconSize: [size, size],
        iconAnchor: [size/2, size/2],
        popupAnchor: [0, -size/2],
      }});
    }}

    function makeNewIcon() {{
      return L.divIcon({{
        className: '',
        html: `<div style="width:18px;height:18px;background:{ACCENT_COLOUR};border-radius:50%;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,0.3);display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;line-height:1;cursor:grab">+</div>`,
        iconSize: [18, 18],
        iconAnchor: [9, 9],
        popupAnchor: [0, -9],
      }});
    }}

    function popupHtml(f, lat, lon) {{
      const tags = [];
      if (f.gladstone)
        tags.push(`<span class="tag" style="color:{GLADSTONE_COLOUR};border-color:{GLADSTONE_COLOUR}55;background:{GLADSTONE_COLOUR}11">Gladstone</span>`);
      if (f.colonial_link)
        tags.push(`<span class="tag" style="color:#555;border-color:#ccc;background:#f9f9f9">Colonial link</span>`);
      if (f.listed !== 'unlisted')
        tags.push(`<span class="tag" style="color:#555;border-color:#ccc;background:#f9f9f9">Listed ${{f.listed}}</span>`);
      if (f.status !== 'extant')
        tags.push(`<span class="tag" style="color:#a00;border-color:#fcc;background:#fff5f5">${{f.status.charAt(0).toUpperCase()+f.status.slice(1)}}</span>`);
      return `
        <div class="popup-name">${{f.name}}</div>
        <div class="popup-meta">${{f.dates}} &middot; ${{f.address}}</div>
        <div class="popup-desc">${{f.description}}</div>
        <div class="popup-tags">${{tags.join('')}}</div>
        <div class="popup-coords">${{lat.toFixed(6)}}, ${{lon.toFixed(6)}}</div>
      `;
    }}

    FEATURES.forEach(function(f) {{
      const marker = L.marker([f.lat, f.lon], {{
        icon: makeIcon(f.colour),
        draggable: true,
        opacity: f.status === 'demolished' ? 0.4 : 1.0,
      }});
      marker.bindPopup(popupHtml(f, f.lat, f.lon), {{ maxWidth: 360 }});
      function recordPos(marker, pos) {{
        corrections[f.id] = {{ lat: +pos.lat.toFixed(6), lon: +pos.lng.toFixed(6) }};
        document.getElementById('coord-display').textContent =
          pos.lat.toFixed(6) + ', ' + pos.lng.toFixed(6);
        marker.setPopupContent(popupHtml(f, pos.lat, pos.lng));
        saveStorage();
      }}
      marker.on('dragend', function() {{ recordPos(this, this.getLatLng()); }});
      marker.on('click', function() {{
        const pos = this.getLatLng();
        document.getElementById('coord-display').textContent =
          pos.lat.toFixed(6) + ', ' + pos.lng.toFixed(6);
        if (document.getElementById('edit-toggle').classList.contains('active'))
          recordPos(this, pos);
      }});
      marker.addTo(map);
    }});

    function toggleEditor() {{
      const panel = document.getElementById('corrections');
      const btn   = document.getElementById('edit-toggle');
      const open  = panel.style.display === 'block';
      panel.style.display = open ? 'none' : 'block';
      btn.classList.toggle('active', !open);
      if (open && addMode) {{
        addMode = false;
        document.getElementById('add-marker-btn').classList.remove('amber');
        map.getContainer().style.cursor = '';
      }}
    }}

    function exportCorrections() {{
      if (Object.keys(corrections).length === 0) {{
        alert('No corrections recorded yet.');
        return;
      }}
      const out = JSON.stringify(corrections, null, 2);
      navigator.clipboard.writeText(out).catch(() => {{}});
      const el = document.getElementById('export-out');
      el.textContent = out;
      el.style.display = 'block';
    }}

    function clearCorrections() {{
      Object.keys(corrections).forEach(k => delete corrections[k]);
      const el = document.getElementById('export-out');
      el.textContent = '';
      el.style.display = 'none';
      document.getElementById('coord-display').textContent = 'Click map for coordinates';
      saveStorage();
    }}

    function toggleAddMode() {{
      addMode = !addMode;
      document.getElementById('add-marker-btn').classList.toggle('amber', addMode);
      map.getContainer().style.cursor = addMode ? 'crosshair' : '';
    }}

    function exportNewMarkers() {{
      if (newMarkers.length === 0) {{
        alert('No new markers placed yet.');
        return;
      }}
      const out = JSON.stringify(newMarkers, null, 2);
      navigator.clipboard.writeText(out).catch(() => {{}});
      const el = document.getElementById('new-export-out');
      el.textContent = out;
      el.style.display = 'block';
    }}

    function clearNewMarkers() {{
      newMarkers.forEach(function(e) {{ e._marker.remove(); }});
      newMarkers.length = 0;
      const el = document.getElementById('new-export-out');
      el.textContent = '';
      el.style.display = 'none';
      saveStorage();
    }}

    function submitAll() {{
      const hasCorr = Object.keys(corrections).length > 0;
      const hasNew  = newMarkers.length > 0;
      if (!hasCorr && !hasNew) {{
        alert('Nothing to submit — move a marker or add a new one first.');
        return;
      }}
      const payload = {{}};
      if (hasCorr) payload.corrections = corrections;
      if (hasNew)  payload.new_markers  = newMarkers;
      const subject = 'North Leith map corrections';
      const body    = JSON.stringify(payload, null, 2);
      window.location.href =
        'mailto:' + SUBMIT_EMAIL +
        '?subject=' + encodeURIComponent(subject) +
        '&body='    + encodeURIComponent(body);
    }}
  </script>
</body>
</html>"""

    out = OUT_MAP / "index.html"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"  Browser map → {out}  ({len(feature_list)} features, draggable)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("North Leith — building map outputs\n")
    build_kml(FEATURES)
    build_geojson(FEATURES)
    build_shapefile(FEATURES)
    build_map(FEATURES)
    print("\nDone.")
