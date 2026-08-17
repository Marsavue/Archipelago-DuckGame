from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from . import data

if TYPE_CHECKING:
    from .world import DuckGameWorld

ITEM_NAME_TO_ID = {}
DEFAULT_ITEM_CLASSIFICATIONS = {}

count = 1
for l in range(len(data.LEVEL_LIST.keys())):
    ITEM_NAME_TO_ID[list(data.LEVEL_LIST.keys())[l]] = count
    DEFAULT_ITEM_CLASSIFICATIONS[list(data.LEVEL_LIST.keys())[l]] = ItemClassification.progression
    count += 1
for levelitem in data.ITEM_LIST.keys():
    ITEM_NAME_TO_ID[levelitem] = count
    DEFAULT_ITEM_CLASSIFICATIONS[levelitem] = data.ITEM_LIST[levelitem]
    count += 1

class DuckGameItem(Item):
    game = "DuckGame"

def get_random_filler_item_name(world: DuckGameWorld) -> str:
    return "Filler"


def create_item_with_correct_classification(world: DuckGameWorld, name: str) -> DuckGameItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return DuckGameItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: DuckGameWorld) -> None:
    regions = list(world.get_regions())
    del regions[0]
    for r in range(len(regions)):
        regions[r] = regions[r].name
    starting_level = world.random.randint(0, len(regions)-1)
    world.push_precollected(world.create_item(regions[starting_level]))
    temp_items:dict = dict(data.ITEM_LIST)
    for i in data.LEVEL_LIST[regions[starting_level]]:
        world.push_precollected(world.create_item(i))
        del temp_items[i]
    del regions[starting_level]
    itempool: list[Item] = []
    for l in range(len(regions)):
        itempool.append(world.create_item(regions[l]))
        for i in data.LEVEL_LIST[regions[l]]:
            if i in temp_items.keys():
                itempool.append(world.create_item(i))
                del temp_items[i]
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
