
import discord
from discord.commands import Option
intents = discord.Intents.all()
client = discord.Bot(command_prefix="wb:", intents=intents)
# we need to limit the guilds for testing purposes
# so other users wouldn't see the command that we're testing

@client.slash_command(description="Pong!") 
async def ping(ctx):
    await ctx.respond(f"Pong! {round(client.latency*1000, 0)}ms")

async def list_search(ctx: discord.AutocompleteContext):
    return ["1", "2", "3"] # from your database
    
    
@client.slash_command(name="ac_example")
async def autocomplete_example(
    ctx: discord.ApplicationContext,
    choice: Option(str, "what will be your choice!", autocomplete=list_search),
):
    await ctx.respond(f"You picked {choice}!")
client.run("TOKEN")
