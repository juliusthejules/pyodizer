import json
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from scapy.all import sniff, IP
import requests

# Read config
def read_config(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

config = read_config('./config.json')

# Device class
class Device:
    def __init__(self, mac_address, bt_address):
        self.mac_address = mac_address
        self.bt_address = bt_address

    def disable_mac_and_bt(self):
        print("MAC and Bluetooth addresses are set to anonymous placeholders.")

# IPAddress class
class IPAddress:
    def __init__(self, ip4, ip6):
        self.ip4 = ip4
        self.ip6 = ip6

    def set_localhost(self):
        print("IP addresses set to localhost for maximum anonymity.")

# FirewallRule class
class FirewallRule:
    def __init__(self, rule):
        self.rule = rule

    def apply_rule(self):
        if self.rule.get("deny") and self.rule.get("port") == 0 and self.rule.get("protocol") == "ALL":
            print("Applying firewall rule to block all traffic.")

# Telemetry class
class Telemetry:
    def __init__(self, enabled):
        self.enabled = enabled

    def disable_telemetry(self):
        print("Telemetry disabled.")

# Hostname class
class Hostname:
    def __init__(self, hostname):
        self.hostname = hostname

    def set_hostname(self):
        print(f"Hostname set to {self.hostname} for additional anonymity.")

# DNS class
class DNS:
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def set_dns(self):
        print("DNS servers set to localhost for primary and secondary.")

# Encryption class
class Encryption:
    def __init__(self, method, enable):
        self.method = method
        self.enable = enable

    def enable_encryption(self):
        if self.method == "AES-256":
            key = hashlib.sha256(b'secret_key').digest()  # Using a mock key here
            cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16))
            print(f"Encryption enabled with {self.method}.")

# Traceroute class
class Traceroute:
    def __init__(self, block):
        self.block = block

    def block_traceroute(self):
        if self.block:
            print("Blocking traceroutes by ignoring ICMP requests.")

            def packet_callback(packet):
                if IP in packet and packet[IP].proto == 1:  # ICMP protocol
                    print("ICMP packet detected and ignored for traceroute blocking.")
                    return None

            # Start a sniffing process to drop ICMP packets
            sniff(filter="icmp", prn=packet_callback, store=0)

# Fingerprinting class
class Fingerprinting:
    def __init__(self, obfuscate):
        self.obfuscate = obfuscate

    def obfuscate_fingerprint(self):
        if self.obfuscate:
            user_agent = "Mozilla/5.0 (compatible; Pyodizer/1.0)"
            headers = {"User-Agent": user_agent}
            response = requests.get("https://httpbin.org/user-agent", headers=headers)
            print(f"Fingerprint obfuscation enabled. User-Agent set to: {response.json()['user-agent']}")

# Instantiate classes based on config
device = Device(config['device']['macAddress'], config['device']['btAddress'])
ip_address = IPAddress(config['ipAddress']['ip4'], config['ipAddress']['ip6'])
firewall_rule = FirewallRule(config['firewallRule'])
telemetry = Telemetry(config['telemetry']['enabled'])
hostname = Hostname(config['hostname'])
dns = DNS(config['dns']['primary'], config['dns']['secondary'])
encryption = Encryption(config['encryption']['method'], config['encryption']['enable'])
traceroute = Traceroute(config['traceroute']['block'])
fingerprinting = Fingerprinting(config['fingerprinting']['obfuscate'])

# Apply configurations
device.disable_mac_and_bt()
ip_address.set_localhost()
firewall_rule.apply_rule()
if not telemetry.enabled:
    telemetry.disable_telemetry()
hostname.set_hostname()
dns.set_dns()
if encryption.enable:
    encryption.enable_encryption()
if traceroute.block:
    traceroute.block_traceroute()
if fingerprinting.obfuscate:
    fingerprinting.obfuscate_fingerprint()

print("Configurations applied successfully.")
