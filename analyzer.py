from utils import get_protocol, get_ip_addresses, get_ports, get_packet_size, get_timestamp

def analyze_packet(packet):
    source_ip, destination_ip = get_ip_addresses(packet)
    source_port, destination_port = get_ports(packet)
    return {
        "timestamp": get_timestamp(packet),
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "protocol": get_protocol(packet),
        "source_port": source_port,
        "destination_port": destination_port,
        "size": get_packet_size(packet)
    }

def display_packet(info):
    print("\\n" + "-" * 65)
    print(f"Time           : {info['timestamp']}")
    print(f"Source IP      : {info['source_ip']}")
    print(f"Destination IP : {info['destination_ip']}")
    print(f"Protocol       : {info['protocol']}")
    print(f"Source Port    : {info['source_port']}")
    print(f"Dest Port      : {info['destination_port']}")
    print(f"Packet Size    : {info['size']} bytes")
    print("-" * 65)
