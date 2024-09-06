import discord
from discord import app_commands
from discord.ext import commands

from services import Database


class Settings(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.__db = Database()

    async def send_embed(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        is_success: bool = True,
    ) -> None:
        color = discord.Color.random() if is_success else discord.Color.dark_red()
        embed = discord.Embed(title=title, description=description, color=color)
        await interaction.followup.send(embed=embed)

    @app_commands.command(description="Ve los clubs en la base de datos")
    async def ver_clubs(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=True)

        if clubs := self.__db.get_clubs():
            embed = discord.Embed(color=discord.Color.random())

            for club in clubs:
                embed.add_field(name=club.name, value=club.tag, inline=False)
            await interaction.followup.send(embed=embed)
        else:
            txt = "Aún no hay clubs en la base de datos agrega uno con ```/agregar_club```"
            await self.send_embed(interaction, "", txt, False)

    @app_commands.command(description="Agrega un club a la base de datos")
    @app_commands.describe(tag="Ingresa el tag del club")
    async def agregar_club(self, interaction: discord.Interaction, tag: str) -> None:
        await interaction.response.defer(ephemeral=True)

        txt = self.__db.set_club(tag)
        await self.send_embed(interaction, txt, "", "exitosamente" in txt)

    @app_commands.command(description="Elimina un club a la base de datos")
    @app_commands.describe(tag="Ingresa el tag del club")
    async def eliminar_club(self, interaction: discord.Interaction, tag: str) -> None:
        await interaction.response.defer(ephemeral=True)

        if self.__db.get_clubs():
            txt = self.__db.remove_club(tag)
            await self.send_embed(interaction, txt, "", "exitosamente" in txt)
        else:
            txt = "Aún no hay clubs en la base de datos agrega uno con ```/agregar_club```"
            await self.send_embed(interaction, "", txt, False)

    @eliminar_club.autocomplete("tag")
    async def eliminar_club_autocomplete(
        self, _, current: str
    ) -> list[app_commands.Choice[str]]:
        clubs = self.__db.get_clubs()
        return (
            [
                app_commands.Choice(name=club.name, value=club.tag)
                for club in clubs
                if current.lower() in club.name.lower()
            ]
            if clubs
            else []
        )


async def setup(bot) -> None:
    await bot.add_cog(Settings(bot))
