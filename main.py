###################################################################

from logging import exception
from click import pass_context
from arrays import headpats
from arrays import slaps
from arrays import ew
from bot_token import TOKEN
from minion_memes import minion_meme
from helpmsg import help_msg

# DISCORD LIBRARIES
import discord
from discord.ext import commands
from discord.utils import get
from core import ready
from core import join

# NEEDED FOR WEB SCRAPING
from bs4 import BeautifulSoup as bs
import requests

# GENERAL
from random import randint

# FOR PLAYING AUDIO (TTS)
from playsound import playsound as play
import gtts
import json
from browser_history import get_history
from browser_history.browsers import Safari

# FOR TRANSLATOR
from googletrans import Translator

###################################################################

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='++', intents=intents)
client.add_cog(ready(client))

translator = Translator()

json_file = open('/Users/ashton/Documents/Discordのボット/JiQi/dabloons.json', 'r') # open the json file
dabloons_data = json.load(json_file) # set up a dictionary

###################################################################

@client.event
async def on_member_join(member):
	guild = client.get_guild(937836149592952974)
	channel = guild.get_channel(937836703232716810)
	general = guild.get_channel(937836150574432260)

	embedVar = discord.Embed(
		title = f'Welcome to {guild.name}!',
		description = f"We're happy to have you around, {member.mention}",
		color = 0xFFDFD3,
	).set_image(url='https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif')

	await channel.send(embed=embedVar)
	await general.send('Ayup lad')
	return

###################################################################

@client.event
async def on_member_remove(member):
	guild = client.get_guild(937836149592952974)
	channel = guild.get_channel(988085867925102622)

	embedVar = discord.Embed(
		title = f'Goodbye, {member.name}!',
		description = f'{guild.name} will miss you (probably)',
		color = 0xFFDFD3,
	).set_image(url='https://c.tenor.com/EZsmE8l33TcAAAAC/anime-anime-cry.gif')

	await channel.send(embed=embedVar)
	return

###################################################################

