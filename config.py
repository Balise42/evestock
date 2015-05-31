# station name
stations = {
    # Jita 4-4
    60003760:
    {
        "mkt_del": [
            ["Helium Isotopes", 500000],
            ["Hydrogen Isotopes", 500000],
            ["Nitrogen Isotopes", 500000],
            ["Oxygen Isotopes", 500000],
            ["Liquid Ozone", 0],
        ],
    },
    # Amamake 4
    60004819:
    {
        "mkt_del": [
            ["Liquid Ozone", 20000],
            ["Cynosural Field Generator I", 20],
            ["Expanded Cargohold I", 20],
        ],
    },
    # Poitot 5-14
    60013465:
    {
        "topes_hangar": [
            ["Helium Isotopes", 350000],
            ["Hydrogen Isotopes", 350000],
            ["Nitrogen Isotopes", 350000],
            ["Oxygen Isotopes", 350000],
            ["Liquid Ozone", 20000],
            ["Cynosural Field Generator I", 20],
            ["Expanded Cargohold I", 20],
        ],
        "skills_bin": [
            ["Caldari Frigate", 10],
            ["Caldari Destroyer", 10],
            ["Caldari Cruiser", 10],
            ["Caldari Battlecruiser", 10],
            ["Caldari Battleship", 10],
            ["Caldari Titan", 10],
        ],
    },
}

loc_aliases = {
    "mkt_del": ["deliveries"],
    "topes_hangar": ["hangar", "Topes"],
    "skills_bin": ["hangar", "Misc", " Skillbooks"],
}

# id <-> station name list (from eve static dump)
stationids = "station.static"
# id <-> item name list (from eve static dump)
itemids = "item.static"
# invflag <-> flag description (from eve static dump)
invflags = "infvlags.static"

# What kind of stock are we monitoring? Used in page title and headline.
description = "Example"

# optional, only if you want to regenerate the item ids list
dbname = "eve-dump.db"
# what action message to display in case errors persist
error_action = "find someone to fix it"

log_level = "DEBUG"
