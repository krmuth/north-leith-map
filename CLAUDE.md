# CLAUDE.md — North Leith Neighbourhood History Map

## Project overview

This project maps the layered history of a small area of North Leith, Edinburgh (centred on Madeira Street, EH6) using geospatial data compatible with **Google Earth** (KML/KMZ) and **ArcGIS** (GeoJSON / Shapefile). The primary output is a richly annotated spatial dataset that can be interrogated, styled, and extended over time.

The researcher is a literary critic living in Leith. The project began as a series of conversations tracing the connections between specific buildings on and around Madeira Street — a Victorian tenement, a bombed church, a Georgian manse now used as a homeless hostel — and has expanded to encompass the economic and colonial history of the neighbourhood as embedded in its built fabric.

The immediate research focus is **John Gladstone's economic imprint on North Leith**, but the ambition is broader: a single georeferenced dataset capturing the neighbourhood's overlapping histories — maritime, colonial, philanthropic, military, ecclesiastical, industrial.

---

## Output formats

All outputs should be produced in the following formats unless instructed otherwise:

- **KML** — for Google Earth visualisation (supports rich HTML descriptions, icons, folders, time spans)
- **GeoJSON** — for ArcGIS and web mapping (lightweight, widely supported)
- **Shapefile (.shp/.dbf/.prj/.shx)** — for ArcGIS desktop workflows requiring vector layers

Where possible, produce KML as the primary authored format and derive GeoJSON from it, since KML supports richer inline annotation.

---

## Coordinate system

- All coordinates in **WGS84 (EPSG:4326)** — decimal degrees, longitude first in GeoJSON, latitude first in KML
- Precision to 6 decimal places

---

## Data structure

Each feature (point, polygon, or line) should carry the following attributes:

| Field | Type | Notes |
|---|---|---|
| `id` | string | Unique slug, e.g. `st-thomas-church` |
| `name` | string | Display name |
| `category` | string | See categories below |
| `date_from` | integer | Earliest year (construction, founding, event) |
| `date_to` | integer or null | Latest year (demolition, closure); null if extant |
| `address` | string | Modern address where known |
| `listed` | string | Listed building status (A / B / C / unlisted) |
| `gladstone` | boolean | Whether directly associated with John Gladstone |
| `colonial_link` | boolean | Whether the site has a documented colonial connection |
| `description` | string | Full prose annotation (HTML permitted in KML) |
| `sources` | array | Array of source strings or URLs |
| `status` | string | `extant` / `demolished` / `converted` / `damaged` |

---

## Categories

Use these controlled vocabulary terms for the `category` field:

- `religious` — churches, kirks, missions, gurdwaras
- `educational` — schools, colleges
- `welfare` — poorhouses, almshouses, hospitals, care homes, homeless accommodation
- `commercial` — businesses, warehouses, workshops
- `civic` — town halls, libraries, public buildings
- `maritime` — port infrastructure, shipping offices, seamen's institutions
- `residential` — tenements, mansions, manses, guest houses
- `memorial` — plaques, monuments, gardens
- `military` — barracks, fortifications, bomb sites

---

## Current feature inventory

### Gladstone imprint (priority layer)

| id | Name | Location | date_from | Notes |
|---|---|---|---|---|
| `st-thomas-church` | St Thomas's Church / Guru Nanak Gurdwara | Sheriff Brae | 1840 | Built and endowed by Gladstone; architect John Henderson; bombed 1941 (manse); now Sikh temple |
| `st-thomas-manse` | St Thomas's Manse | Sheriff Brae | 1840 | Destroyed by Zeppelin bomb, April 1916 |
| `st-thomas-almshouse` | St Thomas's Almshouses | Sheriff Brae | 1840 | Accommodation for 10 women; also described as asylum |
| `st-thomas-schools` | St Thomas's Schools (boys and girls) | Sheriff Brae | 1840 | Endowed by Gladstone bequest; avg attendance 80 boys / 120 girls (1852) |
| `mill-lane-schools` | Mill Lane Schools / Gladstones | Mill Lane, Great Junction Street | 1838 | Built by Gladstone; first free female education in area; later named Gladstones |
| `gladstone-birthplace` | Gladstone Birthplace / Plaque | King Street / Great Junction Street junction | 1764 | Born John Gladstones; plaque erected 1909; building demolished |
| `rose-garden` | Gladstone Rose Garden | Sheriff Brae vicinity | 1838 | Public rose garden, part of Gladstone philanthropic complex |

### Wider neighbourhood history (secondary layer)

