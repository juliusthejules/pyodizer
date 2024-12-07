import os

# Class Definitions
class Device:
    def __init__(self, mac_address, bt_address):
        self.mac_address = mac_address
        self.bt_address = bt_address

    def disable_mac_and_bt(self):
        print(f"Disabling MAC address {self.mac_address} and Bluetooth address {self.bt_address}...")

class IPAddress:
    def __init__(self, ip4, ip6):
        self.ip4 = ip4
        self.ip6 = ip6

    def set_localhost(self):
        print(f"Setting IPv4 to {self.ip4} and IPv6 to {self.ip6}...")

class FirewallRule:
    def __init__(self, deny, port, protocol):
        self.deny = deny
        self.port = port
        self.protocol = protocol

    def apply_rule(self):
        if self.deny:
            print(f"Applying firewall rule: Blocking traffic on port {self.port}, protocol {self.protocol}")

class Telemetry:
    def __init__(self, enabled):
        self.enabled = enabled

    def disable_telemetry(self):
        if not self.enabled:
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

class Traceroute:
    def __init__(self, block):
        self.block = block

    def block_traceroute(self):
        if self.block:
            print("Blocking traceroute...")

class Fingerprinting:
    def __init__(self, obfuscate):
        self.obfuscate = obfuscate

    def obfuscate_fingerprint(self):
        if self.obfuscate:
            print("Obfuscating browser fingerprint...")

# PyDonfig Loader Function
def load_pydl(file_path):
    config = {}
    with open(file_path, "r") as file:
        current_section = None
        for line in file:
            line = line.strip()

            # Skip comments and empty lines
            if line.startswith("//") or not line:
                continue

            if line.endswith(":"):  # Section header
                current_section = line[:-1]
                config[current_section] = {}
            else:  # Key-value pair
                key, value = line.split(">", 1)
                key = key.strip()
                value = value.strip().strip('"')  # Remove quotes
                # Convert booleans and numbers
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False
                elif value.lower() == "null":
                    value = None
                elif value.isdigit():
                    value = int(value)
                elif value.replace(".", "", 1).isdigit():
                    value = float(value)

                if current_section:
                    config[current_section][key] = value
                else:
                    config[key] = value
    return config

# Main Execution
if __name__ == "__main__":
    config_path = "./Pyodizer/config.pydl"

    # Check if the configuration file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    # Load the configuration
    config = load_pydl(config_path)
    print(f"Successfully loaded configuration from {config_path}")

    # Create instances dynamically based on configuration
    device = Device(
        mac_address=config["device"]["macAddress"],
        bt_address=config["device"]["btAddress"]
    )
    ip_address = IPAddress(
        ip4=config["ipAddress"]["ip4"],
        ip6=config["ipAddress"]["ip6"]
    )
    firewall_rule = FirewallRule(
        deny=config["firewallRule"]["deny"],
        port=config["firewallRule"]["port"],
        protocol=config["firewallRule"]["protocol"]
    )
    telemetry = Telemetry(enabled=config["telemetry"]["enabled"])
    hostname = Hostname(hostname=config["hostname"])
    dns = DNS(
        primary=config["dns"]["primary"],
        secondary=config["dns"]["secondary"]
    )
    encryption = Encryption(
        method=config["encryption"]["method"],
        enable=config["encryption"]["enable"]
    )
    traceroute = Traceroute(block=config["traceroute"]["block"])
    fingerprinting = Fingerprinting(obfuscate=config["fingerprinting"]["obfuscate"])

    # Apply configuration dynamically
    device.disable_mac_and_bt()
    ip_address.set_localhost()
    firewall_rule.apply_rule()
    telemetry.disable_telemetry()
    hostname.set_hostname()
    dns.set_dns()
    encryption.enable_encryption()
    traceroute.block_traceroute()
    fingerprinting.obfuscate_fingerprint()

    # Success message
    print("All configurations applied successfully!")
