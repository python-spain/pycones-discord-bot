from __future__ import annotations

from functools import cached_property
from typing import Any
import tomllib


class Config:
    def __init__(self) -> None:
        with open("config.toml", "rb") as fd:
            self._toml = tomllib.load(fd)

    @cached_property
    def config(self) -> dict[str, Any]:
        return self._toml

    @cached_property
    def pretix_token(self) -> str:
        return self._toml["pretix"]["token"]

    @cached_property
    def organizer(self) -> str:
        return self._toml["pretix"]["organizer"]

    @cached_property
    def event(self) -> str:
        return self._toml["pretix"]["event"]


config = Config()
