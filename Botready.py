import discord
import numpy

default_intents = discord.Intents.default()
default_intents.members= True
client = discord.Client(intents=default_intents)
token="OTU5MzUwNDgyNzU1ODEzNDE2.Ykamwg._E608jgq3sLcsmIz1p713neXkF4"

class Botready(discord.Client) :

    async def on_ready():
        print("Le bot est prêt !")

Client=Botready
Client.run(token)
