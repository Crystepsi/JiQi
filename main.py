from fileinput import filename
import discord
from discord.ext import commands
import os
from bs4 import BeautifulSoup as bs
import requests
import sqlite3

TOKEN = ""

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='++', intents=intents)


@client.event
async def on_ready():
	print(f'Connected to Discord as {client.user}')
	return

@client.event
async def on_member_join(member):
	guild = client.get_guild(937836149592952974)
	channel = guild.get_channel(937836703232716810)

	embedVar = discord.Embed(
		title = f'Welcome to {guild.name}!',
		description = f"We're happy to have you around, {member.mention}",
		color = 0xFFDFD3,
	).set_image(url='https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif')

	await channel.send(embed=embedVar)
	return

@client.event
async def on_member_remove(member):
	guild = client.get_guild(937836149592952974)
	channel = guild.get_channel(988085867925102622)

	embedVar = discord.Embed(
		title = f'Goodbye, {member.mention}!',
		description = f'{guild.name} will miss you (probably)',
		color = 0xFFDFD3,
	).set_image(url='https://c.tenor.com/EZsmE8l33TcAAAAC/anime-anime-cry.gif')

	await channel.send(embed=embedVar)
	return

@client.event
async def on_message(message):
	if message.content.lower().startswith('++jiqi'):
		hello = discord.Embed(
			title = 'Hello!',
			color = 0xFFDFD3
		).set_image(url='https://volta.neocities.org/JiQi/JiQi3.png')

		await message.channel.send(embed=hello)

	if message.content.lower().startswith("++def"):
		word = message.content[6:]
		if word == 'bajillion':
			await message.channel.send('1000 jillion')
			return 
		else:
			url = "https://www.urbandictionary.com/define.php?term=" + word
			url_get = requests.get(url)
			page = bs(url_get.content, "html.parser")
			top = page.find("div", {"class": "meaning mb-4"})

			try:
				await message.channel.send(top.text)
				return
			except AttributeError:
				await message.channel.send("Google it")
				return

	# GET WIKI SUMMARY -- FINISHED
	if message.content.lower().startswith("++wiki"):
		entry = message.content[7:].replace(" ", "_")
		url = "https://en.wikipedia.org/wiki/" + entry
		url_get = requests.get(url)
		page = bs(url_get.content, "html.parser")
		summary = page.find("div", {"class": "mw-parser-output"}).find("p")

		try:
			await message.channel.send(summary.text)
			return
		except:
			await message.channel.send(f'{url}')
			return

client.run(TOKEN)
