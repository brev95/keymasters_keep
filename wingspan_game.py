from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class WingspanArchipelagoOptions:
    wingspan_expansions_owned: WingspanExpansionsOwned



class WingspanGame(Game):
    name = "Wingspan"
    platform = KeymastersKeepGamePlatforms.BOARD

    platforms_other = [
        KeymastersKeepGamePlatforms.PC,
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = False

    options_cls = WingspanArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Starting goals: GOALS",
                data={
                    "GOALS": (self.end_of_round_goals, 4)
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win a game of Wingspan",
                data={},
                is_time_consuming=True,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a round with 'GOAL' as your goal",
                data={
                    "GOAL": (self.end_of_round_goals, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="At the end of game, have the GOAL",
                data={
                    "GOAL": (self.game_end_points, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Collect NUMBER FOOD",
                data={
                    "NUMBER": (self.food_range, 1),
                    "FOOD": (self.food_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Achieve one additional bonus objective: BONUS",
                data={
                    "BONUS": (self.bonus_objectives, 3),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=4,
            ),
        ]

    @property
    def expansions_owned(self):
        return sorted(self.archipelago_options.wingspan_expansions_owned.values)

    @property
    def has_asia_expansion(self):
        return "Asia" in self.dlc_owned

    @property
    def has_european_expansion(self):
        return "European" in self.dlc_owned

    @property
    def has_oceania_expansion(self):
        return "Oceania" in self.dlc_owned

    @property
    def board_columns(self) -> range:
        return range(1, 6)

    @property
    def food_range(self) -> range:
        return range(3, 7)

    @property
    def bonus_range(self) -> range:
        return range(1, 7)

    @functools.cached_property
    def base_food_types(self) -> List[str]:
        return [
            "invertebrate",
            "seed",
            "fish",
            "fruit",
            "rodent",
        ]

    @functools.cached_property
    def oceania_food_types(self) -> List[str]:
        return [
            "nectar",
        ]

    @property
    def food_types(self) -> List[str]:
        food = self.base_food_types[:]
        if self.has_oceania_expansion:
            food.extend(self.oceania_food_types)
        return food

    @functools.cached_property
    def habitats(self) -> List[str]:
        return [
            "forest",
            "grassland",
            "wetland",
        ]

    @functools.cached_property
    def nest_types(self) -> List[str]:
        return [
            "bowl",
            "cavity",
            "ground",
            "platform",
            "wild"
        ]

    @property
    def end_of_round_goals(self) -> List[str]:
        return [
            f"Most birds with {nest_type} nest type with an egg" for nest_type in self.nest_types
        ] + [
            f"Most birds in {habitat}" for habitat in self.habitats
        ] + [
            f"Most eggs in {nest_type}" for nest_type in self.nest_types
        ] + [
            f"Most eggs in {habitat}" for habitat in self.habitats
        ] + [
            f"Most birds with a beak pointing {direction}" for direction in ["left", "right"]
        ] + [
            f"Most cubes on '{action}' action" for action in [
                "Play a Bird",
                "Gather Food",
                "Lay Eggs",
                "Draw Cards",
            ]
        ] + [
            "Most birds"
            "Most sets of eggs (1 in each habitat type)"
            "Most food in your personal supply",
            "Most bird cards in hand",
            "Most birds worth over 4 points",
            "Most birds with no eggs",
            "Most birds in one row",
            "Most filled columns",
            "Most birds with a brown 'when activated' power",
            "Most birds with either no power of a 'when played' power",
            "Most birds with a tucked card",
            "Most food cost on birds",
        ]

    @property
    def game_end_points(self) -> List[str]:
        return [
            "most points from birds",
            "most points from bonus cards",
            "most points from end of round goals",
            "most eggs on birds",
            "most food cached on birds",
            "most tucked cards",
        ]

    @functools.cached_property
    def bonus_objectives(self) -> List[str]:
        return [
            "Birds with colors in their names",
            "Birds with body parts in their names",
            "Birds with geography terms in their names",
            "Birds named after a person",
            "Birds with a specific type of nest",
            "Birds with at least 4 eggs laid on them",
            "Birds that have at least 1 egg laid on them",
            "Birds that can only live in one specific habitat",
            "Birds with wingspans over 65cm",
            "Birds with wingspans 30cm or less",
            "Birds worth less than 4 points",
            "Birds in your hand at end of game",
            "Sets of 4 nest types (1 of each type)",
            "Columns with a pair or trio of nest types",
            "Consecutive birds with ascending or descending wingspans",
            "Birds with completely full nests",
            "Birds with an egg limit of 2 or less",
            "Birds with a food cost of 2 or less",
            "Food remaining in your personal supply",
            "Fish and rodent tokens cached on birds",
            "Birds that allow you to score or draw more bonus cards",
        ] + [
            f"Different nest types in {habitat}" for habitat in self.habitats
        ] + [
            f"Consecutive birds in {habitat} with ascending or descending scores" for habitat in self.habitats
        ]


class WingspanExpansionsOwned(OptionSet):
    """
        Indicates which Wingspan expansions the player owns, if any.
        """
    display_name = "Wingspan Expansions Owned"
    valid_keys = [
        "Asia",
        "European",
        "Oceania",
    ]

    default = valid_keys

