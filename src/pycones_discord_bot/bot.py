from __future__ import annotations

from typing import TYPE_CHECKING

from discord import Client
from discord.app_commands import CommandTree, command, describe, Command

if TYPE_CHECKING:
    from discord import Member


class PyConESBot(Client):
    def __init__(self) -> None:
        self.tree = CommandTree(self)
        self.tree.add_command(
            Command(
                name="register_rule",
                description="Register a rule",
                callback=self.register_rule,
            )
        )

    @describe(rule_id="The ID of the rule to register")
    async def register_rule(self, ctx, rule_id: int) -> None:
        self.rule_id = rule_id

    async def on_ready(self) -> None:
        if self.rule_id is not None:
            return

        msg = await self.fetch_guild(1234)

    async def on_member_join(self, member: Member) -> None:
        guild = member.guild
