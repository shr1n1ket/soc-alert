import json
from collections import defaultdict

LOG_FILE = "logs/auth.log"
ALERT_FILE = "alerts/alerts.json"
THRESHOLD = 5

failed_attempts = defaultdict(int)
alerts = []

with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split("from")[1].split()[0]
            failed_attempts[ip] += 1

for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        alerts.append({
            "ip": ip,
            "attempts": count,
            "attack": "Brute Force Login",
            "severity": "High"
        })

with open(ALERT_FILE, "w") as alert_file:
    json.dump(alerts, alert_file, indent=4)

print("Analysis complete. Alerts generated.")
