from . import handler

endpoint = "players"


class Player:
    def __init__(self, player_name):
        player_data = handler.get(endpoint, player_name)[0]

        self.name = player_data["name"]
        self.uuid = player_data["uuid"]
        self.title = player_data["title"]
        self.surname = player_data["surname"]
        self.formatted_name = player_data["formattedName"]
        self.about = player_data["about"]

        self.town = player_data["town"]["name"]
        self.town_uuid = player_data["town"]["uuid"]

        self.nation = player_data["nation"]["name"]
        self.nation_uuid = player_data["nation"]["uuid"]

        self.timestamps = player_data["timestamps"]
        self.registered = player_data["timestamps"]["registered"]
        self.joined_town_at = player_data["timestamps"]["joinedTownAt"]
        self.last_online = player_data["timestamps"]["lastOnline"]

        self.status = player_data["status"]
        self.is_online = player_data["status"]["isOnline"]
        self.is_npc = player_data["status"]["isNPC"]
        self.is_mayor = player_data["status"]["isMayor"]
        self.is_king = player_data["status"]["isKing"]
        self.has_town = player_data["status"]["hasTown"]
        self.has_nation = player_data["status"]["hasNation"]

        self.stats = player_data["stats"]
        self.balance = player_data["stats"]["balance"]
        self.num_friends = player_data["stats"]["numFriends"]

        self.perms = player_data["perms"]
        self.build_perms = player_data["perms"]["build"]
        self.destroy_perms = player_data["perms"]["destroy"]
        self.switch_perms = player_data["perms"]["switch"]
        self.item_use_perms = player_data["perms"]["itemUse"]
        self.flags = player_data["perms"]["flags"]
        self.pvp_flag = player_data["perms"]["flags"]["pvp"]
        self.explosion_flag = player_data["perms"]["flags"]["explosion"]
        self.fire_flag = player_data["perms"]["flags"]["fire"]
        self.mobs_flag = player_data["perms"]["flags"]["mobs"]

        self.ranks = player_data["ranks"]
        self.town_ranks = player_data["ranks"]["townRanks"]
        self.nation_ranks = player_data["ranks"]["nationRanks"]

        self.friends = [friend["name"] for friend in player_data["friends"]]
