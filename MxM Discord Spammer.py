import requests
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Passwort für den Zugriff
PASSWORD = "1509"  # Ersetze dies durch dein gewünschtes Passwort

# Funktion zur Passwortüberprüfung
def check_password():
    attempts = 3  # Anzahl der Versuche
    for _ in range(attempts):
        entered_password = input("Bitte gib dein Passwort ein: ").strip()
        if entered_password == PASSWORD:
            print(Fore.GREEN + "Passwort korrekt. Zugriff gewährt.\n")
            return True
        else:
            print(Fore.RED + "Falsches Passwort. Bitte versuche es erneut.\n")
    print(Fore.YELLOW + "Zu viele falsche Versuche. Programm wird beendet.")
    return False

# Passwortüberprüfung
if not check_password():
    exit()  # Beendet das Skript, wenn das Passwort falsch ist

# Banner
print(Fore.MAGENTA + " __  __      __  __   ____  _                       _ ")
print(Fore.MAGENTA + "|  \/  |_  _|  \/  | |  _ \(_)___  ___ ___  _ __ __| |")
print(Fore.MAGENTA + "| |\/| \ \/ / |\/| | | | | | / __|/ __/ _ \| '__/ _` |")
print(Fore.MAGENTA + "| |  | |>  <| |  | | | |_| | \__ \ (_| (_) | | | (_| |")
print(Fore.MAGENTA + "|_|__|_/_/\_\_|  |_| |____/|_|___/\___\___/|_|  \__,_|")
print(Fore.MAGENTA + "/ ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __      ")
print(Fore.MAGENTA + "\___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|     ")
print(Fore.MAGENTA + " ___) | |_) | (_| | | | | | | | | | | |  __/ |        ")
print(Fore.MAGENTA + "|____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|        ")
print(Fore.MAGENTA + "      |_|                                             ")
print(Fore.MAGENTA + "            Developed by Mxstry and Mxtion            ")
print("")

# Eingaben des Benutzers
token = input("Login mit deinem Token: ").strip()
print("")
channel_id = input("Gib die Channel-ID ein: ").strip()
print("")
message = input("Nachricht: ")
print("")
repeat_count = int(input("Nachrichtenanzahl: "))
print("")

# Payload und Header
payload = {
    'content': message
}

headers = {
    'authorization': token
}

# Nachrichten senden
for i in range(repeat_count):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    r = requests.post(url, data=payload, headers=headers)
    
    if r.status_code == 200:
        print(f"Nachricht {i + 1} wurde an {channel_id} gesendet.")
    
    elif r.status_code == 429:  # Ratenlimit-Fehler behandeln
        retry_after = r.json().get('retry_after', 1)  # Zeit in Sekunden
        print(f"Rate-Limit. Pausiere für {retry_after} Sekunden...")
        time.sleep(retry_after)  # Pause
        # Erneut versuchen
        r = requests.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            print(f"Nachricht {i + 1} wurde an {channel_id} gesendet. (nach Rate-Limit)")
        else:
            print(f"Fehler beim Senden von Nachricht {i + 1}: {r.status_code} - {r.text}")
    
    else:
        print(f"Fehler beim Senden von Nachricht {i + 1}: {r.status_code} - {r.text}")