@client.event
async def on_raw_reaction_add(payload):
	guild = client.get_guild(payload.guild_id)
	member = guild.get_member(payload.user_id)

	# COLOURS
	if payload.message_id == 994307237902303373:
		if payload.emoji.name == '🔴':
			role = discord.utils.get(guild.roles, name='Red')
			await member.add_roles(role)
		if payload.emoji.name == '🟠':
			role = discord.utils.get(guild.roles, name='Orange')
			await member.add_roles(role)			 
		if payload.emoji.name == '🟡':
			role = discord.utils.get(guild.roles, name='Yellow')
			await member.add_roles(role)			 
		if payload.emoji.name == '🟢':
			role = discord.utils.get(guild.roles, name='Green')
			await member.add_roles(role)
		if payload.emoji.name == '🔵':
			role = discord.utils.get(guild.roles, name='Blue')
			await member.add_roles(role)
		if payload.emoji.name == '🟣':
			role = discord.utils.get(guild.roles, name='Purple')
			await member.add_roles(role)			 
		if payload.emoji.name == 'osu':
			role = discord.utils.get(guild.roles, name='Pink')
			await member.add_roles(role)			 
		if payload.emoji.name == '🟤':
			role = discord.utils.get(guild.roles, name='Brown')
			await member.add_roles(role)			 
		if payload.emoji.name == 'black':
			role = discord.utils.get(guild.roles, name='Black')
			await member.add_roles(role)			 
		if payload.emoji.name == 'white':
			role = discord.utils.get(guild.roles, name='White')
			await member.add_roles(role)
			
	# PLATFORM
	if payload.message_id == 994368484148523159:
		if payload.emoji.name == '🔴':
			role = discord.utils.get(guild.roles, name='xbox')
			await member.add_roles(role)
		if payload.emoji.name == '🟠':
			role = discord.utils.get(guild.roles, name='Playstation')
			await member.add_roles(role)
		if payload.emoji.name == '🟡':
			role = discord.utils.get(guild.roles, name='Switch')
			await member.add_roles(role)
		if payload.emoji.name == '🟢':
			role = discord.utils.get(guild.roles, name='Wii')
			await member.add_roles(role)
		if payload.emoji.name == '🔵':
			role = discord.utils.get(guild.roles, name='Mobile')
			await member.add_roles(role)
		if payload.emoji.name == '🟣':
			role = discord.utils.get(guild.roles, name='Windows')
			await member.add_roles(role)
		if payload.emoji.name == 'black':
			role = discord.utils.get(guild.roles, name='Mac')
			await member.add_roles(role)
		if payload.emoji.name == 'white':
			role = discord.utils.get(guild.roles, name='Linux')
			await member.add_roles(role)

	# ORIGIN
	if payload.message_id == 988096225716879500:
		if payload.emoji.name == '🔴':
			role = discord.utils.get(guild.roles, name='IRL')
			await member.add_roles(role)
		if payload.emoji.name == '🟠':
			role = discord.utils.get(guild.roles, name='From Website')
			await member.add_roles(role)
		if payload.emoji.name == '🟡':
			role = discord.utils.get(guild.roles, name='From MSP')
			await member.add_roles(role)

	# GAMES
	if payload.message_id == 988093682748117084:
		if payload.emoji.name == 'osu':
			role = discord.utils.get(guild.roles, name='Osu!')
			await member.add_roles(role)
		if payload.emoji.name == 'runescrape':
			role = discord.utils.get(guild.roles, name='Runescape')
			await member.add_roles(role)
		if payload.emoji.name == 'minecraft':
			role = discord.utils.get(guild.roles, name='Minecraft')
			await member.add_roles(role)
		if payload.emoji.name == 'csgo':
			role = discord.utils.get(guild.roles, name='CSGO')
			await member.add_roles(role)
		if payload.emoji.name == 'msp':
			role = discord.utils.get(guild.roles, name='MSP')
			await member.add_roles(role)
		if payload.emoji.name == 'fortnite':
			role = discord.utils.get(guild.roles, name='Fortnite')
			await member.add_roles(role)
		if payload.emoji.name == 'project_diva':
			role = discord.utils.get(guild.roles, name='Project Diva')
			await member.add_roles(role)
		if payload.emoji.name == 'league':
			role = discord.utils.get(guild.roles, name='League of Legends')
			await member.add_roles(role)
		if payload.emoji.name == 'genshin':
			role = discord.utils.get(guild.roles, name='Genshin Impact')
			await member.add_roles(role)
		if payload.emoji.name == 'beatsaber':
			role = discord.utils.get(guild.roles, name='Beatsaber')
			await member.add_roles(role)
		if payload.emoji.name == 'mariokart':
			role = discord.utils.get(guild.roles, name='Mario Kart')
			await member.add_roles(role)
		if payload.emoji.name == 'duolingo':
			role = discord.utils.get(guild.roles, name='Duolingo')
			await member.add_roles(role)
		if payload.emoji.name == 'fifa':
			role = discord.utils.get(guild.roles, name='Fifa')
			await member.add_roles(role)

	# DM STATUS
	if payload.message_id == 988091162432786502:
		if payload.emoji.name == '🔴':
			role = discord.utils.get(guild.roles, name='DMs Open')
			await member.add_roles(role)
		if payload.emoji.name == '🟠':
			role = discord.utils.get(guild.roles, name='DMs Closed')
			await member.add_roles(role)

	# PRONOUNS
	if payload.message_id == 988089810650554388:
		if payload.emoji.name == '🔴':
			role = discord.utils.get(guild.roles, name='He/Him')
			await member.add_roles(role)
		if payload.emoji.name == '🟠':
			role = discord.utils.get(guild.roles, name='She/Her')
			await member.add_roles(role)
		if payload.emoji.name == '🟡':
			role = discord.utils.get(guild.roles, name='They/Them')
			await member.add_roles(role)
		if payload.emoji.name == '🟢':
			role = discord.utils.get(guild.roles, name='She/They')
			await member.add_roles(role)
		if payload.emoji.name == '🔵':
			role = discord.utils.get(guild.roles, name='He/They')
			await member.add_roles(role)
		if payload.emoji.name == '🟣':
			role = discord.utils.get(guild.roles, name='Any Pronouns')
			await member.add_roles(role)
		if payload.emoji.name == '🟤':
			role = discord.utils.get(guild.roles, name='Ask About Pronouns')
			await member.add_roles(role)


