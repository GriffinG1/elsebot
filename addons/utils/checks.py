from discord.ext.commands import check


def is_owner():
    return check((lambda ctx: ctx.bot.owner_role in ctx.message.author.roles))


def is_botdev():
    return check((lambda ctx: ctx.bot.botdev_role in ctx.message.author.roles or ctx.bot.owner_role in ctx.message.author.roles))
