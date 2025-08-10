from . import handler

class Discord:
    def __init__(self):
        self.endpoint = "discord"

    def discord_id(self, uuid: str):
        discord_data = self._get([{"type": "uuid", "value": uuid}])[0]
        return discord_data["id"]

    def minecraft_uuid(self, discord_id: str):
        discord_data = self._get([{"type": "discord", "value": discord_id}])[0]
        return discord_data["uuid"]

    def _get(self, queries):
        return handler.get(endpoint=self.endpoint, queries=queries)