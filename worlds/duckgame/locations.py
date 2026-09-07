from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items,data
from .data import low_medal_order,medal_order,level_list_keys
from worlds.duckgame.options import SilverMedal,GoldMedal,PlatinumMedal,BronzeMedal,DeveloperMedal

if TYPE_CHECKING:
    from .world import DuckGameWorld

LOCATION_NAME_TO_ID = {}

loc = 1
for l in range(len(level_list_keys)):
    for m in medal_order:
        LOCATION_NAME_TO_ID[level_list_keys[l]+" "+m+" Medal"] = loc
        loc +=1

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