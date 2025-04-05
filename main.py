import discord
from discord.ext import commands
import os
from commands import (
    intro, analyse, accumuleer, alert, dagelijks,
    setexchange, setfee, signal, smartanalyse, simulate
)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is klaar als {bot.user}")

# Add all cogs
async def setup():
    await bot.add_cog(intro.Intro(bot))
    await bot.add_cog(analyse.Analyse(bot))
    await bot.add_cog(accumuleer.Accumuleer(bot))
    await bot.add_cog(alert.Alert(bot))
    await bot.add_cog(dagelijks.Dagelijks(bot))
    await bot.add_cog(setexchange.SetExchange(bot))
    await bot.add_cog(setfee.SetFee(bot))
    await bot.add_cog(signal.Signal(bot))
    await bot.add_cog(smartanalyse.SmartAnalyse(bot))
    await bot.add_cog(simulate.Simulate(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands gesynchroniseerd: {len(synced)}")
    except Exception as e:
        print(e)

bot.loop.create_task(setup())
bot.run(os.getenv("DISCORD_TOKEN"))
