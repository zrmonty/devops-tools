# This script provides an automated and programmatic way to monitor network latency, 
# with easy integration into larger systems, clear output, and additional functionality 
# like error handling and extensibility over the traditional ping command.

import subprocess
import re

def test_network_latency(hosts):
    """
    Tests the network latency to a list of IP addresses or hostnames.
    
    Args:
    hosts (list): A list of IP addresses or hostnames to test latency against.
    """
    if not hosts:
        raise ValueError("No hosts provided. Please add at least one IP address or hostname to the 'hosts' list.")
    
    for host in hosts:
        avg_latency = get_average_latency(host)
        if avg_latency is not None:
            print(f"Average latency to {host}: {avg_latency} ms")
        else:
            print(f"Failed to test latency to {host}")

def get_average_latency(host):
    """
    Pings a host and returns the average latency.
    
    Args:
    host (str): The IP address or hostname to ping.
    
    Returns:
    float or None: The average latency to the host, or None if the ping failed.
    """
    try:
        output = subprocess.check_output(["ping", "-c", "4", host])
        match = re.search(r"round-trip min/avg/max/stddev = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)", output.decode())
        if match:
            return float(match.group(2))
    except subprocess.CalledProcessError:
        return None

hosts = []  # Add the list of IP addresses or hostnames

test_network_latency(hosts)
