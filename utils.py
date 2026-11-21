from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Ether
from scapy.layers.dns import DNS

def get_protocol(packet):
    if packet.haslayer(DNS): return "DNS"
    if packet.haslayer(TCP): return "TCP"
    if packet.haslayer(UDP): return "UDP"
    if packet.haslayer(ICMP): return "ICMP"
    if packet.haslayer(IPv6): return "IPv6"
    if packet.haslayer(IP): return "IP"
    if packet.haslayer(Ether): return "Ethernet"
    return "OTHER"

def get_ip_addresses(packet):
    if packet.haslayer(IP): return packet[IP].src, packet[IP].dst
    if packet.haslayer(IPv6): return packet[IPv6].src, packet[IPv6].dst
    return "N/A", "N/A"

def get_ports(packet):
    if packet.haslayer(TCP): return packet[TCP].sport, packet[TCP].dport
    if packet.haslayer(UDP): return packet[UDP].sport, packet[UDP].dport
    return "N/A", "N/A"

def get_packet_size(packet):
    return len(packet)

def get_timestamp(packet):
    return float(packet.time)
