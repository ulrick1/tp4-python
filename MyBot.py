
import discord

default_intents = discord.Intents.default()
default_intents.members= True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()

        for each_message in messages:
            await each_message.delete()

@client.event
async def on_member_join(member):
   general_channel: discord.TextChannel = client.get_channel(959351198476038187)
   await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

@client.event
async def on_message(message):
    if message.content.lower() == "quoi":
        await message.channel.send("de neuf")

client.run("OTU5MzUwNDgyNzU1ODEzNDE2.Ykamwg._E608jgq3sLcsmIz1p713neXkF4")

