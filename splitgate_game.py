from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class SplitgateArchipelagoOptions:
    pass


class SplitgateGame(Game):
    name = "Splitgate"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
    ]

    is_adult_only_or_unrated = False

    options_cls = SplitgateArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win a game",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Play a game",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a game of GAME",
                data={
                    "GAME": (self.game_modes, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Play a game of GAME",
                data={
                    "GAME": (self.game_modes, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Get KILLS kills with WEAPON",
                data={
                    "KILLS": (self.number, 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Get KILLS kills with WEAPON",
                data={
                    "KILLS": (self.large_number, 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Get KILLS melee kills",
                data={
                    "KILLS": (self.small_number, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Get NUMBER headshots",
                data={
                    "NUMBER": (self.number, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Get NUMBER headshots",
                data={
                    "NUMBER": (self.large_number, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Play a game on MAP",
                data={
                    "MAP": (self.maps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete a race on MAP on DIFFICULTY difficulty",
                data={
                    "MAP": (self.maps, 1),
                    "DIFFICULTY": (self.difficulty, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Score highest on your team in a match",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Get a killing spree",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
        ]

    @staticmethod
    def game_modes() -> List[str]:
        return [
            "Team Deathmatch",
            "Team Fiesta",
            "Sniper Frenzy",
            "Team Objective",
            "No Portals",
            "Team Rumble",
            "SWAT",
            "Search and Survive",
            "FFA Brawl",
            "Ranked",
        ]

    @staticmethod
    def weapons() -> List[str]:
        return [
            "Assault Rifle",
            "BFB",
            "Battle Rifle",
            "Carbine",
            "Pistol",
            "Plasma Rifle",
            "Railgun",
            "Rocket Launcher",
            "Shotgun",
            "SMG",
            "Sniper",
            "Splitball",
        ]

    @staticmethod
    def maps() -> List[str]:
        return [
            "Abyss",
            "Atlantis",
            "Club Silo",
            "Crag",
            "Foregone Destruction",
            "Helix",
            "Highwind",
            "Impact",
            "Karman Station",
            "Lavawell",
            "Oasis",
            "Olympus",
            "Pantheon",
            "Stadium",
        ]

    @staticmethod
    def difficulty() -> List[str]:
        return [
            "Easy",
            "Medium",
            "Hard",
        ]

    @staticmethod
    def small_number() -> range:
        return range(1, 6)

    @staticmethod
    def number() -> range:
        return range(1, 11)

    @staticmethod
    def large_number() -> range:
        return range(1, 31)
