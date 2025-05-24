import subprocess
import re
import os
import sys
import time
from time import sleep
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")

# الألوان
#===========================
Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
Z1 = '\033[2;31m' # أحمر ثاني
F = '\033[2;32m'  # أخضر
F1 = '\033[1;32m' #اخضر غامق
F2 = '\033[0;32m' #اخضر فاتح
A = '\033[2;34m'  # أزرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # أزرق فاتح
M = '\x1b[1;37m'  # أبيض
#============================

def sleep1(T):
    for r in T + "\n":
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(10/1000)  

def sleep(T):
    for r in T + "\n":
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(20/1000) 

os.system("cls")
os.system("clear")

logo = ('      M O K A')
banner = sleep1(F1 + pyfiglet.figlet_format(logo))
t2 = ("▃▃" * 29)
tt2 = sleep1(M + t2)

print(f"\n \n{F1}                Wifi Password Saved")
print(f"{Y}[1] WINDOWS")
print(f"{Y}[2] KALI LINUX")
windo = input(f"{M} =>> ")
if windo == "1":
    os.system("cls")
    os.system("clear")
    logo = ('      M O K A')
    banner = sleep1(F1 + pyfiglet.figlet_format(logo))
    t2 = ("▃▃" * 29)
    tt2 = sleep1(M + t2)

    def get_wifi_profiles():
        result = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding="utf-8")
        profiles = re.findall(r"All User Profile\s*:\s(.*)", result)
        return [p.strip() for p in profiles]

    def get_wifi_password(profile):
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"], encoding="utf-8", errors="ignore")
            password = re.search(r"Key Content\s*:\s(.*)", result)
            if password:
                return f"{F1}{password.group(1).strip()}{M}"
            else:
                return f"{Z}(Nothing / UNKNOWN){M}"
        except subprocess.CalledProcessError:
            return f"{Z}(Error){M}" 

    def main():
        profiles = get_wifi_profiles()
        print(f"\n{Y} WIFI Password :{M}\n")
        print(f"{Y}{'-' * 50}{M}")
        print(f"{Y}{'{:<30}'.format('Name')} | {'{:<}'.format('Password')}{M}")
        print(f"{Y}{'-' * 50}{M}")
        for profile in profiles:
            password = get_wifi_password(profile)
            print(f"{X}{'{:<30}'.format(profile)}{M} {Y}|{M} {password}")

    if __name__ == "__main__":
        main()
elif windo == "2":
    os.system("clear")
    logo = ('      M O K A')
    banner = sleep1(F1 + pyfiglet.figlet_format(logo))
    t2 = ("▃▃" * 29)
    tt2 = sleep1(M + t2)

    def get_wifi_profiles():
        try:
            
            result = subprocess.check_output(["nmcli", "-t", "-f", "NAME", "connection", "show"], encoding="utf-8")
            profiles = result.splitlines()
            return [p.strip() for p in profiles if p.strip()]
        except subprocess.CalledProcessError:
            print(f"{Z}Error: Make sure you are running the code with root privileges (use sudo){M}")
            return []

    def get_wifi_password(profile):
        try:
            
            result = subprocess.check_output(["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", profile], encoding="utf-8", errors="ignore")
            password = result.strip()
            if password:
                return f"{F1}{password}{M}"
            else:
                return f"{Z}(Nothing / UNKNOWN){M}"
        except subprocess.CalledProcessError:
            return f"{Z}(Error){M}"

    def main():
        
        if os.geteuid() != 0:
            print(f"{Z}Error: Make sure you are running the code with root privileges (use sudo){M}")
            sys.exit(1)

        profiles = get_wifi_profiles()
        if not profiles:
            print(f"{Z}There are no saved Wi-Fi networks or an error occurred.{M}")
            return

        print(f"\n{Y}   WIFI Password{M}\n")
        print(f"{Y}{'-' * 50}{M}")
        print(f"{Y}{'{:<30}'.format('Name')} | {'{:<}'.format('Password')}{M}")
        print(f"{Y}{'-' * 50}{M}")
        for profile in profiles:
            password = get_wifi_password(profile)
            print(f"{X}{'{:<30}'.format(profile)}{M} {Y}|{M} {password}")

    if __name__ == "__main__":
        main()
else:

    print(f"{Z}Error")
    exit()
