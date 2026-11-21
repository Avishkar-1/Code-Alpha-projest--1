from scapy.all import sniff
from analyzer import analyze_packet, display_packet

class NetworkSniffer:
    def __init__(self):
        self.packet_count = 0

    def process_packet(self, packet):
        self.packet_count += 1
        display_packet(analyze_packet(packet))

    def start(self, interface=None, count=0):
        print("=" * 65)
        print("             NETSNIFF NETWORK ANALYZER")
        print("=" * 65)
        print("Capture started...")
        print("Press Ctrl+C to stop.")
        print("Only metadata is displayed.")
        print("=" * 65)
        try:
            sniff(iface=interface, prn=self.process_packet, store=False, count=count)
        except KeyboardInterrupt:
            print("\\nCapture stopped by user.")
        except PermissionError:
            print("\\nPermission denied. Run with appropriate permissions.")
        except Exception as error:
            print(f"\\nCapture error: {error}")
        finally:
            print(f"\\nTotal packets processed: {self.packet_count}")
            print("Sniffer stopped.")