###################################################################

@client.event
async def on_message(message):

	if message.author == client.user:
		return

	###################################################################

	# HELP
	if message.content.lower().startswith('++help'):
		await message.channel.send(embed=discord.Embed(
			color = 0xFFDFD3,
			description = help_msg
		))

	###################################################################

	# DABLOONS
	if message.author.name not in dabloons_data:
		dabloons_data[message.author.name] = 1
		with open('dabloons.json', 'w') as f:
			json.dump(dabloons_data, f) # write to the dictionary
	else:
		dabloons_data[message.author.name] = dabloons_data[message.author.name] + 1
		with open('dabloons.json', 'w') as f:
			json.dump(dabloons_data, f) # write to the dictionary


	if message.content.lower() == '++dabloons':
		await message.channel.send(f'You have {str(dabloons_data[message.author.name])}! So shiny......')
		return

	if message.content.lower() == '++history':
		await message.channel.send(get_history().histories[0])
		return

	###################################################################

	if message.content.lower().startswith('++rick'):
		await message.channel.send(file = discord.File('/Users/ashton/Documents/Discordのボット/JiQi/Discord/videos/1.mp4'))
		return

	###################################################################

	# random chance that jiqi will just tell the person to shut up

	number = randint(1, 1000)

	if number == 69:
		await message.channel.send('Shut up')
		return

	if number == 420:
		await message.channel.send(embed = discord.Embed(
			color = 0xFFDFD3
		).set_image(url='https://i.imgur.com/wmdOOzG.png'))

	###################################################################

	#if message.content.lower().startswith('++dm'):
	#	target = client.get_user(int(message.content.split(' ')[1]))
	#	msg = message.content.split(' ')[2:]
#
#		msg_spaced = []
#		for i in range(0, len(msg)):
#			msg_spaced.append(msg[i] + ' ')
#		text = ''.join(msg_spaced)

#		await target.send(text)
#		return

	###################################################################

