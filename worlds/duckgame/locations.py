from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items,data
from worlds.duckgame.options import SilverMedal,GoldMedal,PlatinumMedal,BronzeMedal,DeveloperMedal

if TYPE_CHECKING:
    from .world import DuckGameWorld

LOCATION_NAME_TO_ID = {}
low_medal_order = ["Silver","Gold","Platinum","Bronze","Developer"]

# Update this to do the same as the other junk (getattr)
# What are you saying dawg, you can just do a loop it'll take 5 seconds
loc = 1
for l in range(len(list(data.LEVEL_LIST.keys()))):
    LOCATION_NAME_TO_ID[list(data.LEVEL_LIST.keys())[l]+" Bronze Medal"] = loc
    LOCATION_NAME_TO_ID[list(data.LEVEL_LIST.keys())[l]+" Silver Medal"] = loc+1
    LOCATION_NAME_TO_ID[list(data.LEVEL_LIST.keys())[l]+" Gold Medal"] = loc+2
    LOCATION_NAME_TO_ID[list(data.LEVEL_LIST.keys())[l]+" Platinum Medal"] = loc+3
    LOCATION_NAME_TO_ID[list(data.LEVEL_LIST.keys())[l]+" Developer Medal"] = loc+4
    loc += 5

class DuckGameLocation(Location):
    game = "DuckGame"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DuckGameWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: DuckGameWorld) -> None:
    medals = []
    for m in low_medal_order:
        if getattr(world.options,"use_"+m.lower()+"_medal"):
            medals.append(m)
    for m in low_medal_order:
        if len(medals)<world.options.min_medal_types:
            if m not in medals:
                medals.append(m)
                setattr(world.options,"use_"+m.lower()+"_medal",globals()[m+"Medal"](True))
    regions = list(world.get_regions())
    del regions[0]
    for r in regions:
        region = world.get_region(r.name)
        locations = []
        for m in medals:
            locations.append(r.name+" "+m+" Medal")
        region.add_locations(get_location_names_with_ids(locations), DuckGameLocation)

def create_events(world: DuckGameWorld) -> None:
    return