"""
Canonical feature dataset for the North Leith Neighbourhood History Map.

Coordinates are WGS84 (EPSG:4326), stored as lat/lon decimal degrees.
All coordinates marked approximate — require ground-truthing against OS data.
GeoJSON output uses lon/lat order; KML uses lat/lon order.
"""

FEATURES = [

    # -------------------------------------------------------------------------
    # GLADSTONE LAYER — priority features directly associated with John Gladstone
    # -------------------------------------------------------------------------

    {
        "id": "st-thomas-church",
        "name": "St Thomas's Church / Guru Nanak Gurdwara",
        "category": "religious",
        "date_from": 1840,
        "date_to": None,
        "address": "Sheriff Brae, Edinburgh EH6 6QX",
        "listed": "unlisted",
        "gladstone": True,
        "colonial_link": True,
        "description": (
            "Built and endowed by John Gladstone in 1840, designed by architect John Henderson. "
            "Gladstone, whose wealth derived in part from Caribbean plantation slavery and the "
            "subsequent slave-owner compensation scheme, funded the church as an act of "
            "philanthropy in the neighbourhood of his birth. The adjacent manse was destroyed "
            "by a Zeppelin bomb in April 1916. The church later converted to the Guru Nanak "
            "Dev Ji Gurdwara, now serving Edinburgh's Sikh community — a layered history of "
            "colonial religion repurposed by a post-colonial diaspora."
        ),
        "sources": [
            "Historic Environment Scotland / Trove.scot",
            "UCL Legacies of British Slave-ownership database — lbs.ucl.ac.uk",
            "Bank of England working paper 1006: The collection of slavery compensation, 1835–43",
        ],
        "status": "converted",
        "lat": 55.97457,
        "lon": -3.175478,
    },

    {
        "id": "st-thomas-manse",
        "name": "St Thomas's Manse",
        "category": "residential",
        "date_from": 1840,
        "date_to": 1916,
        "address": "Sheriff Brae, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": True,
        "colonial_link": True,
        "description": (
            "The manse of St Thomas's Church, built as part of John Gladstone's philanthropic "
            "complex on Sheriff Brae in 1840. Destroyed by a Zeppelin bomb in April 1916 — "
            "one of the earliest civilian bombing casualties in Edinburgh. The site is part "
            "of the 1916 Zeppelin raid pattern distinct from the 1941 Luftwaffe attacks that "
            "struck much of the rest of the neighbourhood."
        ),
        "sources": [
            "Historic Environment Scotland / Trove.scot",
            "Leith Local History Society — leithlocalhistorysociety.org.uk",
        ],
        "status": "demolished",
        "lat": 55.974687,
        "lon": -3.175226,
    },

    {
        "id": "st-thomas-almshouse",
        "name": "St Thomas's Almshouses",
        "category": "welfare",
        "date_from": 1840,
        "date_to": None,
        "address": "Sheriff Brae, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": True,
        "colonial_link": True,
        "description": (
            "Accommodation for ten women, also described in contemporary records as an asylum, "
            "endowed by John Gladstone as part of his philanthropic complex at Sheriff Brae. "
            "Built 1840. Current status requires ground-truthing — the site may be incorporated "
            "into later residential development."
        ),
        "sources": [
            "Ordnance Survey Name Books, Midlothian 1852 — scotlandsplaces.gov.uk",
            "Historic Environment Scotland / Trove.scot",
        ],
        "status": "extant",
        "lat": 55.974693,
        "lon": -3.17595,
    },

    {
        "id": "st-thomas-schools",
        "name": "St Thomas's Schools (boys and girls)",
        "category": "educational",
        "date_from": 1840,
        "date_to": None,
        "address": "Sheriff Brae, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": True,
        "colonial_link": True,
        "description": (
            "Schools for boys and girls endowed by John Gladstone's bequest, part of the "
            "philanthropic complex at Sheriff Brae. Average attendance recorded in 1852 as "
            "80 boys and 120 girls. The schools were among the few free educational "
            "institutions in the area at this period."
        ),
        "sources": [
            "Ordnance Survey Name Books, Midlothian 1852 — scotlandsplaces.gov.uk",
            "Historic Environment Scotland / Trove.scot",
        ],
        "status": "extant",
        "lat": 55.974696,
        "lon": -3.176068,
    },

    {
        "id": "mill-lane-schools",
        "name": "Mill Lane Schools / Gladstones",
        "category": "educational",
        "date_from": 1838,
        "date_to": None,
        "address": "Mill Lane / Great Junction Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": True,
        "colonial_link": True,
        "description": (
            "Built by John Gladstone in 1838, two years before the Sheriff Brae complex, "
            "these schools were the first institution in the area to provide free education "
            "to girls. Later renamed Gladstones in honour of their founder. Significant as "
            "an early example of female education provision in Leith."
        ),
        "sources": [
            "Leith Local History Society — leithlocalhistorysociety.org.uk",
            "City of Edinburgh Council planning portal",
        ],
        "status": "extant",
        "lat": 55.974696,
        "lon": -3.176181,
    },

    {
        "id": "gladstone-birthplace",
        "name": "Gladstone Birthplace / Plaque",
        "category": "memorial",
        "date_from": 1764,
        "date_to": None,
        "address": "King Street / Great Junction Street junction, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": True,
        "colonial_link": True,
        "description": (
            "Birthplace of John Gladstones (later Gladstone), born 1764. Gladstone went on "
            "to become a Liverpool merchant whose fortune was substantially built on Caribbean "
            "plantation slavery; he received one of the largest compensation payments under "
            "the 1833 Slavery Abolition Act. A commemorative plaque was erected in 1909. "
            "The original building has been demolished."
        ),
        "sources": [
            "Wikipedia: Sir John Gladstone, 1st Baronet",
            "UCL Legacies of British Slave-ownership database — lbs.ucl.ac.uk",
            "Capital Collections (Edinburgh) — capitalcollections.org.uk",
        ],
        "status": "demolished",
        "lat": 55.973366,
        "lon": -3.176127,
    },

    {
        "id": "rose-garden",
        "name": "Gladstone Rose Garden",
        "category": "memorial",
        "date_from": 1838,
        "date_to": None,
        "address": "Sheriff Brae vicinity, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": True,
        "colonial_link": True,
        "description": (
            "Public rose garden established as part of John Gladstone's philanthropic complex "
            "at Sheriff Brae, c.1838. Precise location and current status require "
            "ground-truthing."
        ),
        "sources": [
            "Leith Local History Society — leithlocalhistorysociety.org.uk",
        ],
        "status": "extant",
        "lat": 55.974573,
        "lon": -3.175784,
    },

    # -------------------------------------------------------------------------
    # WIDER NEIGHBOURHOOD LAYER — secondary features
    # -------------------------------------------------------------------------

    {
        "id": "kyle-place",
        "name": "Kyle Place / 26–28 Madeira Street",
        "category": "residential",
        "date_from": 1840,
        "date_to": None,
        "address": "26–28 Madeira Street, Edinburgh EH6 4AT",
        "listed": "C",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Category C listed Victorian tenement. Notable for its schooner relief — a "
            "carved sailing vessel on the façade — reflecting the maritime character of "
            "the neighbourhood. The pend (covered close) was widened around 1914. "
            "A significant example of the residential architecture of North Leith."
        ),
        "sources": [
            "Historic Environment Scotland / Trove.scot",
            "City of Edinburgh Council planning portal",
        ],
        "status": "extant",
        "lat": 55.975542,
        "lon": -3.181695,
    },

    {
        "id": "north-leith-poorhouse",
        "name": "North Leith Poorhouse",
        "category": "welfare",
        "date_from": 1863,
        "date_to": 1906,
        "address": "North Junction Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Poorhouse constructed 1863, designed by architect Peter Hamilton. Capacity of "
            "approximately 120 inmates. Superseded by the joint Seafield Poorhouse (1906–08), "
            "which served multiple Edinburgh parishes. The site was subsequently used for the "
            "David Kilpatrick School, and later became the Ferrylee Care Home — a continuous "
            "thread of welfare provision on the same ground across 160 years."
        ),
        "sources": [
            "National Records of Scotland — poorhouse and parish records",
            "Historic Environment Scotland / Trove.scot",
            "Leith Local History Society — leithlocalhistorysociety.org.uk/junction_street/north_leith_poorhouse.htm",
        ],
        "status": "demolished",
        "lat": 55.976104,
        "lon": -3.180853,
    },

    {
        "id": "david-kilpatrick-school",
        "name": "David Kilpatrick School",
        "category": "educational",
        "date_from": 1915,
        "date_to": 1975,
        "address": "North Junction Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "School designed by architect George Craig, constructed 1915, on the site of the "
            "former North Leith Poorhouse. Used as a military barracks during 1915–19. The "
            "annexe, known locally as 'the Bombies', was damaged in the April 1941 Luftwaffe "
            "bombing raids that struck much of North Leith. Demolished in the 1970s. The site "
            "is now occupied by Ferrylee Care Home. A stone plaque from the school survives "
            "on the boundary of the open ground."
        ),
        "sources": [
            "Canmore / Trove.scot — canmore.org.uk/site/188370",
            "Leith Local History Society — leithlocalhistorysociety.org.uk/junction_street/david_kilpatrick_school.htm",
            "City of Edinburgh Council planning portal",
        ],
        "status": "demolished",
        "lat": 55.976125,
        "lon": -3.180799,
    },

    {
        "id": "north-leith-parish-church",
        "name": "North Leith Parish Church",
        "category": "religious",
        "date_from": 1816,
        "date_to": 2024,
        "address": "51 Madeira Street, Edinburgh EH6 4QS",
        "listed": "A",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Category A listed church designed by William Burn, completed 1816. Damaged in "
            "the April 1941 Luftwaffe bombing raids. Closed March 2024 and offered for sale — "
            "part of the wider decline of the Church of Scotland's estate in central Leith. "
            "One of the most significant listed buildings on Madeira Street."
        ),
        "sources": [
            "Historic Environment Scotland / Trove.scot",
            "City of Edinburgh Council planning portal",
        ],
        "status": "damaged",
        "lat": 55.976016,
        "lon": -3.183026,
    },

    {
        "id": "norwegian-seamen-church",
        "name": "Norwegian Seaman's Lutheran Church / Leith School of Art",
        "category": "maritime",
        "date_from": 1868,
        "date_to": None,
        "address": "25 North Junction Street, Edinburgh EH6 6HW",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Built 1868 for the Norwegian seafaring community in Leith, designed by Johan "
            "Schroder with James Simpson. Distinguished by its fish-scale spire and Vim Stone "
            "construction. King Haakon VII visited in 1941 during the Norwegian government-in-exile. "
            "Now houses the Leith School of Art — another instance of a purpose-built "
            "religious/community building repurposed for the arts."
        ),
        "sources": [
            "Leith Local History Society — leithlocalhistorysociety.org.uk",
            "Historic Environment Scotland / Trove.scot",
        ],
        "status": "converted",
        "lat": 55.976095,
        "lon": -3.179686,
    },

    {
        "id": "leith-theatre",
        "name": "Leith Theatre / Thomas Morton Hall",
        "category": "civic",
        "date_from": 1932,
        "date_to": 1988,
        "address": "28–30 Ferry Road, Edinburgh EH6 4AE",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Civic theatre and hall designed by Bradshaw Gass & Hope, opened 1932. Also known "
            "as Thomas Morton Hall. Damaged in the April 1941 Luftwaffe bombing raids. Operated "
            "as a rock venue in the 1970s before closing in 1988. Listed on the Theatres at Risk "
            "Register. A 50-year lease was secured in 2025, offering the prospect of restoration."
        ),
        "sources": [
            "Leith Local History Society — leithlocalhistorysociety.org.uk",
            "Historic Environment Scotland / Trove.scot",
        ],
        "status": "damaged",
        "lat": 55.975713,
        "lon": -3.180403,
    },

    {
        "id": "leith-mount",
        "name": "Leith Mount / 46 Ferry Road",
        "category": "welfare",
        "date_from": 1825,
        "date_to": None,
        "address": "46 Ferry Road, Edinburgh EH6 4AE",
        "listed": "B",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Category B listed Georgian manse, c.1825. Now operating as a council-contracted "
            "homeless hostel run by K & S Mir Ltd. One of the more intact Georgian buildings "
            "remaining in North Leith, its current use as welfare accommodation continues a "
            "pattern of institutional repurposing across the neighbourhood."
        ),
        "sources": [
            "Historic Environment Scotland / Trove.scot",
            "City of Edinburgh Council planning portal",
        ],
        "status": "converted",
        "lat": 55.975242,
        "lon": -3.181073,
    },

    {
        "id": "sinclair-bagpipes",
        "name": "Wm Sinclair & Son Bagpipe Makers",
        "category": "commercial",
        "date_from": 1931,
        "date_to": None,
        "address": "1 Madeira Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": True,
        "description": (
            "Family bagpipe-making business, five generations, operating from c.1931. "
            "Instruments made from African blackwood (Dalbergia melanoxylon), sourced from "
            "Tanzania and Mozambique — connecting the Madeira Street workshop to a global "
            "supply chain that passes through Liverpool, itself connected to the colonial "
            "trade networks in which John Gladstone's family also operated. Still in business."
        ),
        "sources": [
            "Piping Press / sinclair-bagpipes.co.uk — Sinclair family history",
            "African Blackwood Conservation Project — blackwoodconservation.org",
        ],
        "status": "extant",
        "lat": 55.975107,
        "lon": -3.181631,
    },

    {
        "id": "ferrylee-care-home",
        "name": "Ferrylee Care Home",
        "category": "welfare",
        "date_from": 1975,
        "date_to": None,
        "address": "33 North Junction Street, Edinburgh EH6 6HR",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Care home built post-1970s on the site of the former David Kilpatrick School "
            "and, before that, the North Leith Poorhouse. Operated by City of Edinburgh "
            "Council; 43 rooms, providing residential, dementia and respite care. The "
            "sequence of uses on this ground — poorhouse (1863), school (1915), barracks "
            "(1915–19), bomb damage (1941), demolition (1970s), care home (c.1975) — "
            "traces the changing institutional response to poverty and dependency across "
            "160 years."
        ),
        "sources": [
            "City of Edinburgh Council — edinburgh.gov.uk/directory-record/1114595/ferrylee",
            "Care Inspectorate Scotland",
        ],
        "status": "extant",
        "lat": 55.976146,
        "lon": -3.181003,
    },

    # -------------------------------------------------------------------------
    # MILITARY / DEFENSIVE
    # -------------------------------------------------------------------------

    {
        "id": "leith-fort",
        "name": "Leith Fort",
        "category": "military",
        "date_from": 1780,
        "date_to": 1960,
        "address": "North Fort Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Artillery fort built from 1780 to defend the port of Leith against seaborne attack, "
            "prompted by the threat from the American privateer John Paul Jones in 1779. Designed "
            "by James Craig — better known for the plan of Edinburgh's New Town — under the "
            "practical supervision of Captain Andrew Frazer, Chief Engineer for Scotland. Paid "
            "for jointly by Edinburgh and Leith. Largely demolished c.1960; a housing scheme "
            "on the site was itself demolished in 2013 and replaced. The gate lodges on North "
            "Fort Street survive."
        ),
        "sources": [
            "Threadinburgh — threadinburgh.scot/2022/11/24/the-thread-about-leith-fort",
            "Canmore / Trove.scot — canmore.org.uk/site/145502",
            "Capital Collections (Edinburgh) — capitalcollections.org.uk",
        ],
        "status": "demolished",
        "lat": 55.977034,
        "lon": -3.184855,
    },

    {
        "id": "citadel",
        "name": "The Citadel",
        "category": "military",
        "date_from": 1653,
        "date_to": 1660,
        "address": "Dock Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Pentagonal Cromwellian fortress ordered in 1653, overseen by General George Monck "
            "following the Parliamentary victory at Dunbar in 1650. Built to control the port "
            "of Leith and regulate access to Edinburgh. Financed under duress by Edinburgh "
            "Corporation to the sum of £5,000 sterling. Largely demolished after the Restoration "
            "of the monarchy in 1660. A vaulted gateway on Dock Street is the only significant "
            "surviving remnant."
        ),
        "sources": [
            "Leith Local History Society — leithlocalhistorysociety.org.uk/fortifications/citadel.htm",
            "Threadinburgh — threadinburgh.scot/2022/09/09",
        ],
        "status": "demolished",
        "lat": 55.976413,
        "lon": -3.175741,
    },

    # -------------------------------------------------------------------------
    # MARITIME / CIVIC
    # -------------------------------------------------------------------------

    {
        "id": "trinity-house",
        "name": "Trinity House",
        "category": "maritime",
        "date_from": 1816,
        "date_to": None,
        "address": "99 Kirkgate, Edinburgh EH6 6BJ",
        "listed": "A",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Category A listed guild hall of the Incorporation of Master and Mariners of Leith, "
            "an institution founded by charter of Robert II in 1380. The current building was "
            "designed by Thomas Brown and completed in 1816 on the site of an earlier Trinity "
            "House and hospital dating from 1555. The Convening Room contains an ornate plaster "
            "frieze, a long mahogany table, and portraits by Sir Henry Raeburn. Collections "
            "include navigational instruments, charts, whaling harpoons, and model ships. "
            "Now in state care as a maritime museum."
        ),
        "sources": [
            "Historic Environment Scotland — historicenvironment.scot/visit-a-place/places/trinity-house",
            "Trinity House of Leith — Wikipedia",
        ],
        "status": "converted",
        "lat": 55.972162,
        "lon": -3.17138,
    },

    {
        "id": "leith-custom-house",
        "name": "Leith Custom House",
        "category": "civic",
        "date_from": 1812,
        "date_to": None,
        "address": "65–67 Commercial Street, Edinburgh EH6 6LH",
        "listed": "A",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Category A listed neo-classical custom house designed by Robert Reid and built "
            "1810–12, with additions and alterations by William Burn in 1825. Cream sandstone "
            "ashlar, symmetrical eleven-bay frontage. In use as a customs facility until 1980, "
            "then as a museum store. Acquired by the City of Edinburgh through its Common Good "
            "Fund in 2015. Now managed by the Scottish Historic Buildings Trust as an arts and "
            "events hub, with long-term restoration plans under development."
        ),
        "sources": [
            "Scottish Historic Buildings Trust — shbt.org.uk/our-buildings/custom-house",
            "Historic Environment Scotland LB26787",
        ],
        "status": "converted",
        "lat": 55.976672,
        "lon": -3.170918,
    },

    {
        "id": "lambs-house",
        "name": "Lamb's House",
        "category": "commercial",
        "date_from": 1610,
        "date_to": None,
        "address": "Water Street, Edinburgh EH6 6RB",
        "listed": "A",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Category A listed early 17th-century merchant's house and warehouse, built c.1610 "
            "for Andrew Lamb, a prosperous Leith merchant trading with the Hanseatic ports. "
            "Mary Queen of Scots reputedly rested here on her return to Scotland in 1561, though "
            "the present building post-dates that event. Original features include crow-stepped "
            "gables, a stone turnpike staircase, leaded windows, and Baltic pine beams. Formerly "
            "a National Trust for Scotland property used as a day centre. Sensitively restored "
            "2010–16 by conservation architect Nicholas Groves-Raines; RIAS Award winner 2016."
        ),
        "sources": [
            "Lamb's House — Wikipedia",
            "GRAS — gras.co/projects/lambs-house",
            "Canmore / Trove.scot — canmore.org.uk/site/51956",
        ],
        "status": "converted",
        "lat": 55.975199,
        "lon": -3.169402,
    },

    # -------------------------------------------------------------------------
    # RELIGIOUS
    # -------------------------------------------------------------------------

    {
        "id": "south-leith-parish-church",
        "name": "South Leith Parish Church",
        "category": "religious",
        "date_from": 1483,
        "date_to": None,
        "address": "Kirkgate, Edinburgh EH6 6BJ",
        "listed": "A",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Category A listed church with origins as a chapel dedicated to St Mary, first built "
            "1483. Used as a magazine by Cromwellian troops 1650–57. Current building largely "
            "1847–48 by Thomas Hamilton, retaining the layout and part of the aisle walls of the "
            "earlier church. Contains a magnificent hammer-beam ceiling, stained glass, and the "
            "colours of the 1st/7th Battalion Royal Scots, commemorating losses in the "
            "Quintinshill rail disaster of 1915. The kirkyard is burial place of John Home and "
            "of John Pew, said to be Robert Louis Stevenson's model for Blind Pew in "
            "Treasure Island. In 2024 united with North Leith Parish Church."
        ),
        "sources": [
            "South Leith Parish Church — Wikipedia",
            "Historic Environment Scotland / Trove.scot",
        ],
        "status": "extant",
        "lat": 55.972012,
        "lon": -3.17058,
    },

    # -------------------------------------------------------------------------
    # POORHOUSES
    # -------------------------------------------------------------------------

    {
        "id": "south-leith-poorhouse",
        "name": "South Leith Poorhouse / Taylor Gardens",
        "category": "welfare",
        "date_from": 1850,
        "date_to": 1911,
        "address": "Taylor Gardens, North Junction Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Purpose-built poorhouse for the parish of South Leith, opened 1850 at a cost of "
            "£8,000. Located on the east side of North Junction Street, directly adjacent to "
            "Leith Hospital. Contained separate schoolrooms for boys and girls within the main "
            "building. Following the amalgamation of South and North Leith boards in 1894, both "
            "poorhouses were superseded by the new Seafield Poorhouse (1906–08). The South Leith "
            "building was acquired by Leith Hospital managers and demolished in 1911 to admit "
            "more light and air to the hospital wards. The site is now Taylor Gardens, a "
            "public park."
        ),
        "sources": [
            "Leith Local History Society — leithlocalhistorysociety.org.uk/junction_street/south_leith_poorhouse.htm",
            "Workhouses.org.uk — workhouses.org.uk/Leith",
            "Canmore — canmore.org.uk/site/151628",
        ],
        "status": "demolished",
        "lat": 55.974131,
        "lon": -3.176599,
    },

    {
        "id": "seafield-poorhouse",
        "name": "Seafield Poorhouse / Eastern General Hospital",
        "category": "welfare",
        "date_from": 1906,
        "date_to": None,
        "address": "Seafield Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Built 1906–08 to designs by Joseph Marr Johnston, the Seafield Poorhouse was the "
            "last poorhouse constructed in Scotland and replaced both the North Leith and South "
            "Leith poorhouses following their boards' amalgamation in 1894. Capacity of "
            "approximately 650 inmates. Requisitioned as Leith War Hospital during the First "
            "World War. Subsequently became the Eastern General Hospital, a role it fulfilled "
            "for much of the 20th century. Part of the site is now occupied by Findlay House."
        ),
        "sources": [
            "Workhouses.org.uk — workhouses.org.uk/Leith",
            "Trove.scot — trove.scot/place/74067",
        ],
        "status": "converted",
        "lat": 55.968212,
        "lon": -3.146091,
    },

    # -------------------------------------------------------------------------
    # SCHOOLS — HISTORICAL
    # -------------------------------------------------------------------------

    {
        "id": "leith-academy-links",
        "name": "Leith Academy (Leith Links building)",
        "category": "educational",
        "date_from": 1806,
        "date_to": 1898,
        "address": "Leith Links, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "First purpose-built home of Leith Academy, designed by Robert Burn and completed "
            "in 1806 beside Leith Links. The school itself dates to 1560, when it was founded "
            "in South Leith Parish Church; records mention a grammar school in Leith as early "
            "as 1521. Demolished 1896 and replaced by a new building on the same site in 1898."
        ),
        "sources": [
            "Leith Academy — Wikipedia",
            "QMU — qmu.ac.uk/about-the-university/qmu150/qmu150-150-stories/places/leith-academy-in-duke-street",
        ],
        "status": "demolished",
        "lat": 55.970433,
        "lon": -3.168767,
    },

    {
        "id": "leith-academy-duke-street",
        "name": "Leith Academy (Duke Street building)",
        "category": "educational",
        "date_from": 1931,
        "date_to": 1991,
        "address": "Duke Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Second replacement building for Leith Academy, opened 1931 after the school "
            "outgrew its Leith Links premises. In use as the school until the current Easter "
            "Road building opened in 1991. The Duke Street building subsequently became part "
            "of Queen Margaret University's Leith campus."
        ),
        "sources": [
            "Leith Academy — Wikipedia",
            "QMU — qmu.ac.uk/about-the-university/qmu150",
        ],
        "status": "converted",
        "lat": 55.969295,
        "lon": -3.167667,
    },

    {
        "id": "fort-primary-school",
        "name": "Fort Primary School",
        "category": "educational",
        "date_from": 1880,
        "date_to": 1968,
        "address": "North Fort Street, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "School within the Leith Fort complex on North Fort Street. Thomas Trotter, who "
            "later became the first rector of Trinity Academy, taught here. The building served "
            "as a school annex until 1968 and as a community club for a period thereafter, "
            "before demolition. Flats now occupy the site."
        ),
        "sources": [
            "EdinPhoto — edinphoto.org.uk/1_edin/1_edinburgh_history_-_recollections_north_fort_street_primary_school.htm",
        ],
        "status": "demolished",
        "lat": 55.977364,
        "lon": -3.186019,
    },

    {
        "id": "bonnington-primary-school",
        "name": "Bonnington Primary School / Bun-sgoil Taobh na Pàirce",
        "category": "educational",
        "date_from": 1875,
        "date_to": None,
        "address": "Bonnington Road, Edinburgh EH6",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Victorian Board school built 1875–77 to designs by James Simpson — the same "
            "architect who designed the Norwegian Seaman's Lutheran Church on North Junction "
            "Street. Extended in 1907 by George Craig, who would later design David Kilpatrick "
            "School in 1915. Now houses Bun-sgoil Taobh na Pàirce, Edinburgh's Gaelic-medium "
            "primary school — another instance of a historic school building repurposed for a "
            "new educational community."
        ),
        "sources": [
            "Bun-sgoil Taobh na Pàirce — Wikipedia",
        ],
        "status": "converted",
        "lat": 55.970535,
        "lon": -3.179898,
    },

    {
        "id": "lorne-street-primary",
        "name": "Lorne Street Primary School",
        "category": "educational",
        "date_from": 1876,
        "date_to": None,
        "address": "7 Lorne Street, Edinburgh EH6 8QS",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Victorian Board school, original building opened 1876. A multicultural and diverse "
            "school community reflecting the character of contemporary Leith. The building "
            "suffered a fire, closed, and reopened in 1973. The Victorian structure survives."
        ),
        "sources": [
            "Lorne Primary School — lorneprimary.co.uk",
        ],
        "status": "extant",
        "lat": 55.966203,
        "lon": -3.174561,
    },

    # -------------------------------------------------------------------------
    # SCHOOLS — CURRENT
    # -------------------------------------------------------------------------

    {
        "id": "leith-academy",
        "name": "Leith Academy",
        "category": "educational",
        "date_from": 1991,
        "date_to": None,
        "address": "20 Academy Park, Easter Road, Edinburgh EH6 8JQ",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Current building of Leith Academy, opened 1991 after sustained campaigning by "
            "staff, students and parents. The only secondary school serving the Leith area. "
            "The school's history stretches back to 1560. Former pupils of David Kilpatrick "
            "School, which closed in 1975, were transferred to Trinity Academy."
        ),
        "sources": [
            "Leith Academy — leithacademy.uk",
            "Leith Academy — Wikipedia",
        ],
        "status": "extant",
        "lat": 55.967866,
        "lon": -3.167034,
    },

    {
        "id": "leith-primary-school",
        "name": "Leith Primary School",
        "category": "educational",
        "date_from": None,
        "date_to": None,
        "address": "St Andrew Place, Edinburgh EH6 7EG",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Current primary school serving the Leith area. Associated secondary school is "
            "Leith Academy."
        ),
        "sources": [
            "City of Edinburgh Council — edinburgh.gov.uk/directory-record/1697749/leith-primary-school",
        ],
        "status": "extant",
        "lat": 55.970442,
        "lon": -3.168821,
    },

    {
        "id": "hermitage-park-primary",
        "name": "Hermitage Park Primary School",
        "category": "educational",
        "date_from": None,
        "date_to": None,
        "address": "9 Hermitage Park, Edinburgh EH6 8HD",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Current primary school in the Hermitage Park area of Leith."
        ),
        "sources": [
            "City of Edinburgh Council — edinburgh.gov.uk/directory-record/1697743/hermitage-park-primary-school",
        ],
        "status": "extant",
        "lat": 55.965718,
        "lon": -3.16218,
    },

    {
        "id": "fort-early-years",
        "name": "Fort Early Years Centre",
        "category": "educational",
        "date_from": None,
        "date_to": None,
        "address": "North Fort Street, Edinburgh EH6 4HJ",
        "listed": "unlisted",
        "gladstone": False,
        "colonial_link": False,
        "description": (
            "Current early years and childcare centre on North Fort Street, on the site of "
            "the former Leith Fort and Fort Primary School."
        ),
        "sources": [
            "City of Edinburgh Council — edinburgh.gov.uk/directory-record/1581141/fort-early-years-centre",
        ],
        "status": "extant",
        "lat": 55.976476,
        "lon": -3.185831,
    },
]
