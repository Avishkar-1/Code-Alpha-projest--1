from sniffer import NetworkSniffer

def main():
    print("""
=========================================
       NETSNIFF - NETWORK ANALYZER
=========================================
Educational Network Traffic Analyzer

Displays packet metadata such as IP addresses,
protocols, ports, and packet sizes.

Use only on networks/devices you own or
have explicit permission to monitor.
=========================================
""")
    interface = input("Enter network interface (leave blank for default): ").strip()
    if not interface:
        interface = None
    sniffer = NetworkSniffer()
    try:
        sniffer.start(interface=interface, count=0)
    except KeyboardInterrupt:
        print("\\nProgram exited.")

if __name__ == "__main__":
    main()
