import discord
from discord.ext import commands
import json
import os
import time

configFile = 'config.json'

try:
    with open(configFile) as f:
        try:
            token = json.load(f)['token']
        except KeyError:
            print('Broken config file! Missing token in json.\nResetting config file...')
            time.sleep(1)
            token = input('Please enter your token: ')
            with open(configFile, 'w') as f:
                json.dump({'token': token}, f)
except FileNotFoundError:
    token = input('Config file not found! Please enter your token: ')
    with open(configFile, 'w') as f:
        json.dump({'token': token}, f)

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True, help_command=None)

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
async def help(ctx):
    await ctx.send('**-----PC Remote-----**\n\n'
                   '`!shutdown <time>` - Shutdowns the PC in the specified time.\n`' +
                   '!restart <time>` - Restarts the PC in the specified time.\n' +
                   '`!hibernate` - Puts the PC to hibernation (Similar to sleep).\n`' +
                   '!abort` - Aborts the shutdown or restart.'
                   )

try:
    client.run(token)
except discord.errors.LoginFailure:
    token = input('Invalid token! Please enter your valid token: ')
    with open(configFile, 'r') as f:
        config = json.load(f)
    config['token'] = token
    with open(configFile, 'w') as f:
        json.dump(config, f)
    print("Token updated! Restarting...")
    os.system(f'python {__file__}')