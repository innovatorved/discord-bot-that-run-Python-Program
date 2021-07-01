import os
import discord

client = discord.Client()

@client.event
async def on_ready():
	""" automatic execute whwn you loged in to the system"""
	print("We have logged in a {0.user}".format(client))

@client.event
async def on_message(message):
	"""Recieve msg to Discord and send Message"""
	if message.author == client.user:
		"""return nothing if msg is send by itself"""
		return
	# print(message.content)
	
	if message.content.lower().startswith("hello"):
		"""Send Hello to the channel if anybody say hello"""
		await message.channel.send("Hello I am Bot")


if __name__ == "__main__":
	my_secret = os.environ['token']  # enter your token here
	client.run(my_secret)