#	if '@695626968233934971' in message.content.lower():
#		say = gtts.gTTS(text=message.content.replace('<@695626968233934971>', ' '))
#		say.save('tts.mp3')
#		play('tts.mp3')

	###################################################################

	if message.content.lower().startswith('++jiqi'):
		hello = discord.Embed(
			title = 'Hello!',
			color = 0xFFDFD3
		).set_image(url='https://volta.neocities.org/JiQi/JiQi3.png')

		await message.channel.send(embed=hello)

	###################################################################

	# URBAN DICTIONARY GRAB -- FINISHED 
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
				await message.channel.send('google it')
				return

	###################################################################

	# GET WIKI SUMMARY -- FUNCTIONAL
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

	###################################################################

	# WHISPER -- FINSISHED
	if message.content.lower().startswith('++whisper'):
		whisper = message.content[10:]

		guild = client.get_guild(937836149592952974)
		channel = guild.get_channel(988442097222828032)

		embedded = discord.Embed(
			title = 'Someone whispered:',
			description = whisper,
			color = 0xFFDFD3
		)

		if '@everyone' not in whisper:
			await channel.send(embed=embedded)

		print(f'{message.author} whispered {whisper}')
		return

	###################################################################

	# JIQI SAYS -- FINISHED
	if message.content.lower().startswith('++say'):
		jiqi_says = message.content[5:]

		guild = client.get_guild(937836149592952974)
		channel = guild.get_channel(988442097222828032)

		embedded = discord.Embed(
			title = 'JiQi says:',
			description = jiqi_says,
			color = 0xFFDFD3
		).set_image(url='https://volta.neocities.org/JiQi/JiQi3.png')

		if '@everyone' not in jiqi_says:
			await channel.send(embed=embedded)

		print(f'{message.author} says {jiqi_says}')
		return

	###################################################################

	# SHOW -- FINISHED
	if message.content.lower().startswith('++show'):
		image_url = message.content[6:]

		guild = client.get_guild(937836149592952974)
		channel = guild.get_channel(988442097222828032)

		embedded = discord.Embed(
			color = 0xFFDFD3
		).set_image(url=image_url)

		await channel.send(embed=embedded)
		return

	###################################################################


	###################################################################

	# PORN -- FINISHED
	if message.content.lower().startswith('++r34'):
		req = message.content[6:]

		if ' ' in req:
			req = req.replace(' ', '_')

		url = 'https://rule34.xxx/index.php?page=post&s=list&tags=' + req
		url_get = requests.get(url)
		page = bs(url_get.content, "html.parser")
		img_tags = page.find_all('img', {'class' : 'preview'})

		rand_image = img_tags[randint(0, len(img_tags)-1)]

		guild = client.get_guild(937836149592952974)
		channel = guild.get_channel(994058926641385565)

		try:
			await channel.send(embed=discord.Embed(
				color = 0xFFDFD3
			).set_image(url=rand_image['src']))
		except:
			await channel.send(embed=discord.Embed(
				color = 0xFFDFD3,
				description = "That tag doesn't exist, try another one (;"
			))

		for i in ew:
			if str(i) in message.content.lower():
				await channel.send(embed=discord.Embed(
					color = 0xFFDFD3
				).set_image(url='https://c.tenor.com/G_p24OxHrC8AAAAC/my-honest-reaction-my-reactioj.gif'))

	###################################################################

	# HEADPATS -- FINISHED
	if message.content.lower().startswith('++pat'):
		gif = headpats[randint(0, len(headpats)-1)]
		if '@everyone' in message.content.lower():
			await message.channel.send(embed = discord.Embed(
				color = 0xFFDFD3,
				description = f'{str(message.author).split("#")[0]} headpats everyone'
			).set_image(url=gif))
		else:
			await message.channel.send(embed = discord.Embed(
				color = 0xFFDFD3,
				description = f'{str(message.author).split("#")[0]} headpats {message.content[5:]}'
			).set_image(url=gif))

	###################################################################

	# SLAPS -- FINISHED
	if message.content.lower().startswith('++slap'):
		gif = slaps[randint(0, len(slaps)-1)]
		if '@everyone' in message.content.lower():
			await message.channel.send(embed = discord.Embed(
				color = 0xFFDFD3,
				description = f'{str(message.author).split("#")[0]} slaps everyone'
			).set_image(url=gif))
		else:
			await message.channel.send(embed = discord.Embed(
				color = 0xFFDFD3,
				description = f'{str(message.author).split("#")[0]} slaps {message.content[6:]}'
			).set_image(url=gif))

	###################################################################

	# MINION MEMES -- FINISHED
	if message.content.lower().startswith('++minion'):
		url_get = requests.get('https://www.pinterest.co.uk/happyjose19/minion-meme/')
		page = bs(url_get.content, "html.parser")
		memes = page.find_all('img', {'class' : 'hCL kVc L4E MIw'})

		minion_meme = memes[randint(0, len(memes)-1)]['src']

		await message.channel.send(embed = discord.Embed(
			color = 0xFFDFD3
		).set_image(url=minion_meme))

	###################################################################

	# TRANSLATE -- UNFINISHED
	if message.content.lower().startswith('++translate'):
		text = message.content[12:]
		lang_detect = translator.detect(text).lang
		await message.channel.send(embed = discord.Embed(
			color = 0xFFDFD3,
			title = translator.translate(text).text,
			description = f'Translated from {lang_detect}'
		))
		return

	###################################################################

	# IF IN
	if 'virgin' in message.content.lower():
		await message.channel.send(embed=discord.Embed(
			color = 0xFFDFD3
		).set_image(url='https://bettwslifehouse.org.uk/images/gallery/Arthog%20-%2035bf3e49801f35.JPG'))

	if 'uwu' in message.content.lower():
		await message.channel.send(embed=discord.Embed(
			description = 'Cringe',
			color = 0xFFDFD3
		))
	if 'owo' in message.content.lower():
		await message.channel.send(embed=discord.Embed(
			description = 'Cringe',
			color = 0xFFDFD3
		))

	if 'whore' in message.content.lower():
		await message.channel.send(embed=discord.Embed(
			description = '@❤ 𝖘𝖆𝖙𝖆𝖓 ❤#2127',
			color = 0xFFDFD3
		))

	###################################################################

client.run(TOKEN)