from termcolor import colored
import os


class Colors:
	r = colored("red")
	b = colored("blue")
	g = colored("green")
	end = colored("white")





def Start():

	print(colored("""
  _____           _  __   __                
 |  __ \         (_) \ \ / /                
 | |__) | __ ___  _   \ V / ___ _ __   ___  
 |  ___/ '__/ _ \| |   > < / _ \ '_ \ / _ \ 
 | |   | | | (_) | |  / . \  __/ | | | (_) |
 |_|   |_|  \___/| | /_/ \_\___|_| |_|\___/ 
                _/ |        bootloader                
               |__/                         

	""", "red"))
	install = input("Would you like to install the required modules? Y/N: ")
	if install == "Y":
		print(colored("Installing", "blue"))
		os.system("pip install discord_webhook discord.py colorama")
		print(colored("[*] Done!", "green"))
	else:
			print("Okay, skipping...")
			pass
		
	print("Starting up... Make sure you have the bot.py in the Main folder!")
	os.system("python bot.py");
Start()
