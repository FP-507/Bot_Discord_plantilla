import asyncio
from discord.ext import commands
from .config import DISCORD_TOKEN, PREFIX
from .db import ensure_db

import discord

intents = discord.Intents.default()
intents.members = True          # Si quieres acceder a miembros
intents.message_content = True  # Si quieres leer mensajes

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    print("Comandos cargados:", [cmd.name for cmd in bot.commands])

def main():
    loop = asyncio.get_event_loop()
    ensure_db(loop)  # Inicializa DB
    loop.run_until_complete(bot.load_extension("bot.cogs.general"))
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()
