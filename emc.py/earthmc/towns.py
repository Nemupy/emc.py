from . import handler

endpoint = "towns"


class Town:
    def __init__(self, town_name):
        town_data = handler.get(endpoint, town_name)[0]

        self.name = town_data["name"]
        self.uuid = town_data["uuid"]
        self.board = town_data["board"]
        self.founder = town_data["founder"]
        self.wiki = town_data["wiki"]

        # Mayor
        self.mayor = town_data["mayor"]["name"]
        self.mayor_uuid = town_data["mayor"]["uuid"]

        # Nation
        self.nation = town_data["nation"]["name"]
        self.nation_uuid = town_data["nation"]["uuid"]

        # Timestamps
        self.timestamps = town_data["timestamps"]
        self.registered = town_data["timestamps"]["registered"]
        self.joined_nation_at = town_data["timestamps"]["joinedNationAt"]
        self.ruined_at = town_data["timestamps"]["ruinedAt"]

        # Status
        self.status = town_data["status"]
        self.is_public = town_data["status"]["isPublic"]
        self.is_open = town_data["status"]["isOpen"]
        self.is_neutral = town_data["status"]["isNeutral"]
        self.is_capital = town_data["status"]["isCapital"]
        self.is_over_claimed = town_data["status"]["isOverClaimed"]
        self.is_ruined = town_data["status"]["isRuined"]
        self.is_for_sale = town_data["status"]["isForSale"]
        self.has_nation = town_data["status"]["hasNation"]
        self.has_overclaim_shield = town_data["status"]["hasOverclaimShield"]
        self.can_outsiders_spawn = town_data["status"]["canOutsidersSpawn"]

        # Stats
        self.stats = town_data["stats"]
        self.num_town_blocks = town_data["stats"]["numTownBlocks"]
        self.max_town_blocks = town_data["stats"]["maxTownBlocks"]
        self.bonus_blocks = town_data["stats"]["bonusBlocks"]
        self.num_residents = town_data["stats"]["numResidents"]
        self.num_trusted = town_data["stats"]["numTrusted"]
        self.num_outlaws = town_data["stats"]["numOutlaws"]
        self.balance = town_data["stats"]["balance"]
        self.for_sale_price = town_data["stats"]["forSalePrice"]

        # Perms
        self.perms = town_data["perms"]
        self.build_perms = town_data["perms"]["build"]
        self.destroy_perms = town_data["perms"]["destroy"]
        self.switch_perms = town_data["perms"]["switch"]
        self.item_use_perms = town_data["perms"]["itemUse"]
        self.Flags = town_data["perms"]["flags"]
        self.pvp_flag = town_data["perms"]["flags"]["pvp"]
        self.explosion_flag = town_data["perms"]["flags"]["explosion"]
        self.fire_flag = town_data["perms"]["flags"]["fire"]
        self.mobs_flag = town_data["perms"]["flags"]["mobs"]

        # Coordinates
        self.spawn_world = town_data["coordinates"]["spawn"]["world"]
        self.spawn_x = town_data["coordinates"]["spawn"]["x"]
        self.spawn_y = town_data["coordinates"]["spawn"]["y"]
        self.spawn_z = town_data["coordinates"]["spawn"]["z"]
        self.spawn_pitch = town_data["coordinates"]["spawn"]["pitch"]
        self.spawn_yaw = town_data["coordinates"]["spawn"]["yaw"]
        self.home_block = town_data["coordinates"]["homeBlock"]
        self.town_blocks = town_data["coordinates"]["townBlocks"]

        # Residents
        self.residents = [resident["name"]
                          for resident in town_data["residents"]]

        # Trusted
        self.trusted = [trusted["name"] for trusted in town_data["trusted"]]

        # Outlaws
        self.outlaws = [outlaw["name"] for outlaw in town_data["outlaws"]]

        # Quarters
        self.quarters = town_data["quarters"]

        # Ranks
        self.ranks = town_data["ranks"]