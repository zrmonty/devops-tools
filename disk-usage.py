# This script is intended to be run as a cron job every 5 minutes.
# To set up the cron job, add the following line to your crontab file:
# */5 * * * * /path/to/python /path/to/script.py

import shutil
import smtplib
from email.message import EmailMessage

def main():
    threshold = 90  # Set the disk usage threshold in percent

    # Set the recipient email address. Replace with your email.
    to_email = ""  
    if not to_email:
        raise ValueError("Please set the 'to_email' variable with the recipient email address.")

    if is_disk_usage_above_threshold(threshold):
        subject = "Disk Usage Alert"
        message = f"Disk usage on the server has exceeded {threshold}%."
        send_email_alert(subject, message, to_email)

def is_disk_usage_above_threshold(threshold):
    """Check if the disk usage is above the given threshold."""
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    return percent_used > threshold

def send_email_alert(subject, message, to_email):
    """Send an email alert with the given subject and message to the specified email address."""
    # Set the sender email address. Replace with your email.
    from_email = ""  
    if not from_email:
        raise ValueError("Please set the 'from_email' variable with the sender email address.")

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)

if __name__ == "__main__":
    main()
