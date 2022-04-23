
import discord

default_intents = discord.Intents.default()
default_intents.members= True
client = discord.Client(intents=default_intents)

token ="OTY2OTU3ODA0OTEwOTU2NTk0.YmJToQ.KevPommn3dFeX0B0qBxdDwa6Z2A"

@client.event
async def on_ready():
    print("Le bot est prêt !")



client.run(token)
