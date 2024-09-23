from __future__ import annotations

from functools import lru_cache
import tomllib


@lru_cache(maxsize=1)
def _get_toml() -> dict:
    with open("config.toml", "rb") as fd:
        return tomllib.load(fd)


def get_pretix_token() -> str:
    return _get_toml()["pretix"]["token"]


def get_organizer() -> str:
    return _get_toml()["pretix"]["organizer"]


def get_event() -> str:
    return _get_toml()["pretix"]["event"]

