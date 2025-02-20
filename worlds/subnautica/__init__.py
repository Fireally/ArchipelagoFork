import logging
from typing import List, Dict, Any

from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification, RegionType
from worlds.AutoWorld import World, WebWorld
from . import Items
from . import Locations
from . import Creatures
from . import Options
from .Items import item_table
from .Rules import set_rules

logger = logging.getLogger("Subnautica")


class SubnaticaWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Subnautica randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Berserker"]
    )]


all_locations = {data["name"]: loc_id for loc_id, data in Locations.location_table.items()}
all_locations.update(Creatures.creature_locations)


class SubnauticaWorld(World):
    """
    Subnautica is an undersea exploration game. Stranded on an alien world, you become infected by
    an unknown bacteria. The planet's automatic quarantine will shoot you down if you try to leave.
    You must find a cure for yourself, build an escape rocket, and leave the planet.
    """
    game: str = "Subnautica"
    web = SubnaticaWeb()

    item_name_to_id = {data["name"]: item_id for item_id, data in Items.item_table.items()}
    location_name_to_id = all_locations
    options = Options.options

    data_version = 3
    required_client_version = (0, 3, 3)

    prefill_items: List[Item]
    creatures_to_scan: List[str]

    def generate_early(self) -> None:
        self.prefill_items = [
            self.create_item("Seaglide Fragment"),
            self.create_item("Seaglide Fragment")
        ]
        self.creatures_to_scan = self.world.random.sample(Creatures.all_creatures_presorted,
                                                          self.world.creature_scans[self.player].value)

    def create_regions(self):
        self.world.regions += [
            self.create_region("Menu", None, ["Lifepod 5"]),
            self.create_region("Planet 4546B",
                               Locations.events +
                               [location["name"] for location in Locations.location_table.values()] +
                               [creature+Creatures.suffix for creature in self.creatures_to_scan])
        ]

    # refer to Rules.py
    set_rules = set_rules

    def generate_basic(self):
        # Link regions
        self.world.get_entrance("Lifepod 5", self.player).connect(self.world.get_region("Planet 4546B", self.player))

        # Generate item pool
        pool = []
        neptune_launch_platform = None
        extras = self.world.creature_scans[self.player].value
        valuable = self.world.item_pool[self.player] == Options.ItemPool.option_valuable
        for item in item_table.values():
            for i in range(item["count"]):
                subnautica_item = self.create_item(item["name"])
                if item["name"] == "Neptune Launch Platform":
                    neptune_launch_platform = subnautica_item
                elif valuable and ItemClassification.filler == item["classification"]:
                    extras += 1
                else:
                    pool.append(subnautica_item)

        for item_name in self.world.random.choices(sorted(Items.advancement_item_names - {"Neptune Launch Platform"}),
                                                   k=extras):
            item = self.create_item(item_name)
            item.classification = ItemClassification.filler  # as it's an extra, just fast-fill it somewhere
            pool.append(item)

        self.world.itempool += pool

        # Victory item
        self.world.get_location("Aurora - Captain Data Terminal", self.player).place_locked_item(
            neptune_launch_platform)
        for event in Locations.events:
            self.world.get_location(event, self.player).place_locked_item(
                SubnauticaItem(event, ItemClassification.progression, None, player=self.player))
        # make the goal event the victory "item"
        self.world.get_location(self.world.goal[self.player].get_event_name(), self.player).item.name = "Victory"

    def fill_slot_data(self) -> Dict[str, Any]:
        goal: Options.Goal = self.world.goal[self.player]
        item_pool: Options.ItemPool = self.world.item_pool[self.player]
        vanilla_tech: List[str] = []
        if item_pool == Options.ItemPool.option_valuable:
            for item in Items.item_table.values():
                if item["classification"] == ItemClassification.filler:
                    vanilla_tech.append(item["tech_type"])

        slot_data: Dict[str, Any] = {
            "goal": goal.current_key,
            "vanilla_tech": vanilla_tech,
            "creatures_to_scan": self.creatures_to_scan
        }

        return slot_data

    def create_item(self, name: str) -> Item:
        item_id: int = self.item_name_to_id[name]

        return SubnauticaItem(name,
                              item_table[item_id]["classification"],
                              item_id, player=self.player)

    def create_region(self, name: str, locations=None, exits=None):
        ret = Region(name, RegionType.Generic, name, self.player)
        ret.world = self.world
        if locations:
            for location in locations:
                loc_id = self.location_name_to_id.get(location, None)
                location = SubnauticaLocation(self.player, location, loc_id, ret)
                ret.locations.append(location)
        if exits:
            for region_exit in exits:
                ret.exits.append(Entrance(self.player, region_exit, ret))
        return ret

    def get_pre_fill_items(self) -> List[Item]:
        return self.prefill_items

    def pre_fill(self) -> None:
        reachable = self.world.get_reachable_locations(player=self.player)
        self.world.random.shuffle(reachable)
        items = self.prefill_items.copy()
        for item in items:
            reachable.pop().place_locked_item(item)


class SubnauticaLocation(Location):
    game: str = "Subnautica"


class SubnauticaItem(Item):
    game: str = "Subnautica"
