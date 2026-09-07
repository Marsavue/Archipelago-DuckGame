from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from rule_builder.rules import HasAll,NestedRule#, AtLeast
from . import data
from .data import medal_order
from worlds.duckgame.options import MedalCountGoal
from math import floor

if TYPE_CHECKING:
    from .world import DuckGameWorld

def set_all_rules(world: DuckGameWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: DuckGameWorld) -> None:
    regions = list(world.get_regions())
    del regions[0]
    for r in regions:
        world.set_rule(world.get_entrance(r.name), HasAll(r.name))

def set_all_location_rules(world: DuckGameWorld) -> None:
    regions = list(world.get_regions())
    del regions[0]
    pos = 1
    for m in range(len(medal_order)): 
        if getattr(world.options,"use_"+medal_order[m].lower()+"_medal"):
            for r in regions:
                items = data.LEVEL_LIST[r.name]
                reqs = []
                for i in range(pos):
                    reqs = [*reqs, *items[i]]
                world.set_rule(world.get_location(r.name+" "+medal_order[m]+" Medal"), HasAll(r.name,*reqs))
        pos+=1

def set_completion_condition(world: DuckGameWorld) -> None:
    # Combine location rules and completion condition for slightly faster gen

    regions = list(world.get_regions())
    del regions[0]
    goal_rules = []
    medals_per_level = 0
    pos = 1
    for m in range(len(medal_order)): 
        if getattr(world.options,"use_"+medal_order[m].lower()+"_medal"):
            medals_per_level+=1
            for r in regions:
                items = data.LEVEL_LIST[r.name]
                reqs = []
                for i in range(pos):
                    reqs = [*reqs, *items[i]]
                goal_rules.append(HasAll(r.name,*reqs))
        pos+=1
    if world.options.medal_count_goal > MedalCountGoal(world.options.total_arcade_levels*medals_per_level):
        world.options.medal_count_goal = MedalCountGoal(world.options.total_arcade_levels*medals_per_level)
    world.set_completion_rule(MyAtLeast(int(world.options.medal_count_goal),*goal_rules))


class MyAtLeast(NestedRule["DuckGameWorld"], game="DuckGame"):
    count: int

    def __init__(
        self,
        count: int,
        *children: Rule["DuckGameWorld"],
        options: Iterable[OptionFilter] = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(*children, options=options, filtered_resolution=filtered_resolution)
        self.count = count

    
    def _instantiate(self, world: "DuckGameWorld") -> Rule.Resolved:
        count = self.count
        if count == 0:
            return True_().resolve(world)

        children_to_process = [c.resolve(world) for c in self.children]
        return MyAtLeast.from_resolved(count, world, children_to_process)

    @classmethod
    def from_resolved(cls, count: int, world: "DuckGameWorld", children_to_process: list[Rule.Resolved]) -> Rule.Resolved:
        clauses: list[Rule.Resolved] = []

        while children_to_process:
            child = children_to_process.pop(0)
            if child.always_true:
                if count == 1:
                    return child
                count -= 1
                continue
            if child.always_false:
                # falses can be ignored
                continue

            clauses.append(child)

        if len(clauses) < count:
            return False_().resolve(world)
        if count == 1:
            # Switch to Or which has more optimized handling
            return Or.from_resolved(world, clauses)
        if count == len(clauses):
            # Switch to And which has more optimized handling
            return And.from_resolved(world, clauses)
        return MyAtLeast.Resolved(
            tuple(clauses),
            count=count,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )
    
    class Resolved(NestedRule.Resolved):
        count: int

        
        def _evaluate(self, state: CollectionState) -> bool:
            count = self.count
            for rule in self.children:
                if rule(state):
                    if count == 1:
                        return True
                    count -= 1
            return False

        
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            messages: list[JSONMessagePart] = []
            if state is None:
                messages = [
                    {"type": "text", "text": "At least "},
                    {"type": "color", "color": "cyan", "text": str(self.count)},
                    {"type": "text", "text": " of ("},
                ]
            else:
                satisfied_count = sum(1 if child(state) else 0 for child in self.children)
                messages = [
                    {"type": "text", "text": "At least "},
                    {"type": "color", "color": "cyan", "text": f"{satisfied_count}/{self.count}"},
                    {"type": "text", "text": " of ("},
                ]
            for i, child in enumerate(self.children):
                if i > 0:
                    messages.append({"type": "text", "text": ", "})
                messages.extend(child.explain_json(state))
            messages.append({"type": "text", "text": ")"})
            return messages

        
        def explain_str(self, state: CollectionState | None = None) -> str:
            clauses = ", ".join([c.explain_str(state) for c in self.children])
            if state is None:
                return f"At least {self.count} of ({clauses})"
            satisfied_count = sum(1 if child(state) else 0 for child in self.children)
            return f"At least {satisfied_count}/{self.count} of ({clauses})"

        
        def __str__(self) -> str:
            clauses = ", ".join([str(c) for c in self.children])
            return f"At least {self.count} of ({clauses})"