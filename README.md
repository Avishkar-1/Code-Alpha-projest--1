# NetSniff – Network Traffic Analyzer

A Python-based educational network sniffer that captures packets and displays metadata for learning networking and cybersecurity fundamentals.

## Features
- Real-time packet capture
- Source and destination IP addresses
- Protocol identification (TCP, UDP, ICMP, DNS)
- TCP/UDP port metadata
- Packet size and timestamp
- Modular Python structure

## Requirements
- Python 3
- Scapy

## Installation (Linux/Kali)
```bash
git clone https://github.com/YOUR_USERNAME/NetSniff-Network-Traffic-Analyzer.git
cd NetSniff-Network-Traffic-Analyzer
python3 -m pip install -r requirements.txt
```

## Run
Packet capture may require elevated permissions:
```bash
sudo python3 main.py
```
When prompted, enter an interface name or press Enter to use the default.

List interfaces:
```bash
ip -br link
```

## Project Structure
```text
NetSniff-Network-Traffic-Analyzer/
├── main.py
├── sniffer.py
├── analyzer.py
├── utils.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Ethical Use
Use this project only on networks and devices you own or have explicit permission to monitor. This version displays metadata only; it does not intentionally extract private application messages, passwords, or credentials.

## Disclaimer
This project is provided for educational purposes. The developer is not responsible for unauthorized or improper use.

## License
MIT
