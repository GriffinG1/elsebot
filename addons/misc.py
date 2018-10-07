from datetime import datetime

from discord import Embed, errors, Color, Member
from discord.ext import commands
import datetime


class Misc:
    """
    Miscellaneous commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True) # taken from https://github.com/appu1232/Discord-Selfbot/blob/873a2500d2c518e0d25ca5a6f67828de60fbda99/cogs/misc.py#L626
    async def ping(self, ctx):
        """Pong!"""
        msgtime = ctx.message.created_at.now()
        await (await self.bot.ws.ping())
        now = datetime.datetime.now()
        ptime = now - msgtime
        await ctx.send(':ping_pong:! Pong! Response time: %s ms' % str(ptime.microseconds / 1000.0))
    @commands.command(pass_context=True, aliases=['mc'])
    async def membercount(self, ctx):
        """Prints current member count"""
        await ctx.send("{} currently has {} members!"
                       "".format(ctx.guild.name, len(ctx.guild.members)))
        return

    @commands.command()
    async def about(self, ctx):
        """About elsebot."""
        await ctx.send("View my source code here: https://github.com/SizzlinRoast/elsebot")

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount):
        """Clears a given amount of messages. (Mods only)"""

        channel = ctx.message.channel
        try:
            n = int(amount) + 1
        except ValueError:
            return await ctx.send("Please mention a valid amount of messages!")

        try:
            await channel.purge(limit=n)
            await ctx.send("🗑️ Cleared {} messages in this channel!".format(amount))
            try:
                emb = Embed(title="Messages Cleared", colour=Color.red())
                emb.add_field(
                    name="Mod:", value=ctx.message.author, inline=True)
                emb.add_field(name="Channel:",
                              value=ctx.message.channel, inline=True)
                emb.add_field(name="Amount:", value=amount, inline=True)
                logchannel = self.bot.logs_channel
                await logchannel.send("", embed=emb)
            except errors.Forbidden:
                await ctx.send("💢 I dont have permission to do this.")

        except errors.Forbidden:
            await ctx.say("💢 I don't have permission to do this.")

    @commands.command()
    async def userinfo(self, ctx):
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            member = ctx.message.author
        uname = member.name
        discrim = member.discriminator
        Uid = member.id
        displayName = member.display_name
        isBot = member.bot
        cTime = member.created_at
        jTime = member.joined_at
        str1 = "{}#{}".format(uname, discrim)
        str2 = "{}".format(Uid)
        if displayName == uname:
            displayName = "None"
        str3 = "{}".format(displayName)
        str4 = "{}".format(str(isBot))
        str5 = "{}".format(cTime)
        str6 = "{}".format(jTime)
        emb = Embed(title="Userinfo", color=0x00ff00)
        emb.add_field(name="Member", value=str1 + "\n", inline=True)
        emb.add_field(name="ID", value=str2 + "\n", inline=True)
        emb.add_field(name="Nickname", value=str3 + "\n", inline=True)
        emb.add_field(name="Bot?", value=str4 + "\n", inline=True)
        emb.add_field(name="Account Created", value=str5 + "\n", inline=True)
        emb.add_field(name="Joined Server", value=str6 + "\n", inline=True)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send("", embed=emb)

    @commands.command()
    async def bean(self, ctx, member: Member=None, *, reason: str=""):
        """Ban a member. (Staff Only)"""
        if not member:
            await ctx.send("Please mention a user.")
            return
        if member == ctx.message.author:
            await ctx.send("You cannot ban yourself!")
            return
        elif ctx.me is member:
            await ctx.send("I am unable to ban myself to prevent stupid mistakes.\n"
                           "Please ban me by hand!")
            return
        else:
            await ctx.send("I've banned {}.".format(member))

def setup(bot):
    bot.add_cog(Misc(bot))
