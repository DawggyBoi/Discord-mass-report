import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from time import strftime, gmtime

colorama.init()
sent = 0
b = Style.BRIGHT
os.system('cls' if os.name == 'nt' else 'clear')

ctypes.windll.kernel32.SetConsoleTitleW("[REPORT BOT] Developed By acceleration.back")

# Banner
print(f"""{b+Fore.BLUE}
    ___                  __                __          ____                        __     
   /   | _____________  / /__  _________ _/ /____     / __ \___  ____  ____  _____/ /_____
  / /| |/ ___/ ___/ _ \/ / _ \/ ___/ __ `/ __/ _ \   / /_/ / _ \/ __ \/ __ \/ ___/ __/_  /
 / ___ / /__/ /__/  __/ /  __/ /  / /_/ / /_/  __/  / _, _/  __/ /_/ / /_/ / /  / /_  / /_
/_/  |_\___/\___/\___/_/\___/_/   \__,_/\__/\___/  /_/ |_|\___/ .___/\____/_/   \__/ /___/
                                                             /_/                          
                            Developed By acceleration.back
""")

# Report Type Selection
print(f"""{b+Fore.CYAN} > {Fore.RESET}Select Report Type:
{b+Fore.GREEN} 1 {Fore.RESET}Server Report
{b+Fore.GREEN} 2 {Fore.RESET}DMs Report (Coming in Version 2.0)
""")

report_type = input(f"{b+Fore.BLUE} > Type (1/2){Fore.RESET}: ")

if report_type not in ['1', '2']:
    print(f"{Fore.RED} [!] Invalid selection. Please restart and choose 1 or 2.")
    exit()

if report_type == '1':
    guild_id = input(f"{b+Fore.BLUE} > Server ID{Fore.RESET}: ")
    channel_id = input(f"{b+Fore.BLUE} > Channel ID{Fore.RESET}: ")
    message_id = input(f"{b+Fore.BLUE} > Message ID{Fore.RESET}: ")
else:
    guild_id = None
    channel_id = None
    message_id = input(f"{b+Fore.BLUE} > Message ID{Fore.RESET}: ")

# Reason menu
print(f"""{b+Fore.CYAN} > {Fore.RESET}Report Reason:
{b+Fore.GREEN} 1 {Fore.RESET}Illegal Content
{b+Fore.GREEN} 2 {Fore.RESET}Harassment
{b+Fore.GREEN} 3 {Fore.RESET}Spam or Phishing Links
{b+Fore.GREEN} 4 {Fore.RESET}Self harm
""")

reason = input(f"{b+Fore.BLUE} > Option (1-4){Fore.RESET}: ")

try:
    with open('tokens.txt', 'r') as file:
        tokens = [line.strip() for line in file if line.strip()]
    if not tokens:
        print(f"{Fore.RED}[!] tokens.txt is empty.")
        exit()
except FileNotFoundError:
    print(f"{Fore.RED}[!] tokens.txt not found.")
    exit()

def report_message(token):
    global sent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    payload = {
        'message_id': message_id,
        'reason': reason
    }

    if guild_id:
        payload['guild_id'] = guild_id
    if channel_id:
        payload['channel_id'] = channel_id

    while True:
        try:
            r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
            timestamp = strftime("%H:%M:%S", gmtime())
            if r.status_code == 201:
                print(f"{Fore.GREEN}[{timestamp}] > Sent Report :: Message ID: {message_id}")
                sent += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] Developed By acceleration.back | Sent: {sent}")
            elif r.status_code == 401:
                print(f"{Fore.RED}[{timestamp}] > Invalid Token")
                break
            else:
                print(f"{Fore.YELLOW}[{timestamp}] > Error Code {r.status_code}")
        except Exception as e:
            print(f"{Fore.RED}[!] Exception: {e}")
            break

# Threaded token execution
for token in tokens:
    for _ in range(2):
        Thread(target=report_message, args=(token,)).start()
npm start