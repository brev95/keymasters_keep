from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DigseumArchipelagoOptions:
    pass


class DigseumGame(Game):
    name = "Digseum"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = []

    is_adult_only_or_unrated = False

    options_cls = DigseumArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Find a(n) RELIC",
                data={
                    "RELIC": (self.relics, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Find a(n) RELIC NUMBER times",
                data={
                    "RELIC": (self.relics, 1),
                    "NUMBER": (self.small_number, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL with RELIC",
                data={
                    "LEVEL": (self.small_number, 1),
                    "RELIC": (self.relics, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL with RELIC",
                data={
                    "LEVEL": (self.number, 1),
                    "RELIC": (self.relics, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL with RELIC",
                data={
                    "LEVEL": (self.large_number, 1),
                    "RELIC": (self.relics, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Excavate ZONE NUMBER times",
                data={
                    "ZONE": (self.zones, 1),
                    "NUMBER": (self.small_number, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL in ZONE",
                data={
                    "LEVEL": (self.small_number, 1),
                    "ZONE": (self.zones, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL in ZONE",
                data={
                    "LEVEL": (self.number, 1),
                    "ZONE": (self.zones, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL in ZONE",
                data={
                    "LEVEL": (self.large_number, 1),
                    "ZONE": (self.zones, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Upgrade UPGRADE once",
                data={
                    "UPGRADE": (self.upgrades, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Unlock ABILITY in the Dream Tree",
                data={
                    "ABILITY": (self.ability, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Prestige NUMBER times",
                data={
                    "NUMBER": (self.prestige, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Collect NUMBER dream fragments",
                data={
                    "NUMBER": (self.small_number, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Collect NUMBER dream fragments",
                data={
                    "NUMBER": (self.number, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Collect NUMBER dream fragments",
                data={
                    "NUMBER": (self.large_number, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
        ]

    @staticmethod
    def relics() -> List[str]:
        return [
            "Ancient Tablet",
            "Angel Teardrop",
            "Bottled Fairy",
            "Ceremonial Mask",
            "Cosmic Staff",
            "Cosmic Sword",
            "Crescent Charm",
            "Crown of Thorns",
            "Decorated Spear",
            "Doomsday Hourglass",
            "Dragon Fang",
            "Dragon Scale",
            "Ember Essence",
            "Eternal Lantern",
            "Fairy Wings",
            "Fleeting Flute",
            "Giant Feather",
            "Glistening Ruby",
            "Goddess Crown",
            "Golden Monocle",
            "Heavy Coin",
            "Huge Banana",
            "Ice Mirror",
            "Iridescent Flower",
            "Key To Heaven",
            "Lightning in a Bottle",
            "Lil Cloudy",
            "Monster Skull",
            "Mr. Fun Guy",
            "Mummified Body",
            "Obsidian Sword",
            "Petrified Snake",
            "Petrified Squirrel",
            "Pharaoh Mask",
            "Rainbow Cat",
            "Rainbow Feather",
            "Runic Scroll",
            "Sacrificial Dagger",
            "Scarab Shell",
            "Snowcaller Horn",
            "Sparkling Emerald",
            "Spiritual Totem",
            "Staff of the Shaman",
            "Star Piece",
            "Stone Idol",
            "Tall Mask",
            "Tempest Staff",
            "Unbreaking Cobweb",
            "Unmelting Icicle",
            "World Tree Acorn",
            "Yeti-Fur Hood",
        ]

    @staticmethod
    def zones() -> List[str]:
        return [
            "Astral Plane",
            "Brink of Reality",
            "Cloudtop Castle",
            "Echo Cave",
            "Forest of Secrets",
            "Jungle Temple",
            "Lost Pyramids",
            "Mount Stone",
            "Mucky Marsh",
            "Mud Pit",
            "Mushroom Grotto",
            "Rainbow Bridge",
            "Snowy Summit",
            "Volcanic Wasteland",
        ]

    @staticmethod
    def upgrades() -> List[str]:
        return [
            "Marketing",
            "Pickaxe Area",
            "Pickaxe Strength",
            "Stamina",
        ]

    @staticmethod
    def ability() -> List[str]:
        return [
            "Analyzer",
            "Ascended Relics",
            "Astrology",
            "Collapsing Dreams",
            "Daydreaming",
            "Deep Sleep",
            "Dream Fragmentation",
            "Dream Pocket",
            "Dreaming of Relics",
            "Endless Dreams",
            "Familiarity",
            "Fan Club",
            "From the Ashes",
            "Ghost Digger",
            "Godlike Relics",
            "Going Viral",
            "Gold Pocket",
            "Gone Caving",
            "Ice Cold",
            "Inspector",
            "Jungling",
            "Lost Riches",
            "Magic Mushrooms",
            "Muck Money",
            "Muddy Treasures",
            "Mystic Radar",
            "Mystic Scope",
            "Mystic Spirit",
            "One-Time",
            "Parallel Dreams",
            "Popularity",
            "Prior Expertise",
            "Prior Knowledge",
            "Prior Mastery",
            "Resilience",
            "Retain Knowledge",
            "Rock Solid",
            "Secret Sauce",
            "Semblance",
            "Spirit Pickaxe",
            "Third Eye",
            "Unchanged",
            "Understander",
            "Unyielding",
            "Valuable",
            "Where Am I?"
            "World Wonders",
        ]

    @staticmethod
    def prestige() -> range:
        return range(1, 5)

    @staticmethod
    def small_number() -> range:
        return range(1, 21, 5)

    @staticmethod
    def number() -> range:
        return range(100, 1001, 10)

    @staticmethod
    def large_number() -> range:
        return range(1000, 5001, 100)
