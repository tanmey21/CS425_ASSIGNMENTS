# A collection of my 4 networking course projects.

## A1 – Multi-User Chat Server :heart_eyes::

Here's a summary of what needs to be done in the project:

- Develop a multi-threaded TCP chat server that supports user authentication, private messages, broadcast messages, and group chats.

- Implement server-side logic to handle commands like /msg, /broadcast, /create group, /join group, /leave group, and /group msg.

- Ensure proper synchronization for shared resources using C++ multithreading techniques, and provide a users.txt file containing authenticated users and passwords.

## A2 – DNS Resolver (Iterative & Recursive) :heart::

Here's a summary of what needs to be done in the project:

- Implement both iterative and recursive DNS lookup using Python and the dnspython library.

- For iterative, simulate querying root, TLD, and authoritative servers step-by-step.

- For recursive, delegate the full resolution to a resolver and return the final IP; handle errors gracefully.

## A3 – TCP Handshake via Raw Sockets :innocent::

Here's a summary of what needs to be done in the project:

- Implement the client side of the TCP three-way handshake using raw sockets in C++.

- Construct a SYN packet, receive and parse the SYN-ACK from the server, and send a final ACK.

- Match the expected sequence number behavior based on the server code provided in the GitHub repo.

## A4 – Routing Algorithms Simulator (DVR & LSR) :clap::

Here's a summary of what needs to be done in the project:

- Implement Distance Vector Routing (DVR) and Link State Routing (LSR) algorithms in C++ using an adjacency matrix as input.

- Simulate the computation of routing tables for each node using both algorithms.

- Output the routing tables showing destination, metric, and next hop for every node.
