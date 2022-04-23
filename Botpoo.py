import discord
from click import pass_context
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands.context import Context
from argparse import ArgumentParser, Namespace
from log import Log
import argparse
import json

class Botpoo(Bot):

	def __init__(self, config):
		super().__init__(str(config['préfixe']))
		
		self.add_cog(commandes(self))
		self.add_cog(Log(self, config))

	async def on_ready(self):
		print(f'{self.user} est connecté(e) a Discord!')


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="config file", required=True, dest="config"
    )
    return parser.parse_args()

def get_config(config_file: str)-> dict:

    with open(config_file, "r") as f:

        config = json.load(f)

    return config

def main():
	args = get_args()
	config = json.load(open(args.config))
	Client = Botpoo(config)
	Client.run(str(config['token']))

class commandes(commands.Cog):
	
	def __init__(self, Client) -> None:
		super().__init__()
		self.Client = Client


	@commands.command(name="bonjour", pass_context=True)
	async def temps(self, ctx):
		msg = f"{ctx.message.author.name} a dit " + str(ctx.message.content)
		Log.infoLog(msg)
		await ctx.send("Hello :)")


	@commands.command(name="help", pass_context=True)
	async def HELP(self, ctx):
		msg = f"{ctx.message.author.name} a dit " + str(ctx.message.content)
		Log.infoLog(msg)
		await ctx.send("les commandes possibles sont : help")

async def on_message(self,message):
            
    if message.author == self.user:
        with open("botlog.txt", "a") as L :
            L.write( self.now +"message"+ message.content)
          

if __name__ == "__main__":
	main()

