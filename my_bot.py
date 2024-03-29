# import discord package 
import os
import discord
from dotenv import load_dotenv
# Client (bot)
client = discord.Client()

@client.event
async def on_ready():
# Functionality
  general_channel = client.get_channel(878219278376124421)

  await general_channel.send('Testing Announcements!')

@client.event
async def on_message(message):
  
  if message.content == 'what is the version':
    general_channel = client.get_channel(878219278376124421)

    myEmbed = discord.Embed(title='Current Version', description='The bot is in version 1.0', color=0x00ff00,)
    myEmbed.add_field(name='Version Code',value='v1.0',inline=False)
    myEmbed.add_field(name='Date Released', value='20/08/21', inline=False)
    myEmbed.set_footer(text='This is a sample footer')
    myEmbed.set_author(name='Temi')

    await general_channel.send(embed=myEmbed)

# Run Client on Server 
load_dotenv('Token.env')
TOKEN = os.getenv('DISCORD_TOKEN')
Token.env;

client.run(os.getenv('TOKEN'))


