from . import handler


class Server:
    def __init__(self):
        server_data = handler.get()
        # Version
        self.version = server_data["version"]
        
        # Moon Phase
        self.moon_phase = server_data["moonPhase"]

        # Timestamps
        self.timestamps = server_data["timestamps"]
        self.new_day_time = server_data["timestamps"]["newDayTime"]
        self.server_time_of_day = server_data["timestamps"]["serverTimeOfDay"]

        # Status
        self.has_storm = server_data["status"]["hasStorm"]
        self.is_thundering = server_data["status"]["isThundering"]

        # Stats
        self.stats = server_data["stats"]
        self.time = server_data["stats"]["time"]
        self.full_time = server_data["stats"]["fullTime"]
        self.max_players = server_data["stats"]["maxPlayers"]
        self.num_online_players = server_data["stats"]["numOnlinePlayers"]
        self.num_online_nomads = server_data["stats"]["numOnlineNomads"]
        self.num_residents = server_data["stats"]["numResidents"]
        self.num_nomads = server_data["stats"]["numNomads"]
        self.num_towns = server_data["stats"]["numTowns"]
        self.num_town_blocks = server_data["stats"]["numTownBlocks"]
        self.num_nations = server_data["stats"]["numNations"]
        self.num_quarters = server_data["stats"]["numQuarters"]
        self.num_cuboids = server_data["stats"]["numCuboids"]

        # Vote Party
        self.vote_party = server_data["voteParty"]
        self.vote_target = server_data["voteParty"]["target"]
        self.vote_num_remaining = server_data["voteParty"]["numRemaining"]
