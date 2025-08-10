from . import handler

endpoint = "nations"

class Nation:
    def __init__(self, nation_name):
        nation_data = handler.get(endpoint=endpoint, queries=nation_name)[0]

        self.name = nation_data["name"]
        self.uuid = nation_data["uuid"]
        self.board = nation_data["board"]
        self.dynmap_colour = nation_data["dynmapColour"]
        self.dynmap_outline = nation_data["dynmapOutline"]
        self.wiki = nation_data["wiki"]

        self.king = nation_data["king"]["name"]
        self.king_uuid = nation_data["king"]["uuid"]

        self.capital = nation_data["capital"]["name"]
        self.capital_uuid = nation_data["capital"]["uuid"]

        self.timestamps = nation_data["timestamps"]
        self.registered = nation_data["timestamps"]["registered"]

        self.status = nation_data["status"]
        self.is_public = nation_data["status"]["isPublic"]
        self.is_open = nation_data["status"]["isOpen"]
        self.is_neutral = nation_data["status"]["isNeutral"]

        self.stats = nation_data["stats"]
        self.num_town_blocks = nation_data["stats"]["numTownBlocks"]
        self.num_residents = nation_data["stats"]["numResidents"]
        self.num_towns = nation_data["stats"]["numTowns"]
        self.num_allies = nation_data["stats"]["numAllies"]
        self.num_enemies = nation_data["stats"]["numEnemies"]
        self.balance = nation_data["stats"]["balance"]

        self.spawn_world = nation_data["coordinates"]["spawn"]["world"]
        self.spawn_x = nation_data["coordinates"]["spawn"]["x"]
        self.spawn_y = nation_data["coordinates"]["spawn"]["y"]
        self.spawn_z = nation_data["coordinates"]["spawn"]["z"]
        self.spawn_pitch = nation_data["coordinates"]["spawn"]["pitch"]
        self.spawn_yaw = nation_data["coordinates"]["spawn"]["yaw"]

        self.residents = [resident["name"] for resident in nation_data["residents"]]

        self.towns = [town["name"] for town in nation_data["towns"]]

        self.allies = [ally["name"] for ally in nation_data["allies"]]

        self.enemies = [enemy["name"] for enemy in nation_data["enemies"]]

        self.ranks = nation_data["ranks"]
