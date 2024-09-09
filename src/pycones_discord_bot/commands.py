from __future__ import annotations

from discord.app_commands import command, describe


@command
def ping() -> str:
    return "Pong!"
