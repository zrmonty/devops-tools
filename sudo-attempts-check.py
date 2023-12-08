import subprocess
import time
import requests
import json
import re

def send_slack_notification(subject, message, webhook_url):
    payload = {
        "text": f"{subject}\n{message}",
    }
    requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

def monitor_sudo_failures(slack_webhook_url):
    if not slack_webhook_url:
        raise ValueError("Slack webhook URL must be provided.")
    
    while True:
        result = subprocess.run(['ausearch', '-m', 'EXECVE', '-ts', 'recent', '-i'], capture_output=True)
        logs = result.stdout.decode()

        if 'sudo' in logs and 'permission denied' in logs.lower():
            matches = re.findall(r'uid=(\w+)', logs)
            if matches:
                user = matches[0]
                message = f"User {user} attempted to use sudo without proper authentication."
                send_slack_notification("Sudo Alert", message, slack_webhook_url)
            
        time.sleep(3600)  # Check every hour

slack_webhook_url = ""  # Replace with your Slack webhook URL

monitor_sudo_failures(slack_webhook_url)
