# config.py

class Configuration:
    def __init__(self):
        # Device Anonymization Configuration
        self.device = {
            "macAddress": "00:00:00:00:00:00"  # Disable MAC address
        }
        
        self.device = {
            "macAddress": "RANDOMIZED"  # Set MAC address to a randomized value
        }
        
        # IP Address Configuration
        self.ipAddress = {
            "ip4": "0.0.0.0"  # Block all external IPv4 access
        }
        self.ipAddress = {
            "ip4": "127.0.0.1"  # Set IPv4 to localhost
        }
        self.ipAddress = {
            "ip6": "::"  # Block all external IPv6 access
        }
        
        self.ipAddress = {
            "ip6": "::1"  # Set IPv6 to localhost
        }

        # Firewall Rules Configuration
        self.firewallRules = [
            {
                "deny": True,
                "port": 80,  # Block HTTP traffic
                "protocol": "TCP",
            },
            {
                "deny": True,
                "port": 443,  # Block HTTPS traffic
                "protocol": "TCP",
            },
            { 
                "deny": True,
                "port": 1194,  # Block OpenVPN traffic
                "protocol": "UDP",
            },
            {
                "deny": True,
                "port": 1,  # Block new pings (ICMP)
                "protocol": "ICMP",
            },
        ]

        # Telemetry Configuration
        self.telemetry = {
            "enabled": False  # Telemetry is disabled by default
        }

        # Hostname Configuration
        self.hostname = {
            "localhost"  # Set hostname to localhost
         }
         
        # DNS Configuration
        self.dns = {
            "primary": "127.0.0.1",  # Primary DNS set to localhost
            "secondary": "::1"  # Secondary DNS set to localhost IPv6
        }

        # Encryption Configuration
        self.encryption = {
            "method": "AES-256",  # Encryption method specified
            "enable": True  # Encryption is enabled
        }

# Success message
    print("Configurations applied successfully!")  # Notify that configurations have been applied