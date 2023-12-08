import pwd
import grp
import os
import time
import requests
import json

def monitor_user_accounts(slack_webhook_url):
    if not slack_webhook_url:
        raise ValueError("Slack webhook URL must be provided.")
    
    initial_users = set(get_user_accounts_with_groups())
    while True:
        current_users = set(get_user_accounts_with_groups())
        new_users = current_users - initial_users
        removed_users = initial_users - current_users
        
        for user in new_users:
            message = f"New user account created: {user}"
            send_slack_notification("User Account Alert", message, slack_webhook_url)
        
        for user in removed_users:
            message = f"User account removed: {user}"
            send_slack_notification("User Account Alert", message, slack_webhook_url)
        
        initial_users = current_users
        time.sleep(3600)  # Check every hour

def get_user_accounts_with_groups():
    users_with_groups = {}
    for user in pwd.getpwall():
        username = user.pw_name
        groups = [grp.getgrgid(g).gr_name for g in os.getgrouplist(username, user.pw_gid)]
        users_with_groups[username] = sorted(groups)
    return users_with_groups

def send_slack_notification(subject, message, webhook_url):
    payload = {
        "text": f"{subject}\n{message}",
    }
    requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

slack_webhook_url = ""  # Replace with your Slack webhook URL

monitor_user_accounts(slack_webhook_url)
