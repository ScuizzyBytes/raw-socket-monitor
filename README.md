<div align="center">

  <!-- GLITCH / CYBER BANNER -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=38&pause=1000&color=00FF66&center=true&vCenter=true&random=false&width=800&height=100&lines=%E2%9A%A1+CYBER_SNIFFER+v2.0;%F0%9F%91%81%EF%B8%8F+RAW+SOCKET+PACKET+MONITOR;%F0%9F%92%80+LOW-LEVEL+NETWORK+DISSECTOR" alt="Typing SVG" />
  </a>

  <br/>

  <!-- BADGES WITH ANIMATED HOVER / NEON LOOK -->
  <p align="center">
    <a href="#">
      <img src="https://img.shields.io/badge/CORE-PYTHON_3.10+-00F0FF?style=for-the-badge&logo=python&logoColor=black" alt="Python Version" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/KERNEL-LINUX_RAW_SOCKETS-FF0055?style=for-the-badge&logo=linux&logoColor=white" alt="Linux Kernel" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/GUI-CUSTOMTKINTER-00FF66?style=for-the-badge" alt="CustomTkinter" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/ARCHITECTURE-MODULAR_THREADED-7000FF?style=for-the-badge" alt="Architecture" />
    </a>
  </p>

  <p align="center">
    <i><b>A high-performance, zero-dependency, low-level network packet sniffer and frame analyzer built from scratch.</b></i>
  </p>

  <!-- ANIMATED METRIC WAVE -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00ff66,100:00f0ff&height=120&section=header&text=LIVE%20NETWORK%20INTERCEPTOR&fontSize=25&fontColor=000000&animation=twinkling" width="100%" />

</div>

---

<div align="center">

## ⚡ ARCHITECTURE OVERVIEW

```
                        ┌───────────────────────────────┐
                        │      RAW SOCKET (AF_PACKET)   │
                        └───────────────┬───────────────┘
                                        │
                                        ▼ (Raw Bytes Stream)
                        ┌───────────────────────────────┐
                        │    ETHERNET II FRAME PARSER   │
                        │    [Dest MAC | Src MAC | Type]│
                        └───────────────┬───────────────┘
                                        │
                                        ▼ (IPv4 Layer Payload)
                        ┌───────────────────────────────┐
                        │      IPv4 HEADER DISSECTOR    │
                        │  [IHL & 15] ──> Offset Slicer │
                        │  [TTL | Proto | Src IP | Dst] │
                        └───────────────┬───────────────┘
                                        │
                                        ▼ (Thread-Safe Event Queue)
                        ┌───────────────────────────────┐
                        │   CUSTOMTKINTER GUI ENGINE    │
                        └───────────────────────────────┘
```

</div>

---

## 🛠️ MODULE RESPONSIBILITIES

<div align="center">

| Module | Purpose | Technical Execution |
| :--- | :--- | :--- |
| **`sniffer.py`** | **Packet Capture Engine** | Hooks into OS network stack via `socket(AF_PACKET, SOCK_RAW, ntohs(3))` with privilege verification. |
| **`parser.py`** | **Binary Dissector** | Performs bitwise AND masking (`IHL & 0x0F`), address hex-formatting, and unpacked binary parsing via `struct.unpack`. |
| **`ui.py`** | **Cyberpunk Dashboard** | Multithreaded GUI built on `CustomTkinter` with auto-scrolling terminal log stream. |

</div>

---

## 🔬 TECHNICAL DEEP DIVE: BITWISE PARSING

Standard network abstraction layers hide frame headers. **CYBER_SNIFFER** manually slices and unpacks header byte arrays:

### 1. Ethernet II Header (14 Bytes)
```python
dest_mac, src_mac, proto_type = struct.unpack("! 6s 6s H", data[:14])
```
* **`! 6s 6s H`**: Big-endian network order. Extracts 6-byte destination MAC, 6-byte source MAC, and 2-byte EtherType integer.

### 2. Dynamic IPv4 Header Length (IHL Slicing)
```python
version_ihl = data[0]
ihl = (version_ihl & 15) * 4
```
* **Bitwise Masking (`& 15`)**: Extracts the lower 4 bits of the first IPv4 byte to isolate the Internet Header Length (IHL).
* **Length Multiplication (`* 4`)**: Converts the 32-bit word count into exact byte offset dimensions to calculate payload start index (`data[ihl:]`).

---

## 🚀 QUICK START & DEPLOYMENT

### Prerequisites
* **Linux Environment** (Ubuntu, Debian, or WSL2 with bridge mode).
* **Root Privileges** (Mandatory for binding `SOCK_RAW` sockets).
* **Python 3.10+**

```bash
# 1. Clone the repository
git clone https://github.com/ScuizzyBytes/cyber-packet-sniffer.git
cd cyber-packet-sniffer

# 2. Install GUI dependencies
pip install customtkinter

# 3. Launch with root elevation
sudo python3 ui.py
```

---

<div align="center">

## 📈 SYSTEM ROADMAP

```text
[✔] Phase 1: Raw Packet Ingestion (AF_PACKET, SOCK_RAW)
[✔] Phase 2: Binary Extraction & Frame Dissection (struct, Bitwise Operators)
[✔] Phase 3: CustomTkinter Terminal Dashboard & Dark Theme
[ ] Phase 4: Multithreaded Queue Ingestion (threading.Thread)
[ ] Phase 5: TCP/UDP Payload Hexdump Inspector
[ ] Phase 6: ICMP Anomaly Detection & Statistics Counter
```
