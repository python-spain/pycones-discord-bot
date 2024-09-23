from __future__ import annotations

from functools import lru_cache

import pycones_discord_bot.config as config
import requests

_session = requests.Session()
_session.headers["Authorization"] = f"Token {config.get_pretix_token()}"


@lru_cache
def find_ticket_by_id(ticket_id: str) -> None:
    with _session.get(
        f"https://pretix.eu/api/organizers/{config.get_organizer()}/events/{config.get_event()}/tickets/{ticket_id}/"
    ) as response:
        response.raise_for_status()
        ...
