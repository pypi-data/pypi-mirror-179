from httpx import Client

from ..Pylertatron import Pylertatron
from ..commands import Command


class SyncPylertatron(Pylertatron):
    def __init__(self, webhook_url, balance_ratio, api_key_name, client):
        super().__init__(webhook_url, balance_ratio, api_key_name)
        self.client: Client = client

    def send_alert(self, symbol: str, commands: list[Command], tags: list[str] = None):
        alert = self.generate_alert(symbol, commands, tags)
        data = {"message": alert}
        self.client.post(self.webhook_url, json=data)


def create_pylertatron(webhook_url, balance_ratio, api_key_name) -> SyncPylertatron:
    client = Client()
    return SyncPylertatron(webhook_url, balance_ratio, api_key_name, client=client)
