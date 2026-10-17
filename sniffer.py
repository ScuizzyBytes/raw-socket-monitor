import os
import socket
import sys


def main() -> None:
    
    if sys.platform.startswith("Linux") and os.geteuid() != 0:
        print("[-] Error You need to continue root access...")
        print("[-] Try With Command: sudo python3 sniffer.py")
        sys.exit(1)
        
    try:
        raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    except PermissionError:
        print("[-] Error: Run with Sudo")
        sys.exit(1)

    print("=" * 60)
    print(" [ENGINE] Sniffing Raw Socket from the wire")
    print(" [INFO] Type Ctrl + C to exit.")
    print("=" * 60)
    
    try:
        while True:
            raw_data, addr = raw_socket.recvfrom(65535)
            interface = addr[0]
            packet_len = len(raw_data)
            
            print(f" [PACKET] Interface: {interface:<10} | Size: {packet_len} bytes")
    except KeyboardInterrupt:
        print("Session has Been Ended!")
        
main()