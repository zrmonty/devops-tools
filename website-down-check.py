import requests
import json
import time

class WebsiteMonitor:
    def __init__(self, slack_webhook_url):
        self.slack_webhook_url = slack_webhook_url

        if not slack_webhook_url:
            raise ValueError("Slack webhook URL must be provided.")

    def start_monitoring(self, website_url):
        if not website_url:
            raise ValueError("Website URL must be provided.")

        while True:
            self.check_website(website_url)
            time.sleep(300)  # Check every 5 minutes

    def check_website(self, website_url):
        try:
            response = requests.get(website_url, timeout=10)
            if response.status_code != 200:
                self.send_alert(f"Website {website_url} is down. Status code: {response.status_code}")
        except requests.RequestException as e:
            self.send_alert(f"Website {website_url} is down. Error: {str(e)}")

    def send_alert(self, message):
        payload = {
            "text": message,
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(self.slack_webhook_url, data=json.dumps(payload), headers=headers)

slack_webhook_url = ""  # Replace with your Slack webhook URL

monitor = WebsiteMonitor(slack_webhook_url)
website_url = ""  # Replace with your website URL
monitor.start_monitoring(website_url)
