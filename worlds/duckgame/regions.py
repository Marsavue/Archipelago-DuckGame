from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region
from . import data

if TYPE_CHECKING:
    from .world import DuckGameWorld

def create_and_connect_regions(world: DuckGameWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DuckGameWorld) -> None:
    main = Region("main", world.player, world.multiworld)
    regions = [main]
    temp_regions = dict(data.LEVEL_LIST)
    for r in range(world.options.total_arcade_levels):
        rand_region = world.random.randint(0, len(temp_regions.keys())-1)
        regions.append(Region(list(temp_regions.keys())[rand_region], world.player, world.multiworld))
        del temp_regions[list(temp_regions.keys())[rand_region]]
    world.multiworld.regions += regions

def connect_regions(world: DuckGameWorld) -> None:
    main = world.get_region("main")
    regions = list(world.get_regions())
    del regions[0]
    for r in regions:
        main.connect(world.get_region(r.name), r.name)