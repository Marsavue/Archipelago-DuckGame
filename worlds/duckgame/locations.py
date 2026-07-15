from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items,data

if TYPE_CHECKING:
    from .world import DuckGameWorld

LOCATION_NAME_TO_ID = {}

for l in range(len(list(data.LEVEL_LIST.keys()))):
    for m in range(2):
        medal = ""
        # if m == 0:
        #     medal = " Bronze"
        if m == 0:
            medal = " Silver"
        elif m == 1:
            medal = " Gold"
        LOCATION_NAME_TO_ID[list(data.LEVEL_LIST.keys())[l]+medal] = l*10+m+1

class DuckGameLocation(Location):
    game = "DuckGame"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DuckGameWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: DuckGameWorld) -> None:
    loc = 0
    for r in range(len(data.LEVEL_LIST.keys())):
        region = world.get_region(list(data.LEVEL_LIST.keys())[r])
        locations = []
        for l in range(2):
            locations.append(list(LOCATION_NAME_TO_ID.keys())[loc])
            loc += 1
        region.add_locations(get_location_names_with_ids(locations), DuckGameLocation)

def create_events(world: DuckGameWorld) -> None:
    #TODO NEED TO CREATE VICTORY EVENT
    # loc = world.get_region("5a3ee55f-4149-4f2a-a222-95d1d52c8b8b")
    # loc.add_event(
    #     "loc defeated", "Victory", location_type=DuckGameLocation, item_type=items.DuckGameItem
    # )
    return