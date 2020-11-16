aimport colorama, discord_webhook, discord
from colorama import Fore
from discord_webhook import DiscordWebhook
import requests
import socket
from discord.ext import commands
colorama.init()

bot = commands.Bot(command_prefix="azs")



def webhooknotify():
	webhook = DiscordWebhook(url="https://discord.com/api/webhooks/", username="AZS Bootloader", content="I am alive! Prefix: azs, by raz")
	resp = webhook.execute()
@bot.event
async def on_ready():
	print("[" + Fore.GREEN + "CLIENT" + Fore.WHITE + f"] Logged in as AZS#9191")
	
	
		
webhooknotify()
print("Sent out notification")
bot.run('')

