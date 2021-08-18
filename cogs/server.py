import discord, config
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def support(self, ctx):
        "Contact the staff"

        try: await ctx.author.send(embed=discord.Embed(title="Ticket", description="Hi, you can type here your problem to open a ticket.\nYou'll be put in contact with the staff.", colour=self.bot.colour()))
        except discord.errors.Forbidden:
            await ctx.reply(embed=discord.Embed(description="I couldn't DM you, make sure your **DMs** are **open**!", colour=discord.Colour.red()), mention_author=False)
        else:
            await ctx.reply(embed=discord.Embed(description="Check your DMs!", colour=self.bot.colour()), mention_author=False)

def setup(bot):
    bot.add_cog(Server(bot))
