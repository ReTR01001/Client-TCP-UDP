Python TCP & UDP Clients - Raw Socket Communication

<img width="1533" height="770" alt="image" src="https://github.com/user-attachments/assets/fab335e7-6cba-4bc2-a459-25e26c5041cc" />


About the Project
This repository contains Python scripts demonstrating how to build both **TCP** and **UDP** clients from scratch using the native `socket` library. The primary goal of this lab is to practically explore low-level network communication, comparing connection-oriented (TCP) and connectionless (UDP) protocols. 

The project was tested and validated in a Linux environment (Kali Linux), interacting directly with **Netcat** listeners to simulate real network operations and two-way messaging.

kills Demonstrated
**Low-Level Networking:** Direct interaction with the TCP/IP stack using both `SOCK_STREAM` (TCP) and `SOCK_DGRAM` (UDP).
**Transport Layer Mechanics:** Understanding the difference between establishing a reliable connection (TCP handshake) and sending rapid, connectionless datagrams (UDP).
**Infrastructure & Cybersecurity Foundation:** Essential knowledge of how data packets are routed, encoded, and decoded in clear text, forming the baseline for network troubleshooting, port scanning, and custom security tool development.

* <img width="1528" height="717" alt="image" src="https://github.com/user-attachments/assets/3b9958dc-34ee-4026-b3a0-a0dddd24d58d" />


Technologies & Tools
**Language:** Python 3
**Library:** `socket` (native)
**Test Environment:** Kali Linux / Netcat (`nc`)

---

How to Reproduce the Labs

Scenario 1: TCP Client
A connection-oriented protocol where a session is established before data is transmitted.*

**1. Start the TCP Server (Listener):**
Open a terminal and use Netcat to listen on a specific port (e.g., `4466`).
```bash
nc -lvp 4466
