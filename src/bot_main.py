# main bot file

import nextcord
import Utils.util
from nextcord.ext import commands

intents = nextcord.Intents.all()

def get_token(user_name):
    file = open(f"src/Tokens/{user_name}", 'r')
    token = file.read()
    return token


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.command_prefix = "~"
        self.user_name = args[1]
        self.description = self.user_name

if __name__ == "__main__":
    bot = Bot(intents=intents)
    token = get_token(bot.user_name)
    print(f"Starting bot {bot.user_name}...")
    bot.run(token)
