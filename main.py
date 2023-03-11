import discord
from discord.ext import commands
import json
import os

configFile = 'config.json'

try:
    with open(configFile) as f:
        try:
            # Check to see if json has everything
            config = json.load(f)
            token = config['token']
            prefix = config['prefix']
        except KeyError:
            print('Config file is missing some values! Please check the README.md or GitHub for the config template.')
            input('Press enter to exit...')
            exit()
except FileNotFoundError:
    print(f'{configFile} not found!')
    input('Press enter to exit...')
    exit()

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    print('PC Remote is online!')

@client.command()
async def abort(ctx):
    returnCode = os.system('shutdown -a')
    if returnCode == 0:
        await ctx.send('Action aborted!')
    elif returnCode == 1116:
        await ctx.send('No shutdown is currently in progress.')
    else:
        await ctx.send(f'An error occurred while aborting the shutdown. Code returned: `{returnCode}`. Check the console for more information.')

@client.command()
async def shutdown(ctx, *args):
    if len(args) == 0:
        await ctx.send('Please enter a shutdown time. For an instant shutdown, enter `0`.')
    else:
        try:
            int(args[0]) # Check if the argument is a number
            os.system(f'shutdown -s -t {args[0]}')
            await ctx.send(f'Shutting down in {args[0]} seconds.')
        except ValueError:
            await ctx.send('Please enter a valid number. Use `!help` for more information.')

@client.command()
async def restart(ctx, *args):
    if len(args) == 0:
        await ctx.send('Please enter a restart time. For an instant restart, enter `0`.')
    else:
        os.system(f'shutdown -r -t {args[0]}')
        await ctx.send(f'Restarting in {args[0]} seconds.')

@client.command(aliases=['sleep'])
async def hibernate(ctx, *args):
    await ctx.send('PC has been put to sleep.')
    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

@client.command()
async def stop(ctx):
    await ctx.send('PC Remote is shutting down...')
    await client.close()

@client.command()
async def help(ctx):
    await ctx.send('**-----PC Remote-----**\n\n'
                    '`!shutdown <time>` - Shutdowns the PC in the specified time.\n`' +
                    '!restart <time>` - Restarts the PC in the specified time.\n' +
                    '`!hibernate` - Puts the PC to hibernation (Similar to sleep).\n`' +
                    '!abort` - Aborts the shutdown or restart.\n' +
                    '`!stop` - Stops the bot.\n'
                   )

try:
    client.run(token)
except discord.errors.LoginFailure:
    ('Invalid token! Please enter a valid token in the config file.')