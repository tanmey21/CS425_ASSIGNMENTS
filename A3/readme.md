# TCP Handshake via Raw Sockets 

## Group Members

- Kumar Kanishk Singh (210544)

- Sunny Raja Prasad (218171078)

- Tanmey Agarwal (211098)

## Overview

This project implements the client-side of a simplified TCP three-way handshake using raw sockets in C++.\
It manually constructs TCP/IP packets to simulate the following sequence:

1. SYN – Sends initial packet with sequence number 200

2. SYN-ACK – Receives and validates server response

3. ACK – Sends final acknowledgment with sequence number 600

## ⚙️ How to Compile and Run

### 🔧 Compilation:
```` g++ -o client client.cpp -std=c++11 ````

### ▶️ Execution:
```` sudo ./client ````

The client will:

- Create a raw socket with custom IP and TCP headers

- Send a SYN to port 12345

- Wait for and parse the SYN-ACK

- Complete the handshake with an ACK

- Console output provides real-time status updates.


