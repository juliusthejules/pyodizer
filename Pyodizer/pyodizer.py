import json

# Load configuration from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

class Device:
    def __init__(self, mac_address):
        self.mac_address = mac_address

    def randomize_mac(self):
        print("Randomizing MAC address...")

    def disable_mac(self):
        print("Disabling MAC address...")

class IPAddress:
    def __init__(self, ip4, ip6):
        self.ip4 = ip4
        self.ip6 = ip6

    def block_external_ip4(self):
        print("Blocking external IPv4 access...")

    def set_ip4_to_localhost(self):
        print("Setting IPv4 to localhost...")

    def block_external_ip6(self):
        print("Blocking external IPv6 access...")

    def set_ip6_to_localhost(self):
        print("Setting IPv6 to localhost...")

class FirewallRules:
    def __init__(self, rules):
        self.rules = rules

    def apply_rules(self):
        for rule in self.rules:
            action = "Deny" if rule['deny'] else "Allow"
            print(f"{action}ing {rule['protocol']} traffic on port {rule['port']}")

class Telemetry:
    def __init__(self, enabled):
        self.enabled = enabled

    def disable_telemetry(self):
        print("Disabling telemetry...")

class Hostname:
    def __init__(self, hostname):
        self.hostname = hostname

    def set_hostname(self):
        print(f"Setting hostname to {self.hostname}...")

class DNS:
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def set_dns(self):
        print(f"Setting primary DNS to {self.primary} and secondary DNS to {self.secondary}...")

class Encryption:
    def __init__(self, method, enable):
        self.method = method
        self.enable = enable

    def enable_encryption(self):
        if self.enable:
            print(f"Enabling encryption using {self.method}...")

# Create instances based on configuration
device = Device(config['device']['macAddress'])
ip_address = IPAddress(config['ipAddress']['ip4'], config['ipAddress']['ip6'])
firewall_rules = FirewallRules(config['firewallRules'])
telemetry = Telemetry(config['telemetry']['enabled'])
hostname = Hostname(config['hostname'])
dns = DNS(config['dns']['primary'], config['dns']['secondary'])
encryption = Encryption(config['encryption']['method'], config['encryption']['enable'])

# Apply configuration based on chosen values
if device.mac_address == "RANDOMIZED":
    device.randomize_mac()
elif device.mac_address == "00:00:00:00:00:00":
    device.disable_mac()

if ip_address.ip4 == "0.0.0.0":
    ip_address.block_external_ip4()
elif ip_address.ip4 == "127.0.0.1":
    ip_address.set_ip4_to_localhost()

if ip_address.ip6 == "::":
    ip_address.block_external_ip6()
elif ip_address.ip6 == "::1":
    ip_address.set_ip6_to_localhost()

firewall_rules.apply_rules()

if not telemetry.enabled:
    telemetry.disable_telemetry()

hostname.set_hostname()

dns.set_dns()

if encryption.enable:
    encryption.enable_encryption()

# Success message
print("Configurations applied successfully!")