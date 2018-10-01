from json import load, dump

class Reejoin:
    """
    automatically approve people when they join
    """

    def __init__(self, bot):
        self.bot = bot
        try:
            with open("database/reejoin.json", "r") as config:
                self.config = load(config)

        except FileNotFoundError:
            self.config = {
                "users": [],
            }

            with open("database/reejoin.json", "w") as config:
                dump(self.config, config, indent=4,
                     sort_keys=True, separators=(',', ':'))

    async def on_member_join(self, member):
        if member.id in self.config['users']:
            await member.add_roles(self.bot.approved_role)
            self.config['users'].remove(member.id)

            with open("database/reejoin.json", "w") as config:
                dump(self.config, config, indent=4,
                     sort_keys=True, separators=(',', ':'))

    async def on_member_remove(self, member):
        if self.bot.approved_role in member.roles:
            self.config['users'].append(member.id)

            with open("database/reejoin.json", "w") as config:
                dump(self.config, config, indent=4,
                     sort_keys=True, separators=(',', ':'))

def setup(bot):
    bot.add_cog(Reejoin(bot))
