#!/bin/python3

import sys
import socket
from datetime import datetime

try:
    import ping3    # Needed to check connection to host

except ImportError:
    print("Ping3 is not installed")
    x = input("Install ? (Y/N) : ")
    if(x in ("Y","y")):
        import subprocess
        package_name = "ping3"
        try:
        # Run pip install command
            subprocess.check_call(["pip", "install", package_name])
            print(f"Successfully installed {package_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while installing {package_name}: {e}")
            sys.exit()
    else:
        print("Exiting Program")
        sys.exit()

import ping3

# Define our target
if len(sys.argv) == 2:
    target = sys.argv[1]  # Translate hostname to IPv4
    try:
        response_time = ping3.ping(target)
        if response_time is not None:
            print("\n\nSuccessfully connected\n")
            print("\nStarting Scan\n")
        else:
            print("\nCould not connect to the host. Try again\n")
            sys.exit()
    except Exception as e:
        print(e)
        # print("\nError has occurred. Check your internet\n")
        sys.exit()
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip_address>")

# Banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

# List of commonly used ports
common_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    119: "NNTP",
    123: "NTP",
    135: "RPC",
    137: "NetBIOS",
    138: "NetBIOS",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD/LPR",
    993: "IMAPS",
    995: "POP3S",
    1080: "Socks",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Monitor",
    1521: "Oracle Database",
    1701: "L2TP",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5060: "SIP",
    5900: "VNC",
    8080: "HTTP Proxy"
}

try:
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Creates a Socket Object that must connect to ipv4 via port
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # Returns an error indicator - if port is open it throws a 0, otherwise 1
        if result == 0:
            print("Port " + str(port) + " is open and runs " + common_ports[port] + " protocol")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
