from __future__ import annotations

import requests

from ..config import config
from ..interfaces import Ticket, TicketNotFoundError, TicketPlatform


class Pretix(TicketPlatform[str, Ticket]):
    def __init__(self) -> None:
        self._url = f"https://api.pretix.eu/api/v1/organizers/{config.organizer}/events/{config.event}"
        self._session = requests.Session()
        self._session.headers["Authorization"] = f"Token {config.pretix_token}"
        self._session.headers["Accept"] = "application/json"

    def find_ticket_by_id(self, id: str) -> Ticket:
        with self._session as sess:
            res = sess.get(f"{self._url}/orders/{id}/")

        if res.status_code == 404:
            raise TicketNotFoundError(f"Ticket {id} not found")

        data = res.json()
        return Ticket(
            id=data["code"], attendee=data["attendee_name"], email=data["email"]
        )
