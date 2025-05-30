from __future__ import annotations

import functools

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MTGArchipelagoOptions:
    pass


class MTGGame(Game):
    name = "Magic the Gathering"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.CARD,
    ]

    is_adult_only_or_unrated = False

    options_cls = MTGArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Attack with NUMBER creatures",
                data={
                    "NUMBER": (self.large_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Attack with NUMBER creatures at once",
                data={
                    "NUMBER": (self.small_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Cast NUMBER TYPE spells",
                data={
                    "NUMBER": (self.large_amount, 1),
                    "TYPE": (self.card_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Kill NUMBER of your opponent's creatures",
                data={
                    "NUMBER": (self.large_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Play NUMBER lands",
                data={
                    "NUMBER": (self.large_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Cast NUMBER COLOR_1 or COLOR_2 spells",
                data={
                    "NUMBER": (self.large_amount, 1),
                    "COLOR_1": (self.colors, 1),
                    "COLOR_2": (self.colors, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Cast your commander NUMBER times",
                data={
                    "NUMBER": (self.small_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Cast a(n) TYPE NUMBER times",
                data={
                    "TYPE": (self.common_creature_types, 1),
                    "NUMBER": (self.medium_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Cast a(n) TYPE NUMBER times",
                data={
                    "TYPE": (self.rare_creature_types, 1),
                    "NUMBER": (self.small_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Create NUMBER tokens",
                data={
                    "NUMBER": (self.large_amount, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Play NUMBER TYPE lands",
                data={
                    "NUMBER": (self.small_amount, 1),
                    "TYPE": (self.land_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win using ALT_WIN_CON",
                data={
                    "ALT_WIN_CON": (self.alternative_win_conditions, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a game via ALT_WIN_CON",
                data={
                    "ALT_WIN_CON": (self.alternative_win_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Play a game using BAD_CARDS",
                data={
                    "BAD_CARDS": (self.bad_cards, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]

    @property
    def large_amount(self) -> range:
        return range(5, 41, 5)

    @property
    def medium_amount(self) -> range:
        return range(5, 21, 5)

    @property
    def small_amount(self) -> range:
        return range(1, 6)

    @functools.cached_property
    def colors(self) -> List[str]:
        return [
            "White",
            "Blue",
            "Black",
            "Red",
            "Green",
            "Colorless",
        ]

    @functools.cached_property
    def card_types(self) -> List[str]:
        return [
            "Artifact",
            "Battle",
            "Creature",
            "Enchantment",
            "Instant",
            "Kindred",
            "Planeswalker",
            "Sorcery",
        ]

    @functools.cached_property
    def land(self) -> List[str]:
        return [
            "Land"
        ]

    def all_types(self) -> List[str]:
        return self.card_types + self.land

    @functools.cached_property
    def common_creature_types(self) -> List[str]:
        return [
            "Angel",
            "Beast",
            "Bird",
            "Cat",
            "Cleric",
            "Demon",
            "Dinosaur",
            "Dragon",
            "Druid",
            "Eldrazi",
            "Elemental",
            "Elf",
            "Goblin",
            "Human",
            "Hydra",
            "Knight",
            "Merfolk",
            "Ninja",
            "Phoenix",
            "Pirate",
            "Rogue",
            "Skeleton",
            "Shaman",
            "Sliver",
            "Snake",
            "Soldier",
            "Sphinx",
            "Spirit",
            "Vampire",
            "Warrior",
            "Wizard",
            "Zombie",
        ]

    @functools.cached_property
    def rare_creature_types(self) -> List[str]:
        return [
            "Advisor",
            "Aetherborn",
            "Alien",
            "Ally",
            "Antelope",
            "Ape",
            "Archer",
            "Archon",
            "Armadillo",
            "Army",
            "Artificer",
            "Assassin",
            "Assembly-Worker",
            "Astartes",
            "Atog",
            "Aurochs",
            "Avatar",
            "Azra",
            "Badger",
            "Balloon",
            "Barbarian",
            "Bard",
            "Basilisk",
            "Bat",
            "Bear",
            "Beaver",
            "Beeble",
            "Beholder",
            "Berserker",
            "Blinkmoth",
            "Boar",
            "Bringer",
            "Brushwagg",
            "Camarid",
            "Camel",
            "Capybara",
            "Caribou",
            "Carrier",
            "Centaur",
            "Child",
            "Chimera",
            "Citizen",
            "Clown",
            "Cockatrice",
            "Construct",
            "Coward",
            "Coyote",
            "Crab",
            "Crocodile",
            "C’tan",
            "Custodes",
            "Cyberman",
            "Cyclops",
            "Dalek",
            "Dauthi",
            "Demigod",
            "Deserter",
            "Detective",
            "Devil",
            "Djinn",
            "Doctor",
            "Dog",
            "Drake",
            "Dreadnought",
            "Drone",
            "Dryad",
            "Dwarf",
            "Efreet",
            "Egg",
            "Elder",
            "Elephant",
            "Elk",
            "Employee",
            "Eye",
            "Faerie",
            "Ferret",
            "Fish",
            "Flagbearer",
            "Fox",
            "Fractal",
            "Frog",
            "Fungus",
            "Gamer",
            "Gargoyle",
            "Germ",
            "Giant",
            "Gith",
            "Glimmer",
            "Gnoll",
            "Gnome",
            "Goat",
            "God",
            "Golem",
            "Gorgon",
            "Graveborn",
            "Gremlin",
            "Griffin",
            "Guest",
            "Hag",
            "Halfling",
            "Hamster",
            "Harpy",
            "Hellion",
            "Hippo",
            "Hippogriff",
            "Homarid",
            "Homunculus",
            "Horror",
            "Horse",
            "Hyena",
            "Illusion",
            "Imp",
            "Incarnation",
            "Inkling",
            "Inquisitor",
            "Insect",
            "Jackal",
            "Jellyfish",
            "Juggernaut",
            "Kavu",
            "Kirin",
            "Kithkin",
            "Kobold",
            "Kor",
            "Kraken",
            "Llama",
            "Lamia",
            "Lammasu",
            "Leech",
            "Leviathan",
            "Lhurgoyf",
            "Licid",
            "Lizard",
            "Manticore",
            "Masticore",
            "Mercenary",
            "Metathran",
            "Minion",
            "Minotaur",
            "Mite",
            "Mole",
            "Monger",
            "Mongoose",
            "Monk",
            "Monkey",
            "Moonfolk",
            "Mount",
            "Mouse",
            "Mutant",
            "Myr",
            "Mystic",
            "Nautilus",
            "Necron",
            "Nephilim",
            "Nightmare",
            "Nightstalker",
            "Noble",
            "Noggle",
            "Nomad",
            "Nymph",
            "Octopus",
            "Ogre",
            "Ooze",
            "Orb",
            "Orc",
            "Orgg",
            "Otter",
            "Ouphe",
            "Ox",
            "Oyster",
            "Pangolin",
            "Peasant",
            "Pegasus",
            "Pentavite",
            "Performer",
            "Pest",
            "Phelddagrif",
            "Phyrexian",
            "Pilot",
            "Pincher",
            "Plant",
            "Porcupine",
            "Possum",
            "Praetor",
            "Primarch",
            "Prism",
            "Processor",
            "Rabbit",
            "Raccoon",
            "Ranger",
            "Rat",
            "Rebel",
            "Reflection",
            "Rhino",
            "Rigger",
            "Robot",
            "Sable",
            "Salamander",
            "Samurai",
            "Sand",
            "Saproling",
            "Satyr",
            "Scarecrow",
            "Scientist",
            "Scion",
            "Scorpion",
            "Scout",
            "Sculpture",
            "Seal",
            "Serf",
            "Serpent",
            "Servo",
            "Shade",
            "Shapeshifter",
            "Shark",
            "Sheep",
            "Siren",
            "Skunk",
            "Slith",
            "Sloth",
            "Slug",
            "Snail",
            "Soltari",
            "Spawn",
            "Specter",
            "Spellshaper",
            "Spider",
            "Spike",
            "Splinter",
            "Sponge",
            "Squid",
            "Squirrel",
            "Starfish",
            "Surrakar",
            "Survivor",
            "Synth",
            "Tentacle",
            "Tetravite",
            "Thalakos",
            "Thopter",
            "Thrull",
            "Tiefling",
            "Toy",
            "Treefolk",
            "Trilobite",
            "Triskelavite",
            "Troll",
            "Turtle",
            "Tyranid",
            "Unicorn",
            "Varmint",
            "Vedalken",
            "Volver",
            "Wall",
            "Walrus",
            "Warlock",
            "Weasel",
            "Weird",
            "Werewolf",
            "Whale",
            "Wolf",
            "Wolverine",
            "Wombat",
            "Worm",
            "Wraith",
            "Wurm",
            "Yeti",
            "Zubera",
        ]

    @property
    def creature_types(self) -> List[str]:
        return self.common_creature_types + self.rare_creature_types

    @functools.cached_property
    def artifact_types(self) -> List[str]:
        return [
            "Blood",
            "Clue",
            "Equipment",
            "Food",
            "Gold",
            "Incubator",
            "Map",
            "Powerstone",
            "Treasure",
            "Vehicle",
        ]

    @functools.cached_property
    def enchantment_types(self) -> List[str]:
        return [
            "Aura",
            "Background",
            "Cartouche",
            "Case",
            "Class",
            "Curse",
            "Role",
            "Room",
            "Rune",
            "Saga",
            "Shrine",
        ]

    @functools.cached_property
    def basic_land_types(self) -> List[str]:
        return [
            "Plains",
            "Island",
            "Swamp",
            "Mountain",
            "Forest",
        ]

    @functools.cached_property
    def land_types(self) -> List[str]:
        return [
            "Cave",
            "Desert",
            "Gate",
            "Lair",
            "Locus",
            "Mine",
            "Power-Plant",
            "Sphere",
            "Tower",
            "Urza's",
        ]

    @property
    def all_land_types(self) -> List[str]:
        return self.basic_land_types + self.land_types

    @property
    def all_sub_types(self) -> List[str]:
        return self.creature_types + self.artifact_types + self.enchantment_types

    @functools.cached_property
    def alternative_win_types(self) -> List[str]:
        return [
            "Life Loss",
            "Mill",
            "Poison",
            "Commander Damage",
        ]

    @functools.cached_property
    def alternative_win_cards(self) -> List[str]:
        return [
            "Approach of the Second Sun",
            "Azor's Elocutors",
            "Barren Glory",
            "Battle of Wits",
            "Biovisionary",
            "Call the Spirit Dragons",
            "Central Elevator // Promising Stairs",
            "Chance Encounter",
            "Coalition Victory",
            "Darksteel Reactor",
            "Epic Struggle",
            "Felidar Sovereign",
            "Gallifrey Stands",
            "Halo Fountain",
            "Happily Ever After",
            "Hedron Alignment",
            "Helix Pinnacle",
            "Hellkite Tyrant",
            "Jace, Wielder of Mysteries",
            "Laboratory Maniac",
            "Liliana's Contract",
            "Luck Bobblehead",
            "Mayael's Aria",
            "Maze's End",
            "Mechanized Production",
            "Mortal Combat",
            "Near-Death Experience",
            "Ramses, Assassin Lord",
            "Revel in Riches",
            "Simic Ascendancy",
            "Test of Endurance",
            "Thassa's Oracle",
            "Triskaidekaphile",
            "Twenty-Toed Toad",
            "Zenos yae Galvus // Shinryu, Transcendent Rival",
        ]

    @functools.cached_property
    def acorn_win_conditions(self) -> List[str]:
        return [
            "As Luck Would Have It",
            "Form of the Approach of the Second Sun",
            "Now I Know My ABC's",
            "The Cheese Stands Alone",
        ]

    @property
    def alternative_win_conditions(self) -> List[str]:
        return self.alternative_win_types + self.alternative_win_cards

    @functools.cached_property
    def bad_cards(self) -> List[str]:
        return [
            "Alabaster Leech",
            "Apocalypse Chime",
            "Bargain",
            "Blood Funnel",
            "Break Open",
            "Great Wall",
            "Juju Bubble",
            "Mudhole",
            "Obelisk of Undoing",
            "One with Nothing",
            "Rakalite",
            "Razor Boomerang",
            "Razor Pendulum",
            "Sorrow's Path",
            "Wood Elemental",
            "Zephyr Spirit",
        ]
