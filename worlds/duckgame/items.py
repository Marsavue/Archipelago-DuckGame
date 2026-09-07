from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from . import data
from .data import medal_order,setting_filler_list_keys

if TYPE_CHECKING:
    from .world import DuckGameWorld

ITEM_NAME_TO_ID = {}
DEFAULT_ITEM_CLASSIFICATIONS = {}

count = 1
for level in data.LEVEL_LIST.keys():
    ITEM_NAME_TO_ID[level] = count
    DEFAULT_ITEM_CLASSIFICATIONS[level] = ItemClassification.progression
    count += 1

for level_item in data.ITEM_LIST.keys():
    ITEM_NAME_TO_ID[level_item] = count
    DEFAULT_ITEM_CLASSIFICATIONS[level_item] = data.ITEM_LIST[level_item]
    count += 1

for filler_item in data.FILLER_LIST.keys():
    ITEM_NAME_TO_ID[filler_item] = count
    DEFAULT_ITEM_CLASSIFICATIONS[filler_item] = data.FILLER_LIST[filler_item]
    count += 1

class DuckGameItem(Item):
    game = "DuckGame"

def get_random_filler_item_name(world: DuckGameWorld) -> str:
    if world.random.randint(0,99) < world.options.trap_percent:
        max_filler_weight=0
        for f in setting_filler_list_keys:
            max_filler_weight+=getattr(world.options,f+"_weight")
        rand_trap = world.random.randint(0,max_filler_weight-1)
        current_weight = 0
        for f in setting_filler_list_keys:
            current_weight+=getattr(world.options,f+"_weight")
            if rand_trap<current_weight:
                return data.SETTING_FILLER_LIST[f]
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
    for m in data.LEVEL_LIST[regions[starting_level]]:
        for i in m:
            world.push_precollected(world.create_item(i))
            del temp_items[i]
    del regions[starting_level]
    itempool: list[Item] = []
    for l in range(len(regions)):
        itempool.append(world.create_item(regions[l]))
        for m in data.LEVEL_LIST[regions[l]]:
            for i in m:
                if i in temp_items.keys():
                    itempool.append(world.create_item(i))
                    del temp_items[i]
    for t in range(len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)):
        if len(temp_items.keys())>0:
            pos = world.random.randint(0,len(temp_items.keys())-1)
            item = list(temp_items.keys())[pos]
            if temp_items[item] == ItemClassification.progression:
                DEFAULT_ITEM_CLASSIFICATIONS[item] = ItemClassification.useful
            itempool.append(world.create_item(item))
            del temp_items[item]
    
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
