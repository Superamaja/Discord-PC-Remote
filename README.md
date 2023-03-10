# PC Remote Discord

PC Remote Discord is a simple Python program that allows you to remotely access your PC's power using Discord. With this program, you can easily shutdown, restart, or put your PC to hibernation through Discord commands.

## Features

- Remotely access your PC's power.
- Uses Discord to send and receive commands.
- Optional startup with Windows. (Coming Soon!)

## Commands

Here are the available commands that you can use with PC Remote Discord:

- `!help` - Brings up the command list.
- `!abort` - Aborts the shutdown or restart.
- `!shutdown <time>` - Shuts down the PC in the specified time.
- `!restart <time>` - Restarts the PC in the specified time.
- `!hibernate` - Puts the PC to hibernation (similar to sleep).

## How to Set Up/Install

To set up PC Remote Discord, follow these steps:

1. First, set your Discord bot's token in the `config.json` file.
   ```json
   {
       "token": "TOKEN HERE"
   }
2. Create a bot on the [Discord Developer page](https://discord.com/developers/applications).
3. Enable all `Gateway Intents` in the "Bot" tab.
4. Invite your bot using this link: https://discord.com/api/oauth2/authorize?client_id=CLIENTID&permissions=8&scope=applications.commands%20bot
    * Replace `CLIENTID` with the ID of your bot.
    * I recommend inviting this bot to a private server with only you.

5. Install the required libraries by running the following command in the same directory as the program:
   ```batch
   pip install -r requirements
   ```
