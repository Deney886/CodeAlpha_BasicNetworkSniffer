from scapy.all import *

def packet_callback(packet):
    print("\n=== Packet Captured ===")

    if packet.haslayer(IP):
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

    if packet.haslayer(Raw):
        print("Payload:")
        print(packet[Raw].load)

sniff(filter="tcp", prn=packet_callback, store=False, count=20)