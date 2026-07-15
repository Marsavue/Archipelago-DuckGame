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
    for r in range(len(data.LEVEL_LIST.keys())):
        regions.append(Region(list(data.LEVEL_LIST.keys())[r], world.player, world.multiworld))
    world.multiworld.regions += regions


def connect_regions(world: DuckGameWorld) -> None:
    main = world.get_region("main")
    for r in range(len(data.LEVEL_LIST.keys())):
        main.connect(world.get_region(list(data.LEVEL_LIST.keys())[r]), list(data.LEVEL_LIST.keys())[r])