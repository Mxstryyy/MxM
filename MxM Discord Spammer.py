import requests
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Password for access
PASSWORD = "MxM Tools"  # Replace this with your desired password

# Function for password verification
def check_password():
    attempts = 3  # Number of attempts
    for _ in range(attempts):
        entered_password = input("Please enter your password: ").strip()
        if entered_password == PASSWORD:
            print(Fore.GREEN + "Password correct. Access granted.\n")
            return True
        else:
            print(Fore.RED + "Incorrect password. Please try again.\n")
    print(Fore.YELLOW + "Too many incorrect attempts. Program will terminate.")
    return False

# Password verification
if not check_password():
    exit()  # Terminates the script if the password is incorrect

# Banner
print(Fore.MAGENTA + " __  __      __  __   ____  _                       _ ")
print(Fore.MAGENTA + "|  \/  |_  _|  \/  | |  _ \\(_)___  ___ ___  _ __ __| |")
print(Fore.MAGENTA + "| |\/| \\ \\/ / |\/| | | | | | / __|/ __/ _ \\| '__/ _` |")
print(Fore.MAGENTA + "| |  | |>  <| |  | | | |_| | \\__ \\ (_| (_) | | | (_| |")
print(Fore.MAGENTA + "|_|__|_/_/\\_\\_|  |_| |____/|_|___/\\___\\___/|_|  \\__,_|")
print(Fore.MAGENTA + "/ ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __      ")
print(Fore.MAGENTA + "\\___ \\| '_ \\ / _` | '_ ` _ \\| '_ ` _ \\ / _ \\ '__|     ")
print(Fore.MAGENTA + " ___) | |_) | (_| | | | | | | | | | | |  __/ |        ")
print(Fore.MAGENTA + "|____/| .__/ \\__,_|_| |_| |_|_| |_| |_|\\___|_|        ")
print(Fore.MAGENTA + "      |_|                                             ")
print(Fore.MAGENTA + "            Developed by Mxstry and Mxtion            ")
print("")

# User inputs
token = input("Login with your token: ").strip()
print("")
channel_id = input("Enter the channel ID: ").strip()
print("")
message = input("Message: ")
print("")
repeat_count = int(input("Number of messages: "))
print("")

# Payload and headers
payload = {
    'content': message
}

headers = {
    'authorization': token
}

# Sending messages
for i in range(repeat_count):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    r = requests.post(url, data=payload, headers=headers)
    
    if r.status_code == 200:
        print(f"Message {i + 1} was sent to {channel_id}.")
    
    elif r.status_code == 429:  # Handle rate limit error
        retry_after = r.json().get('retry_after', 1)  # Time in seconds
        print(f"Rate limit. Pausing for {retry_after} seconds...")
        time.sleep(retry_after)  # Pause
        # Retry sending the message
        r = requests.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            print(f"Message {i + 1} was sent to {channel_id}. (after rate limit)")
        else:
            print(f"Error sending message {i + 1}: {r.status_code} - {r.text}")
    
    else:
        print(f"Error sending message {i + 1}: {r.status_code} - {r.text}")
