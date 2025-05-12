# DNS Resolver

## Group Members:
- Kumar Kanishk Singh (210544)
- Sunny Raja Prasad (218171078)
- Tanmey Agarwal (211098)

## Overview:
This Python script implements both iterative and recursive DNS resolution to resolve domain names to IP addresses using the dnspython library. It mimics how real DNS resolvers query root, TLD, and authoritative servers.

## How to Run:
### Prerequisites:
Make sure you have Python 3 and dnspython installed:

```` pip install dnspython ````

### Usage:
```` python3 dns_server.py <mode> <domain> ````

        mode: iterative or recursive
        domain: Domain name to resolve (e.g., example.com)

### Example:
```` python3 dns_server.py iterative google.com ```` \
```` python3 dns_server.py recursive openai.com ````

## ⚙️ How It Works

### Iterative Mode:

- Starts at a root server and queries DNS hierarchy step-by-step.

- Gathers NS records and resolves IPs of TLD and authoritative servers.

- Sends final query to retrieve the domain's IP address.

### Recursive Mode:
- Uses dns.resolver.resolve() to retrieve NS and A records.

- The external resolver handles the full query path.

- Returns resolved IP or failure message.


## 🛠 Error Handling

- Handles DNS timeouts, invalid responses, and lookup failures gracefully.

- 7-second timeout set for each DNS query attempt.

- Future improvements may include retries, caching, and parallel queries.


