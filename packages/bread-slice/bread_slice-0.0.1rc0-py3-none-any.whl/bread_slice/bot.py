import os

import hikari
import lightbulb
import miru


class Bot(lightbulb.BotApp):
    def __init__(self) -> None: 
        super().__init__(
            token=os.environ["TOKEN"], 
            prefix="!", 
            help_slash_command=True, 
            delete_unbound_commands=False, 
            case_insensitive_prefix_commands=True, 
            intents=(
                hikari.Intents.MESSAGE_CONTENT |
                hikari.Intents.GUILD_MESSAGES | 
                hikari.Intents.GUILD_MESSAGE_REACTIONS)
        )