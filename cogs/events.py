import discord, config
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        if interaction.data['type'] != 1: return
        name = interaction.data['name'].lower()
        if name == "support":
            try: await interaction.user.send(embed=discord.Embed(title="Ticket", description="Hi, you can type here your problem to open a ticket.\nYou'll be put in contact with the staff.", colour=self.bot.colour()))
            except discord.errors.Forbidden:
                await interaction.response.send_message(embed=discord.Embed(description="I couldn't DM you, make sure your **DMs** are **open**!", colour=discord.Colour.red()), ephemeral=True)
            else:
                await interaction.response.send_message(embed=discord.Embed(description="Check your DMs!", colour=self.bot.colour()), ephemeral=True)

def setup(bot):
    bot.add_cog(Events(bot))
