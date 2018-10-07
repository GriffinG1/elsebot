from discord.ext import commands


class Memes:
    """
    ayy lmao
    """

    def __init__(self, bot):
        self.bot = bot

    # sss like memes, quite a few gone

    @commands.command(hidden=True)
    async def rip(self, ctx):
        """F"""
        msg = await ctx.send("Press F to pay respects.")
        await msg.add_reaction("🇫")

    @commands.command(hidden=True)
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command(hidden=True)
    async def brickdurr(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/hzuXOHP.png")

    @commands.command(hidden=True)
    async def birds(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/fVAx5oh.png")

    @commands.command(hidden=True)
    async def macboy(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/IpQC6IF.png")
        
    # Kurisu memes
    @commands.command(hidden=True)
    async def dubyadud(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/Sohsi8s.png")

    @commands.command(hidden=True)
    async def rusure(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/dqh3fNi.png")

    @commands.command(hidden=True)
    async def permabrocked(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/ARsOh3p.jpg")

    @commands.command(hidden=True)
    async def thumbsup(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/hki1IIs.gifv")

    @commands.command(hidden=True)
    async def pbanjo(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/sBJKzuK.png")

    @commands.command(hidden=True)
    async def lisp(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/RQeZErU.png")

    @commands.command(hidden=True)
    async def blackalabi(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/JzFem4y.png")

    @commands.command(hidden=True)
    async def soghax(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/oQJy2eN.png")

    @commands.command(hidden=True)
    async def whatisr(self, ctx):
        """MEMES?"""
        await ctx.send("http://i.imgur.com/Z8HhfzJ.jpg")

    @commands.command(hidden=True)
    async def helpers(self, ctx):
        """MEMES?"""
        await ctx.send("http://i.imgur.com/0v1EgMX.png")

    @commands.command(hidden=True)
    async def concern(self, ctx):
        """MEMES?"""
        await ctx.send("https://i.imgur.com/cWXBb5g.png")

    @commands.command(hidden=True)
    async def r34(self, ctx):
        """MEMES?"""
        await ctx.send("http://i.imgur.com/sjQZKBF.gif")

    @commands.command(hidden=True)
    async def lucina(self, ctx):
        """MEMES?"""
        await ctx.send("http://i.imgur.com/ZPMveve.jpg")

    @commands.command(hidden=True)
    async def lucina2(self, ctx):
        """MEMES?"""
        await ctx.send("http://i.imgur.com/ZPMveve.jpg")

    
    # GIB DONGRODER LAZY DEV
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command(hidden=True)
    async def dongroder(self, ctx, variant=""):
        """MEMES?!?
        This meme has multiple variants : piter, swotch.
        If no variant is specified, it will defautlt to piter."""
        if variant == "piter":
            await ctx.send(
                "```Hey YOU. YES YOU!!!! YOU CAN CREATE A DOWNGRADER. JUST like can Plailect , "
                "Aurora Wright , astronautlevel and Apache Thunder and Kyojin work on a 3DS "
                "11.0 Downgrader!!!!!!!!!!!!!!!!!!!!!!!!!!!\nI mean I got arm11 acess with my "
                "6 copies of freakyforms deluxes and now i want to downgrade to 9.2 and as I have "
                "homebrew I can boot lima3ds but it doesnt boot its Aurora Wright fault, its "
                "incompetent and lazy to not develop for 11 I want downgrader to 9.2 and kernel "
                "exploit quick it's not hard ur the devs do it now quick.\nYou just have to "
                "hack/reprogram/patch the 11.0 FIRM so I can downgrade. Think the comunity. Cmon "
                "your hackers you acn do it. And plilect should make guide safer!!! becuase "
                "evryone bricks!!!!! And lima3ds should add nds rom support native. take notes "
                "Aurora Wright !!!!!!!!!!!!!!I WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI "
                "WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 "
                "DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI "
                "WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 "
                "DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI "
                "WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 "
                "DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!```"
            )
        elif variant == "swotch":
            await ctx.send(
                "```Hey YOU. YES YOU!!!! YOU CAN CREATE A DOWNGRADER. JUST like can Plailect , "
                "Aurora Wright , hedgeberg and SciresM and Daeken work on a Switch 3.0.2 "
                "dongroder!!!!!!!!!!!!!!!!!!!!!!!!!!!\nI mean I got browser acess with my 6 "
                "verzions of teh dns and now i want to downgrade to 3.0.0 and as I have browser I "
                "can boot reswotched but it doesnt boot teh hebrew lawnchair its Aurora Wright "
                "fault, its incompetent and lazy to not develop for 3.0.2 I want dongroder to "
                "3.0.0 and trustzone exploit quick it's not hard ur the devs do it now quick.\nYou"
                " just have to hack/reprogram/patch the 3.0.2 bootrom so I can dongrode. Think "
                "the comunity. Cmon your hackers you acn do it. And plilect should make swotch "
                "gudie safer!!! becuase evryone bricks!!!!! And limaswotch should add wii u rom "
                "support native. take notes Aurora Wright !!!!!!!!!!!!!!I WANT Switch 3.0.2 "
                "DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER "
                "NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT "
                "Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER "
                "NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT "
                "Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER "
                "NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT "
                "Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!```"
            )

    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command(hidden=True)
    async def gnulinux(self, ctx,):
        """GNU/Linux Copy Pasta"""
        await ctx.send("```I'd just like to interject for a moment. What you're referring to as "
                       "Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU"
                       " plus Linux. Linux is not an operating system unto itself, but rather "
                       "another free component of a fully functioning GNU system made useful by "
                       "the GNU corelibs, shell utilities and vital system components comprising "
                       "a full OS as defined by POSIX.\n\nMany computer users run a modified "
                       "version of the GNU system every day, without realizing it. "
                       "Through a peculiar turn of events, the version of GNU which is widely "
                       "used today is often called \"Linux\", and many of its users are not aware "
                       "that it is basically the GNU system, developed by the GNU Project.\n\n"
                       "There really is a Linux, and these people are using it, but it is just a "
                       "part of the system they use. Linux is the kernel: the program in the "
                       "system that allocates the machine's resources to the other programs that "
                       "you run. The kernel is an essential part of an operating system, but "
                       "useless by itself; it can only function in the context of a complete "
                       "operating system. Linux is normally used in combination with the GNU "
                       "operating system: the whole system is basically GNU with Linux added, "
                       "or GNU/Linux. All the so-called \"Linux\" distributions are really "
                       "distributions of GNU/Linux.```")

    
    @commands.command(hidden=True)
    async def kina(self, ctx):
        """Memes."""
        await ctx.send("http://imgur.com/8Mm5ZvB")

    @commands.command(hidden=True)
    async def beepbeep(self, ctx, *, roast: str="Roast"):
        """Bope"""
        roast = await commands.clean_content().convert(ctx, roast)
        await ctx.send("Your {} is ready".format(roast))

    @commands.command(hidden=True)
    async def themes(self, ctx):
        """S a l t"""
        await ctx.send("When it comes to custom theme managers on "
                       "the 3ds there haven't always been that "
                       "many choices\nI can only think of three "
                       "off the top of my head")
                       
    @commands.command()
    async def listmemes(self, ctx): #I can't be bothered to have this update automatically
        """Lists the memes"""
        memes = "```beepbeep\nbirds\nblackalabi\nbrickdurr\nconcern\ndongroder\ndubyadud\ngnulinux\nhelpers\nkina\nlenny\nlisp\nlucina\nlucina2\nmacboy\npbanjo\npermabrocked\nr34\nrip\nrusure\nsoghax\nthemes\nthumbsup\nwhatisr```"
        await ctx.send(memes)


def setup(bot):
    bot.add_cog(Memes(bot))
