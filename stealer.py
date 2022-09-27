import subprocess
import os
import sys

# create a file
password_file = open("passwords.txt", "w")
password_file.write("Hello sir! Here are your passwords:\n\n")
password_file.close()

# lists
wifi_files = {}
wifi_name = "none"
wifi_password = "not found"

# use Python to execute a Windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

# grab current directory
path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.update({filename: ["not found", "not found"]})

for i in wifi_files:
    with open(i, 'r') as f:
        for line in f.readlines():
            if 'keyMaterial' in line:
                stripped = line.strip()[13:-14]
                wifi_files[i][1] = stripped

            if 'name' in line and wifi_files[i][0] == "not found":
                stripped = line.strip()[6:-7]
                wifi_files[i][0] = stripped
    sys.stdout = open("passwords.txt", "a")
    print("SSID: "+ wifi_files[i][0] + "\tPassword: "+ wifi_files[i][1], sep='\n')
    sys.stdout.close()
    os.remove(i)