| id | Name | Location | date_from | Notes |
|---|---|---|---|---|
| `kyle-place` | Kyle Place / 26–28 Madeira Street | Madeira Street | c.1840 | Cat. C listed; schooner relief; pend widened c.1914 |
| `north-leith-poorhouse` | North Leith Poorhouse | North Junction Street | 1863 | 120 inmates; Peter Hamilton architect; superseded 1906–08 |
| `david-kilpatrick-school` | David Kilpatrick School | Madeira Street rear | 1915 | George Craig architect; used as barracks 1915–19; bombed 1941; demolished 1970s |
| `north-leith-parish-church` | North Leith Parish Church | 51 Madeira Street | 1816 | William Burn architect; Cat. A listed; bombed 1941; closed March 2024; for sale |
| `norwegian-seamen-church` | Norwegian Seaman's Lutheran Church / Leith School of Art | 25 North Junction Street | 1868 | Johan Schroder + James Simpson architects; fish-scale spire; Vim Stone; King Haakon visited 1941; now Leith School of Art |
| `leith-theatre` | Leith Theatre / Thomas Morton Hall / Leith Library | 28–30 Ferry Road | 1932 | Bradshaw Gass & Hope; bombed 1941; rock venue 1970s; closed 1988; Theatres at Risk Register; 50-year lease secured 2025 |
| `leith-mount` | Leith Mount / 46 Ferry Road | 46 Ferry Road | c.1825 | Cat. B listed Georgian manse; now council-contracted homeless hostel (K & S Mir Ltd) |
| `sinclair-bagpipes` | Wm Sinclair & Son Bagpipe Makers | 1 Madeira Street | c.1931 | Five generations; African blackwood; still operating |
| `ferrylee-care-home` | Ferrylee Care Home | Madeira Street rear | post-1970s | Built on site of David Kilpatrick School / North Leith Poorhouse |

---

## Key relationships to encode

These thematic connections should be expressible as either attribute queries or separate line/polygon layers:

1. **Gladstone colonial circuit** — birthplace → Liverpool → Caribbean plantations → compensation → Leith philanthropy
2. **1941 bombing pattern** — North Leith Parish Church, Norwegian Seamen's Church, David Kilpatrick School annexe ("the Bombies"), Leith Theatre, Largo Place tenements; plus St Thomas's manse (1916 Zeppelin)
3. **Poorhouse to care home continuity** — North Leith Poorhouse site → David Kilpatrick School → Ferrylee Care Home / Mir homeless accommodation
4. **African blackwood supply chain** — Tanzania/Mozambique → Liverpool → Leith (Sinclair workshop at 1 Madeira Street)
5. **Colonial religion repurposed** — St Thomas's (Gladstone / plantation wealth) → Guru Nanak Gurdwara (Sikh community); Norwegian Seamen's Church → Leith School of Art

---

## Coordinates (approximate — require ground-truthing)

```
Madeira Street (approx centre):        55.977800, -3.173900
Kyle Place / 26-28 Madeira Street:     55.977650, -3.174050
North Leith Parish Church:             55.977500, -3.174200
1 Madeira Street (Sinclair):           55.977400, -3.174500
Norwegian Seamen's Church:             55.976800, -3.174800
Leith Theatre / Ferry Road:            55.977200, -3.175500
Leith Mount / 46 Ferry Road:           55.977100, -3.175800
Sheriff Brae / St Thomas's:            55.975800, -3.172500
King St / Great Junction St (plaque):  55.975200, -3.174000
Mill Lane / Great Junction St:         55.975300, -3.174100
```

**Note:** Coordinates are estimated from street-level knowledge and should be verified against OS data or confirmed on-site before final publication. Sheriff Brae and Great Junction Street locations need particular ground-truthing.

---

## Styling conventions (KML)

- **Gladstone layer**: gold/amber (`#ffb300`)
- **Religious**: purple (`#7b1fa2`)
- **Educational**: blue (`#1565c0`)
- **Welfare / poorhouse**: grey (`#546e7a`)
- **Maritime**: teal (`#00695c`)
- **Civic**: red (`#c62828`)
- **Commercial / workshop**: orange (`#e65100`)
- **Demolished / lost**: semi-transparent or dashed
- **Bombed**: red damage marker with year annotation
- **Listed building**: outline polygon where footprint known (A = solid, B = dashed, C = dotted)

---

## Sources and references

- Historic Environment Scotland / Trove.scot — listed building records
- City of Edinburgh Council planning portal — planning application records
- National Records of Scotland — poorhouse, parish, and compensation records
- Leith Local History Society — leithlocalhistorysociety.org.uk
- Wikipedia: Sir John Gladstone, 1st Baronet
- Ordnance Survey Name Books, Midlothian 1852 (scotlandsplaces.gov.uk)
- Piping Press / sinclair-bagpipes.co.uk — Sinclair family history
- African Blackwood Conservation Project — blackwoodconservation.org
- UCL Legacies of British Slave-ownership database — lbs.ucl.ac.uk
- Bank of England working paper 1006: The collection of slavery compensation, 1835–43
- Great Junction Street, Wikipedia
- Capital Collections (Edinburgh) — capitalcollections.org.uk

---

## Relationship to *Settlement*

The researcher is writing a novel provisionally titled *Settlement* — Wharton-influenced, Edinburgh-set, dark domestic realism. This mapping project is independent research but may inform the novel's sense of place and layered time. Material here should be treated as research notes, not as fiction.

---

## Expansion notes

Future layers under consideration:

- **Christian Salvesen** and the Norwegian maritime connection at Leith
- **Leith Fort** (covered in earlier conversation, Document_house_01.docx)
- **The Shore / Coalhill** — Gladstone family origins, tobacco and sugar imports
- **Seafield joint poorhouse** (1906–08) — successor to North Leith Poorhouse
- **Anchor Close / Cockburn Street** — Mir family acquisition 2011
- **Largo Place bombing** — tenements destroyed April 1941, casualties

---

*Last updated: 26 May 2026. Compiled from conversation research. All coordinates and dates subject to verification.*
