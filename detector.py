import re

logfile = "auth.log"

attempts = {}

with open(logfile,"r") as file:
    for line in file:
        if "Failed password" in line:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}',line)
            if ip:
                ip = ip[0]
                attempts[ip] = attempts.get(ip,0) + 1

for ip,count in attempts.items():
    if count > 5:
        print("Possible brute force attack from:", ip)
