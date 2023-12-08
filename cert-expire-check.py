import ssl
import socket
import smtplib
from email.message import EmailMessage
from datetime import datetime
import requests
import json

def monitor_ssl_certificate_expiry(domain, alert_days_before_expiry, email_to, email_from, slack_webhook_url):
    if not email_to or not email_from:
        raise ValueError("Recipient and sender email addresses must be provided.")
    if not slack_webhook_url:
        raise ValueError("Slack webhook URL must be provided.")
    while True:
        cert = ssl.get_server_certificate((domain, 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        expiry_date = datetime.strptime(x509.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%SZ')
        remaining_days = (expiry_date - datetime.utcnow()).days
        if remaining_days <= alert_days_before_expiry:
            subject = f"SSL Certificate Expiry Alert: {domain}"
            message = f"The SSL certificate for {domain} will expire in {remaining_days} days."
            send_email_alert(subject, message, email_to, email_from)
            send_slack_notification(subject, message, slack_webhook_url)
        time.sleep(86400)  # Check every day

def send_email_alert(subject, message, to_email, from_email):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)

def send_slack_notification(subject, message, webhook_url):
    payload = {
        "text": f"{subject}\n{message}",
    }
    requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

domain = "example.com"  # Replace with your domain
alert_days_before_expiry = 30  # Days before expiry to send an alert
email_to = ""  # Replace with the recipient email address
email_from = ""  # Replace with the sender email address
slack_webhook_url = ""  # Replace with your Slack webhook URL

monitor_ssl_certificate_expiry(domain, alert_days_before_expiry, email_to, email_from, slack_webhook_url)
