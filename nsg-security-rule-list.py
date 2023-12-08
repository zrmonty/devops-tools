from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.network import NetworkManagementClient
from azure.common.exceptions import CloudError

# Azure setup
subscription_id = 'YOUR_SUBSCRIPTION_ID' or None
client_id = 'YOUR_CLIENT_ID' or None
secret = 'YOUR_SECRET' or None
tenant = 'YOUR_TENANT_ID' or None


def get_credentials(client_id, secret, tenant):
    """Get ServicePrincipalCredentials for Azure API authentication."""
    return ServicePrincipalCredentials(client_id=client_id, secret=secret, tenant=tenant)


def list_nsgs_and_rules(network_client):
    """List all NSGs and their associated security rules."""
    try:
        nsgs = network_client.network_security_groups.list_all()
        for nsg in nsgs:
            print(f"\tNSG name: {nsg.name}")
            for rule in nsg.security_rules:
                print(f"\t\tSecurity rule name: {rule.name}, priority: {rule.priority}, access: {rule.access}, direction: {rule.direction}, protocol: {rule.protocol}, source address prefix: {rule.source_address_prefix}, source port range: {rule.source_port_range}, destination address prefix: {rule.destination_address_prefix}, destination port range: {rule.destination_port_range}")
    except CloudError as e:
        print(f"An error occurred: {str(e)}")


def main():
    # Validate credentials
    if not all([subscription_id, client_id, secret, tenant]):
        raise ValueError("All Azure credentials (subscription ID, client ID, secret, and tenant ID) must be provided.")
    
    # Get credentials
    credentials = get_credentials(client_id, secret, tenant)
    
    # Create a client
    network_client = NetworkManagementClient(credentials, subscription_id)
    
    # List all NSGs and their associated security rules
    print("List of NSGs and their associated security rules:")
    list_nsgs_and_rules(network_client)


if __name__ == "__main__":
    main()
