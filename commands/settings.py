import discord
from discord import app_commands
from discord.ext import commands

from models import Club
from services import BrawlApi, Database


class Settings(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.__db = Database()
        self.__ba = BrawlApi()

    async def send_embed(
        self,
        interaction: discord.Interaction,
        title: str,
        description: str,
        is_error: bool = False,
    ) -> None:
        color = discord.Color.dark_red() if is_error else discord.Color.random()
        embed = discord.Embed(title=title, description=description, color=color)
        await interaction.followup.send(embed=embed)

    async def __verivy_existence_clubs(
        self, interaction: discord.Interaction, clubs: list[Club] | None
    ) -> list[Club] | None:
        if clubs:
            return clubs
        txt = "Aún no hay clubs en la base de datos agrega uno con ```/agregar_club```"
        await self.send_embed(interaction, "", txt, is_error=True)

    @app_commands.command(description="Ve los clubs en la base de datos")
    async def ver_clubs(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=True)
        clubs = await self.__verivy_existence_clubs(interaction, self.__db.get_clubs())

        if clubs:
            embed = discord.Embed(color=discord.Color.random())

            for club in clubs:
                embed.add_field(name=club.name, value=club.tag, inline=False)
            await interaction.followup.send(embed=embed)

    @app_commands.command(description="Agrega un club a la base de datos")
    @app_commands.describe(tag="Ingresa el tag del club")
    async def agregar_club(self, interaction: discord.Interaction, tag: str) -> None:
        await interaction.response.defer(ephemeral=True)

        txt = self.__db.set_club(tag)
        await self.send_embed(interaction, txt, "", "exitosamente" not in txt)

    @app_commands.command(description="Elimina un club a la base de datos")
    @app_commands.describe(tag="Ingresa el tag del club")
    async def eliminar_club(self, interaction: discord.Interaction, tag: str) -> None:
        await interaction.response.defer(ephemeral=True)
        clubs = await self.__verivy_existence_clubs(interaction, self.__db.get_clubs())

        if clubs:
            txt = self.__db.remove_club(tag)
            await self.send_embed(interaction, txt, "", "exitosamente" not in txt)

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

    @app_commands.command(
        name="vincular", description="Vincula un perfil del club contigo"
    )
    @app_commands.describe(tag="Ingresa el tag")
    async def vincular_perfil(self, interaction: discord.Interaction, tag: str) -> None:
        await interaction.response.defer(ephemeral=True)
        await self.send_embed(interaction, "", tag)

    @vincular_perfil.autocomplete("tag")
    async def vincular_perfil_autocomplete(
        self, _, current: str
    ) -> list[app_commands.Choice[str]]:
        clubs = self.__db.get_clubs()
        members = self.__ba.get_members_from_clubs(
            [c.tag for c in clubs] if clubs else []
        )
        return (
            [
                app_commands.Choice(name=member.name, value=member.tag)
                for member in members
                if (current.lower() in member.name.lower())
                or (current.lower() in member.tag.lower())
            ][:25]
            if members
            else []
        )


async def setup(bot) -> None:
    await bot.add_cog(Settings(bot))
