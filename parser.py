import socket
import struct


def format_mac(mac_bytes: bytes) -> str:
    return ":".join(f"{b:02x}" for b in mac_bytes)

def format_ipv4(ip_bytes: bytes) -> str:
    return ".".join(str(b) for b in ip_bytes)

def parse_ethernet_frame(data: bytes):
    
    desc_mac, src_mac, proto_type = struct.unpack("! 6s 6s H", data[:14])
    
    return format_mac(desc_mac), format_mac(src_mac), socket.ntohs(proto_type), data[14:]

def parse_ipv4_packet(data: bytes):
    
    version_ihl = data[0]
    ihl = (version_ihl & 15)* 4
    
    _, _, _, _, _, _, ttl, photo, _, src, target = struct.unpack("! B B H H H B B H 4s 4s", data[:20])
    
    scr_ip = format_ipv4(src)
    dst_ip = format_ipv4(target)
    
    return scr_ip, dst_ip, photo, ttl, data[ihl:]
    
    