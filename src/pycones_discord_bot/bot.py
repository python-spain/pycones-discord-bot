from __future__ import annotations
import os
from typing import TYPE_CHECKING, Optional
from dotenv import load_dotenv
from discord import Client, Intents, Interaction
from discord.app_commands import CommandTree, command, describe, Command

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if TYPE_CHECKING:
    from discord import Member

if TOKEN is None:
    raise ValueError("El token de Discord no está configurado. Asegúrate de que la variable DISCORD_TOKEN esté definida.")


class PyConESBot(Client):
    def __init__(self) -> None:
        intents = Intents.default()
        intents.members = True
        super().__init__(intents=intents)

        self.tree = CommandTree(self)
        self.rule_id: Optional[int] = None

        self.tree.add_command(
            Command(
                name="register_rule",
                description="Register a rule",
                callback=self.register_rule,
            )
        )

    @describe(rule_id="The ID of the rule to register")
    async def register_rule(self, interaction: Interaction, rule_id: int) -> None:
        """Comando para registrar una regla"""
        self.rule_id = rule_id
        await interaction.response.send_message(f"Rule {rule_id} registered!", ephemeral=True)

    async def on_ready(self) -> None:
        """Evento cuando el bot está listo"""
        print(f"Bot {self.user} está en línea.")
        if self.rule_id is None:
            print("No rule registered yet.")
        else:
            print(f"Rule {self.rule_id} está registrada.")

        await self.tree.sync()
    
    async def on_member_join(self, member: Member) -> None:
        """Evento cuando un miembro se une al servidor"""
        guild = member.guild
        print(f"Nuevo miembro {member.name} se ha unido a {guild.name}")
        # await member.send(f"¡Bienvenido a {guild.name}, {member.name}!")


bot = PyConESBot()
bot.run(TOKEN)