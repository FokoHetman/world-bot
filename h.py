import discord
from discord.ext import commands
client=discord.Client(command_prefix=".", intents=discord.Intents.all())
chosen_one=1070351025271218207

@client.event
async def on_message(msg):
    if int(msg.channel.id)==int(chosen_one):
        for i in msg.content:
            if i.lower() != "h":
                await msg.delete()
                return
client.run("OTc5MTAyOTA5MTE3NjU3MTY4.GpvQ5J.2eX9vXqdcY822TnM-T-jG1dGGT_2K14MWY6P8Q")