from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class PokemonGoArchipelagoOptions:
    pass


class PokemonGoGame(Game):
    name = "Pokemon Go"
    platform = KeymastersKeepGamePlatforms.AND

    platforms_other = [
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = PokemonGoArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Catch NUMBER TYPE",
                data={
                    "NUMBER": (self.catches, 1),
                    "TYPE": (self.pokemon_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Use NUMBER berries to catch Pokémon",
                data={
                    "NUMBER": (self.catches, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Spin NUMBER PokéStops",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Catch NUMBER different species of Pokémon",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Hatch NUMBER eggs",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Make NUMBER THROW_TYPE throws",
                data={
                    "NUMBER": (self.low_range, 1),
                    "THROW_TYPE": (self.throw_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a raid",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Participate in a raid",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Explore NUMBER km",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Evolve a Pokémon",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Power up Pokémon NUMBER times",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Earn NUMBER Candies walking with your buddy",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat NUMBER Team Rocket Grunts",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Send NUMBER gifts to friends",
                data={
                    "NUMBER": (self.low_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Trade a Pokémon",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]

    @property
    def catches(self) -> range:
        return range(5, 31, 5)
    
    @property
    def low_range(self) -> range:
        return range(1, 6)

    @functools.cached_property
    def pokemon_types(self) -> List[str]:
        return [
            "Bug",
            "Dark",
            "Dragon",
            "Electric",
            "Fairy",
            "Fighting",
            "Fire",
            "Flying",
            "Ghost",
            "Grass",
            "Ground",
            "Ice",
            "Normal",
            "Poison",
            "Psychic",
            "Rock",
            "Steel",
            "Water",
        ]

    @functools.cached_property
    def throw_types(self) -> List[str]:
        return [
            "Nice",
            "Great",
            "Excellent",
            "Curveball",
        ]

