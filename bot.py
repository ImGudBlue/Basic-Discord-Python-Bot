import discord
from discord.ext import commands

# Change Discord Bot Prefix, disable default help command
client = commands.Bot(command_prefix="-", help_command=None)

@client.event
async def on_ready():
    # Change Discord Bot status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Hello!"))
    # Print a message when the bot loaded
    print("Bot is ready!")

# Hello Command
@client.command()
async def hello(ctx):
    await ctx.send("Hey, Python!")

# Help command
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "type -help <command> to view the command usage.")

    em.add_field(name = "Basic commands", value = "hello")

    await ctx.send(embed = em)

# The "Hello" command usage
@help.command()
async def hello (ctx):

    em = discord.Embed(title = "Hello Usage", description = "uhh.. i mean just hello?")

    await ctx.send(embed = em)

# Type your discord bot token, get one from https://discord.com/developers/applications
client.run("YOUR BOT TOKEN")
