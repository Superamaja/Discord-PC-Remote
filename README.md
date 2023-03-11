# Discord PC Remote

Discord PC Remote is a Python program that enables you to access your PC's power remotely using Discord. With Discord PC Remote, you can easily shut down, restart, or put your PC to hibernation via Discord commands.

## Features

-   Remotely access your PC's power.
-   Uses Discord to send and receive commands.
-   Option to automatically start the program with Windows.

## Commands

Here are the available commands that you can use with Discord PC Remote:

-   `!help` - Brings up the command list.
-   `!abort` - Aborts the shutdown or restart.
-   `!shutdown <time>` - Shuts down the PC in the specified time.
-   `!restart <time>` - Restarts the PC in the specified time.
-   `!hibernate` - Puts the PC to hibernation (similar to sleep).

Note: The time specified in the !shutdown and !restart commands should be in seconds.

## Activating/Deactivating Startup with Windows

Run the `startup-config.py` file and follow the directions. It will place a shortcut in shell:startup targeting the `main (no-console).pyw`. Make sure you rerun this file if the program's directory is changed.

## No Console Mode

After a successful setup and verifying that there are no bugs, you have the bot running in the background without a console. Just run the `main.py (no-console).pyw` file instead!

## How to Set Up/Install

To set up Discord PC Remote, follow these steps:

1. Create a bot on the [Discord Developer page](https://discord.com/developers/applications).
2. Enter your bot's token in the `config.json` file and configure the bot to your liking.
    ```json
    {
        "token": "TOKEN HERE",
        "prefix": "!"
    }
    ```
3. Enable all `Gateway Intents` in the "Bot" tab.
4. Invite your bot using this link: https://discord.com/api/oauth2/authorize?client_id=CLIENTID&permissions=8&scope=applications.commands%20bot

    - Replace `CLIENTID` with the ID of your bot.
    - Invite this bot to a server with only you.

5. Install the required libraries by running this command in the same directory as the program:
    ```batch
     pip install -r requirements
    ```
