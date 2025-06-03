from __future__ import annotations

from typing import List

from dataclasses import dataclass
from random import randint

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MelvorIdleArchipelagoOptions:
    melvor_idle_dlc_owned: MelvorIdleDLCOwned


class MelvorIdleGame(Game):
    name = "Melvor Idle"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = MelvorIdleArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Create a new save file with the game mode MODE",
                data={
                    "MODE": (self.game_modes, 1),
                },
            )
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Reach level LEVEL in SKILL",
                data={
                    "SKILL": (self.base_skills, 1),
                    "LEVEL": (self.early_skill_levels, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL in SKILL",
                data={
                    "SKILL": (self.skills, 1),
                    "LEVEL": (self.late_skill_levels, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            
            GameObjectiveTemplate(
                label="Reach level LEVEL in SKILL",
                data={
                    "SKILL": (self.into_the_abyss_skills, 1),
                    "LEVEL": (self.early_abyssal_levels, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Reach level LEVEL in SKILL",
                data={
                    "SKILL": (self.into_the_abyss_skills, 1),
                    "LEVEL": (self.late_abyssal_levels, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Kill NUMBER MONSTER",
                data={
                    "NUMBER": (self.random_range, 1),
                    "MONSTER": (self.monsters, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Kill NUMBER BOSS",
                data={
                    "NUMBER": (self.random_range, 1),
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Reach mastery level in MASTERY in an item of your choice in SKILL",
                data={
                    "MASTERY": (self.mastery, 1),
                    "SKILL": (self.non_combat_skills, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete DUNGEON NUMBER times",
                data={
                    "DUNGEON": (self.dungeons, 1),
                    "NUMBER": (self.low_numbers, 1)
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete EVENT once",
                data={
                    "Event": (self.events, 1)
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    @property
    def dlc_owned(self) -> List[str]:
        return sorted(self.archipelago_options.melvor_idle_dlc_owned.value)

    @property
    def has_dlc_throne_of_the_herald(self) -> bool:
        return "Throne of the Herald" in self.dlc_owned

    @property
    def has_dlc_atlas_of_discovery(self) -> bool:
        return "Atlas of Discovery" in self.dlc_owned

    @property
    def has_dlc_into_the_abyss(self) -> bool:
        return "Into the Abyss" in self.dlc_owned

    @staticmethod
    def game_modes() -> List[str]:
        return [
            "Normal",
            "Hardcore",
            "Adventure",
            "Ancient Relics",
        ]

    @staticmethod
    def base_game_levels() -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 99]

    @staticmethod
    def dlc_levels() -> List[int]:
        return [110, 120]

    def levels(self) -> List[int]:
        if self.has_dlc_throne_of_the_herald:
            return self.base_game_levels() + self.dlc_levels()
        return self.base_game_levels()

    def early_skill_levels(self) -> List[int]:
        return self.levels()[:4]

    def late_skill_levels(self) -> List[int]:
        return self.levels()[4:]

    @staticmethod
    def abyssal_levels() -> List[int]:
        return [10, 20, 30, 40, 50, 60]

    def early_abyssal_levels(self) -> List[int]:
        return self.abyssal_levels()[:2]

    def late_abyssal_levels(self) -> List[int]:
        return self.abyssal_levels()[2:]

    @staticmethod
    def low_numbers() -> range:
        return range(5, 101, 5)

    @staticmethod
    def medium_numbers() -> range:
        return range(50, 301, 10)

    @staticmethod
    def high_numbers() -> range:
        return range(250, 1001, 50)

    def random_range(self) -> range:
        rand = randint(0, 100)
        if rand > 75:
            return self.low_numbers()
        elif rand > 50:
            return self.medium_numbers()
        return self.high_numbers()

    @staticmethod
    def mastery() -> range:
        return range(2, 100)

    @staticmethod
    def base_combat_skills() -> List[str]:
        return [
            "Attack",
            "Defence",
            "Hitpoints",
            "Magic",
            "Prayer",
            "Ranged",
            "Slayer",
            "Strength",
        ]

    @staticmethod
    def base_non_combat_skills() -> List[str]:
        return [
            "Agility",
            "Astrology",
            "Cooking",
            "Crafting",
            "Farming",
            "Firemaking",
            "Fishing",
            "Fletching",
            "Herblore",
            "Magic",
            "Mining",
            "Runecrafting",
            "Smithing",
            "Summoning",
            "Thieving",
            "Township",
            "Woodcutting",
        ]

    def base_skills(self) -> List[str]:
        return list(set(self.base_combat_skills() + self.base_non_combat_skills()))

    @staticmethod
    def atlas_of_discovery_skills() -> List[str]:
        return [
            "Archaeology",
            "Cartography",
        ]

    @staticmethod
    def into_the_abyss_combat_skills() -> List[str]:
        return [
            "Corruption",
        ]

    @staticmethod
    def into_the_abyss_non_combat_skills() -> List[str]:
        return [
            "Harvesting",
        ]

    def into_the_abyss_skills(self) -> List[str]:
        return self.into_the_abyss_combat_skills() + self.into_the_abyss_non_combat_skills() + self.base_skills()

    def combat_skills(self) -> List[str]:
        skill_list = self.combat_skills()[:]
        if self.has_dlc_into_the_abyss:
            skill_list.extend(self.into_the_abyss_combat_skills())
        return skill_list

    def non_combat_skills(self) -> List[str]:
        skill_list = self.base_skills()[:]
        if self.has_dlc_atlas_of_discovery:
            skill_list.extend(self.atlas_of_discovery_skills())
        if self.has_dlc_into_the_abyss:
            skill_list.extend(self.into_the_abyss_non_combat_skills())
        return skill_list

    def skills(self) -> List[str]:
        skill_list = self.base_skills()[:]
        if self.has_dlc_atlas_of_discovery:
            skill_list.extend(self.atlas_of_discovery_skills())
        if self.has_dlc_throne_of_the_herald:
            skill_list.extend(self.into_the_abyss_skills())
        return skill_list

    @staticmethod
    def base_game_bosses() -> List[str]:
        return [
            "Mumma Chicken",
            "Zombie Leader",
            "Bandit Leader",
            "Elder Wizard",
            "Spider King",
            "Miolite Monarch",
            "The Kraken",
            "Protector of Ice",
            "Elder Dragon",
            "Malcs, the Guardian of Melvor",
            "Malcs, the Leader of Dragons",
            "Aeris",
            "Glacia",
            "Terran",
            "Ragnar",
            "Ahrenia",
            "Bane, Instrument of Fear",
        ]

    @staticmethod
    def atlas_of_discovery_bosses() -> List[str]:
        return [
            "Lava Golem",
            "Furious Mahogany",
            "Puppet Master",
            "Soul Taker Witch",
            "Nagaia",
        ]

    @staticmethod
    def throne_of_the_herald_bosses() -> List[str]:
        return [
            "Morellia",
            "Trogark",
            "RaZu, Lord of the Skies",
            "Spider Queen",
            "Lady Darkheart",
            "Fiozor, the Ancient Necromancer",
            "The Herald",
        ]

    @staticmethod
    def into_the_abyss_bosses() -> List[str]:
        return [
            "Abyssara, the Abyssal Warden",
            "Felth, the Toxic Martyr",
            "Karn, the Fear Bringer",
            "Vruul, the Withering Devourer",
            "Anketh, the Silent Harbinger",
            "Za-Kul, the Tendril Nightmare",
            "Nihlus, the Void Gazer",
            "Xon, the Abussal King",
        ]

    def bosses(self) -> List[str]:
        boss_list = self.base_game_bosses()[:]
        if self.has_dlc_atlas_of_discovery:
            boss_list.extend(self.altas_of_discovery_bosses())
        if self.has_dlc_throne_of_the_herald:
            boss_list.extend(self.throne_of_the_herald_bosses())
        if self.has_dlc_into_the_abyss:
            boss_list.extend(self.into_the_abyss_bosses())
        return boss_list

    @staticmethod
    def base_dungeons() -> List[str]:
        return [
            "Chicken Coop",
            "Undead Graveyard",
            "Bandit Base",
            "Hall of Wizards",
            "Spider Forest",
            "Miolite Caves",
            "Deep Sea Ship",
            "Frozen Cove",
            "Dragons Den",
            "Volcanic Cave",
            "Infernal Stronghold",
            "Air God Dungeon",
            "Water God Dungeon",
            "Earth God Dungeon",
            "Fire God Dungeon",
            "Stronghold of the Undead",
            "Stronghold of Magic",
            "Stronghold of Dragons",
            "Stronghold of the Gods",
        ]

    @staticmethod
    def atlas_of_discovery_dungeons() -> List[str]:
        return [
            "Golem Territory",
            "Unholy Forest",
            "Trickery Temple",
            "Cult Grounds",
            "Underwater City",
        ]

    @staticmethod
    def throne_of_the_herald_dungeons() -> List[str]:
        return [
            "Ancient Sanctuary",
            "Underground Lava Lake",
            "Lightning Region",
            "Lair of the Spider Queen",
            "Cursed Forest",
            "Necromancers Palace",
        ]

    @staticmethod
    def into_the_abyss_dungeons() -> List[str]:
        return [
            "The Abyssal Approach",
            "Into the Abyss",
            "Depths of Woe",
            "Depths of Decay",
            "Depths of Fear",
            "Depths of Ruin",
            "Depths of Isolation",
            "Depths of Dissolve",
            "Depths of Resolve",
            "Stronghold of Blight",
            "Stronghold of Fear",
            "Stronghold of Nightmares",
            "Stronghold of the Overlords",
        ]

    def dungeons(self) -> List[str]:
        dungeon_list = self.base_dungeons()[:]
        if self.has_dlc_atlas_of_discovery:
            dungeon_list.extend(self.atlas_of_discovery_dungeons())
        if self.has_dlc_throne_of_the_herald:
            dungeon_list.extend(self.throne_of_the_herald_dungeons())
        if self.has_dlc_into_the_abyss:
            dungeon_list.extend(self.into_the_abyss_dungeons())
        return dungeon_list

    @staticmethod
    def base_events() -> List[str]:
        return [
            "Into the Mist",
            "Impending Darkness Event",
        ]

    @staticmethod
    def throne_of_the_herald_events() -> List[str]:
        return [
            "Throne of the Herald",
        ]

    @staticmethod
    def into_the_abyss_events() -> List[str]:
        return [
            "The Final Depth",
        ]

    def events(self) -> List[str]:
        event_list = self.base_events()[:]
        if self.has_dlc_throne_of_the_herald:
            event_list.extend(self.throne_of_the_herald_events())
        if self.has_dlc_into_the_abyss:
            event_list.extend(self.into_the_abyss_events())
        return event_list

    @staticmethod
    def base_monsters() -> List[str]:
        return [
            "Adamant Knight",
            "Adult Farmer",
            "Aeris",
            "Ahrenia (Stronghold)",
            # "Ahrenia",
            "Air Golem",
            "Air Guard",
            "Air Monster",
            "Aleron",
            "Angel",
            "Bandit Leader",
            "Bandit Trainee",
            "Bandit",
            # "Bane, Instrument of Fear",
            "Bat",
            "Big Bat",
            "Black Dragon",
            "Black Knight",
            "Blue Dragon",
            "Bounty Hunter",
            "Brown Spider",
            "Cerberus",
            "Chaotic Greater Dragon",
            "Chick",
            "Chicken",
            "Confused Pirate",
            "Cow",
            "Cursed Lich",
            "Cursed Maiden",
            "Cursed Pirate Captain",
            "Dark Horned Elite",
            "Dark Wizard",
            "Druid",
            "Earth Golem",
            "Earth Guard",
            "Earth Monster",
            "Elder Dragon",
            "Elder Vampire",
            "Elder Wizard",
            "Elementalist (Stronghold)",
            "Elementalist",
            "Elerine Archer",
            "Elerine Mage",
            "Elerine Warrior",
            "Evil Spider",
            "Eye of Fear",
            "Eyes",
            "Fairy",
            "Fearful Eye",
            "Fierce Devil (Stronghold)",
            "Fire Golem",
            "Fire Guard",
            "Fire Monster",
            "Fire Spirit",
            "First Mate",
            "Frozen Archer",
            "Frozen Mammoth",
            "Furious Horned Elite",
            "Ghost Mercenary",
            "Ghost Sailor",
            "Ghost",
            "Giant Crab",
            "Giant Moth",
            "Glacia",
            "Golbin",
            "Goo Monster",
            "Greater Skeletal Dragon",
            "Green Dragon",
            "Green Goo Monster",
            "Green Slime",
            "Griffin",
            "Hill Giant",
            "Holy Archer",
            "Hunting Greater Dragon",
            "Ice Monster",
            "Ice Troll",
            "Ice",
            "Ignis",
            "Incendius",
            "Junior Farmer",
            "Ku-tul",
            "Leech",
            "Legaran Wurm",
            "Lissia",
            "Lots of Eyes",
            "Malcs, the Guardian of Melvor",
            "Malcs, the Leader of Dragons",
            "Many Eyed Monster",
            "Master Farmer",
            "Master Wizard",
            "Miolite Monarch",
            "Miolite Sprig",
            "Miolite Trio",
            "Miolite Warden",
            "Mistral",
            "Mithril Knight",
            "Moist Monster",
            "Moss Giant",
            "Mumma Chicken",
            "Murtia",
            # "Mysterious Figure - Phase 1 (Stronghold)",
            # "Mysterious Figure - Phase 1",
            # "Mysterious Figure - Phase 2 (Stronghold)",
            # "Mysterious Figure - Phase 2",
            "Necromancer",
            "Noxious Serpent",
            "Ophidia",
            "Paladin",
            "Pegasus",
            "Phoenix",
            "Pirate Captain",
            "Pirate",
            "Plant",
            "Prat, the Guardian of Secrets (Stronghold)",
            "Prat, the Guardian of Secrets",
            "Prat, the Protector of Secrets",
            "Priest",
            "Protector of Ice",
            "Purple Goo Monster",
            "Pyra",
            "Raging Horned Elite",
            "Ragnar",
            "Rancora Spider",
            "Ranged Golbin",
            "Red Devil",
            "Red Dragon",
            "Resurrected Eye",
            "Rokken",
            "Rune Knight",
            "Sand Beast",
            "Scattered Goo Monster",
            "Seagull",
            "Seething Horned Elite",
            "Shaman",
            "Shipwreck Beast",
            "Skeleton",
            "Slime Shooter",
            "Spider King",
            "Spider",
            "Spiked Red Claw",
            "Steel Knight",
            "Strange Eyed Monster",
            "Superior Eyed Monster",
            "Sweaty Monster",
            "Tentacle",
            "Terran",
            "The Eye",
            "The Kraken",
            "Thief",
            "Turkul Archers",
            "Turkul General",
            "Turkul Giant",
            "Turkul Riders",
            "Turkul Throwers",
            "Umbora",
            "Valkyrie",
            "Vampiric Bat",
            "Venomous Snake",
            "Vicious Serpent",
            "Voltaire",
            "Water Golem",
            "Water Guard",
            "Water Monster",
            "Wet Monster",
            "Wicked Greater Dragon",
            "Wizard",
            "Zombie Hand",
            "Zombie Leader",
            "Zombie",
        ]

    @staticmethod
    def atlas_of_discovery_monsters() -> List[str]:
        return [
            "Angry Teak",
            "Blind Archer",
            "Blind Ghost",
            "Blind Mage",
            "Blind Warrior",
            "Crystal Barrager",
            "Crystal Behemoth",
            "Crystal Manipulator",
            "Crystal Prowler",
            "Crystal Shatterer",
            "Crystal Smasher",
            "Cult Imp",
            "Cult Member",
            "Cult Monster",
            "Cursed Spirit",
            "Earth Golem",
            "Evil Oak",
            "Fake Door",
            "Furious Mahogany",
            "Granite Golem",
            "Grumpy Willow",
            "Illusive Roots",
            "Lady Darkheart",
            "Lava Golem",
            "Lich",
            "Magic Golem",
            "Magic Mirror",
            "Mermaid Archer",
            "Merman Guard",
            "Merman",
            "Nagaia",
            "Poison Bloater",
            "Poison Leecher",
            "Poison Roamer",
            "Poison Slime",
            "Possessed Barrel",
            "Puppet Master",
            "Raging Maple",
            "Ranged Golem",
            "Soul Taker Witch",
            "Treacherous Jellyfish",
            "Tree Giant",
            "Tree Spirit",
        ]

    @staticmethod
    def throne_of_the_herald_monsters() -> List[str]:
        return [
            "Alraune",
            "Arctair",
            "Banshee",
            "Basher Spider",
            "Bel-Noth",
            "Burning Snake",
            "Cockatrice",
            "Conda",
            "Cursed Skeleton Warrior",
            "Dark Knight",
            "Enforcer Spider",
            "Fierce Devil",
            "Fiozor, the Ancient Necromancer",
            "Frost Golem",
            "Goliath Werewolf",
            "Gret-Yun",
            "Guardian Spider",
            "Guardian of the Herald",
            "Harkair",
            "Hungry Plant",
            "Ice Hydra",
            "Infernal Golem",
            "Kongamato",
            "Large Ice Troll",
            "Leviathan",
            "Lightning Golem",
            "Lightning Monkey",
            "Lightning Spirit",
            "Magic Fire Demon",
            "Manticore",
            "Monster Croc",
            "Morellia",
            "Mummy",
            "Phantom",
            "Plague Doctor",
            "Poison Toad",
            "Polar Bear",
            "RaZu, Lord of the Skies",
            "Scouter Spider",
            "Shadow Beast",
            "Siren",
            "Spectral Ice Wolf",
            "Spectre",
            "Spider Queen",
            "Statue",
            "Stone Snake",
            # "The Herald Phase 1",
            # "The Herald Phase 2",
            # "The Herald",
            "Torvair",
            "Trapper Spider",
            "Trogark",
            "Twin Sea Dragon Serpent",
            "Undead Werewolf",
            "Vampire",
            "Vorloran Devastator",
            "Vorloran Protector",
            "Vorloran Watcher",
            "Wicked Spider",
        ]

    @staticmethod
    def into_the_abyss_monsters() -> List[str]:
        return [
            "Abyssal Bat",
            "Abyssal Chicken",
            "Abyssal Cow",
            "Abyssal Plant",
            "Abyssal Scarecrow",
            "Abyssal Swooper",
            "Abyssal Wallclimber",
            "Abyssara, the Abyssal Warden",
            "Anketh, the Silent Harbinger",
            "Blighted Mantis",
            "Blighted Maw",
            "Blighted Moth",
            "Blighted Shadewing",
            "Blighted Sprayer",
            "Blighted Wisp",
            "Catacomb Sporeslinger",
            "Catacomb Terror",
            "Catacomb Wraith",
            "Catacomb Wurm",
            "Crimson Hound",
            "Crimson Leech",
            "Crimson Viper",
            "Dreadwalker Ghoul",
            "Dreadwalker Revenant",
            "Dreadwalker Wight",
            "Echo Drifter",
            "Echo Horror",
            "Echo Specter",
            "Echo Walker",
            "Eldritch Aberration",
            "Eldritch Ghoul",
            "Eldritch Mindeater",
            "Eldritch Phantom",
            "Eldritch Seeker",
            "Eldritch Soulbinder",
            "Eldritch Stalker",
            "Felth, the Toxic Martyr",
            "Fractured Beast",
            "Fractured Manticore",
            "Fractured Wyvern",
            "Greater Void Artificer",
            "Greater Void Entity",
            "Greater Void Vagrant",
            "Hollow Harbinger",
            "Hollow Nightmare",
            "Hollow Reaper",
            "Karn, the Fear Bringer",
            "Murmuring Trapper",
            "Murmuring Treant",
            "Murmuring Wollowtails",
            "Mutating Chicken",
            "Mutating Cow",
            "Mutating Plant",
            "Mutating Scarecrow",
            "Nhilus, the Void Gazer",
            "Petrifying Basilisk",
            "Petrifying Behemoth",
            "Petrifying Drake",
            "Ravenous Dreadwing",
            "Ravenous Razortalon",
            "Ravenous Shadowfang",
            "Shadow Illusion",
            "Shadow Tormentor",
            "Shadow Trickster",
            "Silentsnap Giantcrab",
            "Silentsnap Siren",
            "Silentsnap Tortoise",
            "Smog Fiend",
            "Smog Golem",
            "Smog Slime",
            "Smog Virefang",
            "Tangled Serpent",
            "Tangled Thornbeast",
            "Tangled Thorns",
            "Tangled Weaver",
            "Toxic Bloom",
            "Toxic Serpent",
            "Toxic Swarm",
            "Void Apostle",
            "Void Doppelganger",
            "Void Dweller",
            "Void Gargantuan",
            "Void Harbinger",
            "Void Nightstalker",
            "Vruul, the Withering Devourer",
            "Wailing Ambusher",
            "Wailing Poltergeist",
            "Wailing Shade",
            "Whispering Drifter",
            "Whispering Manta",
            "Whispering Octopus",
            "Withering Bonearcher",
            "Withering Boneguard",
            "Withering Bonemage",
            # "Xon, the Abyssal King (Phase 1)",
            # "Xon, the Abyssal King (Phase 2)",
            # "Xon, the Abyssal King (Phase 3)",
            "Za-Kul, the Tendril Nightmare",
        ]

    def monsters(self) -> List[str]:
        monster_list = self.base_monsters()[:]
        if self.has_dlc_atlas_of_discovery:
            monster_list.extend(self.atlas_of_discovery_monsters())
        if self.has_dlc_throne_of_the_herald:
            monster_list.extend(self.throne_of_the_herald_monsters())
        if self.has_dlc_into_the_abyss:
            monster_list.extend(self.into_the_abyss_monsters())
        return monster_list


# Archipelago Options
class MelvorIdleDLCOwned(OptionSet):
    """
    Indicates which Melvor Idle DLCs the player owns, if any.
    """
    display_name = "Melvor Idle DLC Owned"
    valid_keys = [
        "Atlas of Discovery",
        "Throne of the Herald",
        "Into the Abyss",
    ]

    default = valid_keys
