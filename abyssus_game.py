from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class AbyssusArchipelagoOptions:
    pass


class AbyssusGame(Game):
    name = "Abyssus"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = []

    is_adult_only_or_unrated = False

    options_cls = AbyssusArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Play a depth using WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete a depth using WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Play a depth using ABILITY",
                data={
                    "ABILITY": (self.abilities, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete a depth using ABILITY",
                data={
                    "ABILITY": (self.abilities, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Play a depth using WEAPON and ABILITY",
                data={
                    "WEAPON": (self.weapons, 1),
                    "ABILITY": (self.abilities, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete a depth using WEAPON and ABILITY",
                data={
                    "WEAPON": (self.weapons, 1),
                    "ABILITY": (self.abilities, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Unlock UPGRADE on the soul wheel",
                data={
                    "UPGRADE": (self.upgrades, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Max UPGRADE on the soul wheel",
                data={
                    "UPGRADE": (self.upgrades, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Play a depth using CANISTERS or more brine canisters",
                data={
                    "CANISTERS": (self.brine_canisters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Play a depth using CANISTERS or more brine canisters",
                data={
                    "CANISTERS": (self.max_brine_canisters, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Unlock WEAPON",
                data={
                    "WEAPON": (self.locked_weapons, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Unlock ABILITY",
                data={
                    "ABILITY": (self.locked_abilities, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Unlock a mod for the WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Unlock a charm",
                data={},
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1)
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def locked_weapons() -> List[str]:
        return [
            "Brine Revolver",
            "Combat Bow",
            "Disc Thrower",
            "Fish Deity",
            "Plasma Launcher",
            "Shotgun",
            "Tesla Gun",
        ]

    def weapons(self) -> List[str]:
        return self.locked_weapons() + [
            "Engine Rifle",
        ]

    @staticmethod
    def locked_abilities() -> List[str]:
        return [
            "Anchor",
            "Ancient Core",
            "Brine Field",
            "Turret",
        ]

    def abilities(self) -> List[str]:
        return self.locked_abilities() + [
            "Frag Grenade",
        ]

    @staticmethod
    def upgrades() -> List[str]:
        tier_one = [
            "Enhanced Weapons",
            "Upgraded Inventions",
            "Bountiful Bottles",
            "Picky Worship",
            "Bartering",
        ]
        tier_two = [
            "Abyssal Stamina",
            "Ability Abundance",
            "Temple's Rest",
            "Starting Funds",
            "Ancient Forge",
        ]
        tier_three = [
            "Keen Vision",
            "Magazine Madness",
            "Gardens' Rest",
            "Ascended Blessings",
            "Gambler",
        ]
        tier_four = [
            "Ability Abundance II",
            "Bountiful Bottles II",
            "Abundance",
        ]
        tier_five = [
            "Rapid Fire",
            "Second Wind",
            "Sanctuary's Rest",
            "Beginner's Charm",
            "Timely Reward",
        ]
        tier_six = [
            "Execution",
            "Finer Charms",
            "Picky Worship II",
        ]
        tier_seven = [
            "Charm Power",
        ]
        return tier_one + tier_two + tier_three + tier_four + tier_five + tier_six + tier_seven

    # TODO: complete bosses once wiki is updated
    @staticmethod
    def bosses() -> List[str]:
        return [
            "the Overseer",
            "Miphina, the Golemancer",
            "Gardens Elite",
            "Gardens Boss",
            "Sanctuary Elite",
            "Sanctuary Boss",
            "The First Herald",
            "The Second Herald",
            "The Third Herald",
            "Final Boss",
        ]

    @staticmethod
    def brine_canisters() -> range:
        return range(1, 5)

    @staticmethod
    def max_brine_canisters() -> range:
        return range(1, 35)
