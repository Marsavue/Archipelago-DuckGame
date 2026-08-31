from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from rule_builder.rules import HasAll#, AtLeast
from . import data
from worlds.duckgame.options import MedalCountGoal
from math import floor

if TYPE_CHECKING:
    from .world import DuckGameWorld

def set_all_rules(world: DuckGameWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

# Should probably change these to location rules but it doesn't matter rn
def set_all_entrance_rules(world: DuckGameWorld) -> None:
    regions = list(world.get_regions())
    del regions[0]
    for r in regions:
        world.set_rule(world.get_entrance(r.name), HasAll(r.name,*data.LEVEL_LIST[r.name]))

def set_all_location_rules(world: DuckGameWorld) -> None:
    return

def set_completion_condition(world: DuckGameWorld) -> None:
    # This is the real code for after AtLeast gets implemented in Stable
    # Not well versed enough to figure this out without AtLeast/long gen times

    # Update this to do the same as the other junk (getattr)
    print(world.options.death_link)
    print(world.options.death_link_amnesty)
    medals_per_level = 0
    if world.options.use_bronze_medal:
        medals_per_level += 1
    if world.options.use_silver_medal:
        medals_per_level += 1
    if world.options.use_gold_medal:
        medals_per_level += 1
    if world.options.use_platinum_medal:
        medals_per_level += 1
    if world.options.use_developer_medal:
        medals_per_level += 1
    if world.options.medal_count_goal > MedalCountGoal(world.options.total_arcade_levels*medals_per_level):
        world.options.medal_count_goal = MedalCountGoal(world.options.total_arcade_levels*medals_per_level)
    # goal_rules = []
    # regions = list(world.get_regions())
    # del regions[0]
    # for r in regions:
    #     goal_rules.append(HasAll(r.name,*data.LEVEL_LIST[r.name]))
    # world.set_completion_rule(AtLeast(floor(world.options.medal_count_goal/medals_per_level),*goal_rules))
