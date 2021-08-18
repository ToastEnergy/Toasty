import discord, config
from discord.ext import commands

class DMS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        guild = self.bot.get_guild(config.ids.guild)
        category = self.bot.get_channel(config.ids.category)

        user = message.author
        shared = [g.name for g in self.bot.guilds if g.get_member(user.id)]
        s = "servers"

        if len(shared) == 1 or len(shared) == 0:
            s = "server"

        res = ""
        for a in shared:
            res += f"• {a}\n"

        if not message.guild:

            if str(message.author.id) in [g.topic for g in category.channels]:
                channel = discord.utils.get(category.channels, topic=str(message.author.id))

            else:
                channel = await guild.create_text_channel(name=str(f"{str(message.author)}"), category=category, topic=message.author.id)

                emb = discord.Embed(description=f"**You are now in chat with Toast Energy staff**", colour=self.bot.colour())
                await user.send(embed=emb)

                await channel.send(f"<@&{config.ids.staff}>", delete_after=1)

                emb = discord.Embed(description=f"**New ticket {message.author}**", colour=self.bot.colour())
                await channel.send(embed=emb)

            emb = discord.Embed(description=f"**{message.author}**: {message.content}", colour=self.bot.colour())
            if message.attachments:
                if message.attachments[0].filename.endswith(("png", "jpg", "jpeg", "webp", "gif")):
                    emb.set_image(url=message.attachments[0].url)

                else:
                    emb.description += f"\n\n[{message.attachments[0].filename}]({message.attachments[0].url})"
            await channel.send(embed=emb)

        elif message.guild == guild:
            if message.channel.category == category:
                user = self.bot.get_user(int(message.channel.topic))
                if not user:
                    return

                else:
                    if message.content != f"{ctx.prefix}close":
                        emb = discord.Embed(description=f"**{message.author}**: {message.content}", colour=self.bot.colour())
                        if message.attachments:
                            if message.attachments[0].filename.endswith(("png", "jpg", "jpeg", "webp", "gif")):
                                emb.set_image(url=message.attachments[0].url)

                            else:
                                emb.description += f"\n\n[{message.attachments[0].filename}]({message.attachments[0].url})"
                        await user.send(embed=emb)

    @commands.has_permissions(manage_messages=True)
    @commands.command(hidden=True)
    async def close(self, ctx, *, channel: discord.TextChannel = None):

        channel = channel or ctx.channel

        if channel.category.id == config.ids.category:
            await ctx.send(f"The Ticket **{channel.name}** has been **closed**!")
            await channel.delete()

        else:
            await channel.send("**That** channel **is not** a ticket!")

def setup(bot):
    bot.add_cog(DMS(bot))
