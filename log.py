from discord.ext import commands
import logging

class Log(commands.Cog):

	def __init__(self, bot, config) -> None:
		super().__init__()
		self.bot = bot
		self.setupLog(config)


	def setupLog(self, config):
		log_format = str(config['log_format'])
		log_date = str(config['log_date'])
		botlog = str(config['botlog'])

		logging.basicConfig(filename=botlog,format=log_format, level=logging.INFO)
