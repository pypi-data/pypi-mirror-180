import asyncio
import os

import aiohttp
import fire
from discord import Webhook, Embed

WEBHOOK_URL = os.getenv("MICROHOOK_URL")

color_scheme = {
    "info": 0xA3BE8C,
    "warning": 0xEBCB8B,
    "error": 0xD08770,
    "critical": 0xBF616A,
}


def build_embed(message: str, level: str, title: str | None = None) -> Embed:
    if title is None:
        title = level.capitalize()

    embed = Embed(title=title, description=message, color=color_scheme[level])
    embed.set_author(
        name="MicroHook",
        url="https://github.com/tkillestein/microhook",
        icon_url="https://upload.wikimedia.org/wikipedia/commons/a/af/Composite_image_of_Supernova_1987A.jpg",
    )
    return embed


class MicroHook(object):
    def __init__(self, webhook_url: str = WEBHOOK_URL):
        self.webhook_url = webhook_url

    async def send_webhook(self, message_embed: Embed) -> None:
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(self.webhook_url, session=session)
            await webhook.send(embed=message_embed, username="MicroHook")

    def info(self, message: str) -> None:
        embed = build_embed(level="info", message=message)
        asyncio.run(self.send_webhook(message_embed=embed))

    def warning(self, message: str) -> None:
        embed = build_embed(level="warning", message=message)
        asyncio.run(self.send_webhook(message_embed=embed))

    def error(self, message: str) -> None:
        embed = build_embed(level="error", message=message)
        asyncio.run(self.send_webhook(message_embed=embed))

    def critical(self, message) -> None:
        embed = build_embed(level="critical", message=message)
        asyncio.run(self.send_webhook(message_embed=embed))
