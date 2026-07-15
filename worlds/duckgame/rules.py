from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from rule_builder.rules import HasAll
from . import data

if TYPE_CHECKING:
    from .world import DuckGameWorld

def set_all_rules(world: DuckGameWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

# Should probably change these to location rules but it doesn't matter
def set_all_entrance_rules(world: DuckGameWorld) -> None:
    for e in range(len(data.LEVEL_LIST.keys())):
        world.set_rule(world.get_entrance(list(data.LEVEL_LIST.keys())[e]), HasAll(list(data.LEVEL_LIST.keys())[e],*data.LEVEL_LIST[list(data.LEVEL_LIST.keys())[e]]))

def set_all_location_rules(world: DuckGameWorld) -> None:
    return


def set_completion_condition(world: DuckGameWorld) -> None:
    #TODO NEED TO CREATE VICTORY EVENT

    # Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    # You can just set a completion condition directly like any other condition, referencing items the player receives:
    # world.multiworld.completion_condition[world.player] = lambda state: state.has_all(("Sword", "Shield"), world.player)

    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    # world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    return
