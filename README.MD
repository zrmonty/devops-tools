# DevOps and System Reliability Engineering (SRE) Scripts

This repository contains Python scripts for various DevOps and SRE tasks, including SSL certificate monitoring, disk usage monitoring, network latency testing, and monitoring user accounts. Each script serves a specific purpose and can be customized for your environment. Some of these are older and can be used with monitoring services, but I want to save them just in case I ever find use for them again.

## Table of Contents

1. [SSL Certificate Expiry Monitoring](#ssl-certificate-expiry-monitoring)
2. [Disk Usage Monitoring](#disk-usage-monitoring)
3. [Network Latency Testing](#network-latency-testing)
4. [Azure Network Security Groups and Rules](#azure-network-security-groups-and-rules)
5. [Sudo Command Authorization Failure Monitoring](#sudo-command-authorization-failure-monitoring)
6. [User Account Monitoring](#user-account-monitoring)
7. [Website Availability Monitoring](#website-availability-monitoring)

## SSL Certificate Expiry Monitoring

### Description

This script monitors the expiration date of SSL certificates for a given domain. When the certificate is about to expire (based on the specified number of days), it sends alerts via email and Slack.

### How to Use

Configure the following variables:

- `domain`: The domain for which you want to monitor SSL certificate expiry.
- `alert_days_before_expiry`: The number of days before certificate expiration to send an alert.
- `email_to`: The recipient email address for alerts.
- `email_from`: The sender email address for alerts.
- `slack_webhook_url`: Your Slack webhook URL for sending alerts.

Run the script:

```shell
python cert-expire-check.py
```

## Disk Usage Monitoring

### Description
This script monitors disk usage on a server. If the disk usage exceeds a specified threshold, it sends an email alert.

### How to Use
Configure the following variables:

- `threshold``: The disk usage threshold (in percent) above which an alert is sent.
- `to_email``: The recipient email address for alerts.

Run the script:

```shell
python disk-usage.py
```

To automate the script, set it up as a cron job to run periodically.

## Network Latency Testing

### Description
This script tests network latency to a list of IP addresses or hostnames and reports the average latency. It provides an alternative to the traditional ping command with error handling and extensibility.

### How to Use
Configure the hosts list with the IP addresses or hostnames you want to test.

Run the script:

```shell
python latency-test.py
```

## Azure Network Security Groups and Rules

### Description
This script lists all Network Security Groups (NSGs) and their associated security rules in an Azure subscription. It helps monitor and audit security configurations.

### How to Use
Configure Azure credentials:

- `subscription_id`: Your Azure subscription ID.
- `client_id`: Your Azure client ID.
- `secret`: Your Azure secret.
- `tenant`: Your Azure tenant ID.

Run the script:

```shell
python nsg-security-rule-list.py
```

## Sudo Command Authorization Failure Monitoring

### Description
This script monitors sudo command authorization failures in Linux systems. It searches the audit logs and sends a Slack notification when unauthorized sudo attempts are detected.

### How to Use
Configure the following variable:

- `slack_webhook_url`: Your Slack webhook URL for sending alerts.

Run the script:

```shell
python sudo-attempts-check.py
```

## User Account Monitoring

### Description
This script monitors user account changes on Linux systems, including new account creations and removals. It sends alerts via Slack when changes are detected.

### How to Use
Configure the following variable:

- `slack_webhook_url`: Your Slack webhook URL for sending alerts.

Run the script:

```shell
python user-create-delete-elevate-watch.py
```

## Website Availability Monitoring

### Description
This script monitors the availability of a website by sending HTTP requests. It sends alerts via Slack when the website is unreachable or returns an error status code.

### How to Use
Configure the following variables:

- `slack_webhook_url`: Your Slack webhook URL for sending alerts.
- `website_url`: The URL of the website to monitor.

Run the script:
```shell
python website-down-check.py
```