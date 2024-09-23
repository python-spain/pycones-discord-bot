from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Hashable, Generic, TypeVar, TypedDict


class Ticket(TypedDict):
    """A ticket represents a ticket for an event. It contains the minimum information a ticket
    should have."""

    id: str
    """The ID of the ticket."""

    attendee: str
    """The attendee full name."""

    email: str
    """The attendee email."""


_K = TypeVar("_K", bound=Hashable)
_T = TypeVar("_T", bound=Ticket)


class TicketPlatform(ABC, Generic[_K, _T]):
    """A ticket represents an entity which interfaces a ticketing platform for accessing
    information about attendees and their tickets.
    """

    @abstractmethod
    def find_ticket_by_id(self, id: _K) -> _T:
        """Find a ticket by its ID. If the ticket does not exist, it should raise a
        :obj:`TicketNotFoundError` exception.

        Args:
            id (:obj:`_K`): The ID of the ticket. Must be unique and immutable.

        Returns:
            :obj:`_T`: The ticket. It must be either :class:`Ticket` or a subclass of it.
        """


class TicketNotFoundError(Exception):
    """Raised when a ticket is not found."""
