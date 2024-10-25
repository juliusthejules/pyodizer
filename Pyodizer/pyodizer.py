import json

def read_config(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

config = read_config('./config.json')

class Device:
    def __init__(self, mac_address, bt_address):
        self.mac_address = mac_address
        self.bt_address = bt_address

    def disable_mac_and_bt(self):
        print("Disabling MAC and Bluetooth addresses...")

class IPAddress:
    def __init__(self, ip4, ip6):
        self.ip4 = ip4
        self.ip6 = ip6

    def set_localhost(self):
        print("Setting both IPv4 and IPv6 to localhost...")

class FirewallRule:
    def __init__(self, rule):
        self.rule = rule

    def apply_rule(self):
        if self.rule.get("deny") and self.rule.get("port") == 0 and self.rule.get("protocol") == "ALL":
            print("Applying firewall rule: Blocking all traffic")

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
        print("Setting DNS servers to primary and secondary localhost...")

class Encryption:
    def __init__(self, method, enable):
        self.method = method
        self.enable = enable

    def enable_encryption(self):
        print(f"Enabling encryption with method {self.method}...")

# Create instances based on configuration
device = Device(config['device']['macAddress'], config['device'].get('btAddress'))
ip_address = IPAddress(config['ipAddress']['ip4'], config['ipAddress']['ip6'])
firewall_rule = FirewallRule(config['firewallRule'])
telemetry = Telemetry(config['telemetry']['enabled'])
hostname = Hostname(config['hostname'])
dns = DNS(config['dns']['primary'], config['dns']['secondary'])
encryption = Encryption(config['encryption']['method'], config['encryption']['enable'])

# Apply configuration based on chosen values
device.disable_mac_and_bt()
ip_address.set_localhost()
firewall_rule.apply_rule()

if not telemetry.enabled:
    telemetry.disable_telemetry()

hostname.set_hostname()
dns.set_dns()

if encryption.enable:
    encryption.enable_encryption()

# Success message
print("Configurations applied successfully!")
