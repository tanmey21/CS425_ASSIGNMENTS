# Multithreaded Chat Server CS425

## Assignment 1

### Group Members:
- Tanmey Agarwal (211098) 
- Kumar Kanishk Singh (210544) 
- Sunny Raja Prasad (218171078)


### How to compile and run the code?
- Compile the server code using g++ server_grp.cpp -o server_grp
- Start the server using ./server_grp
- Start each client using ./client_grp
- Enter the username and password, if they matches the client will be added to the network.

### 1.  Features
### 1.1 Implemented Features:
- TCP server on port 12345 with support for multiple concurrent clients via threads

- User authentication from users.txt

Commands Supported:

        - /msg <user> <message> – Private message

        - /broadcast <message> – Message all users

        - /create_group <group> – Create a group

        - /join_group <group> – Join a group

        - /leave_group <group> – Leave a group

        - /group_msg <group> <message> – Message to group members

#### 1.2 Not Implemented Features
- No frontend, have to type messages from terminal.
- Persistent storage for messages even if server is closed.

### 2.  Design Decisions

- Each client is handled in a separate thread.

- Shared data structures protected using std::mutex and std::lock_guard:

        - clients: socket → username

        - users: username → password

        - groups: group → set of sockets

        - sock: username → socket

### 5.  Challenges & Solutions
- Handling concurrent client connections → Used multi-threading with std::mutex .
- Ensuring thread safety → Used std::lock_guard<std::mutex> for shared resources.
- Parsing user commands correctly → Used std::string::find() and substr().
- Debugging segmentation faults → Added proper error handling and log- ging.


### 6.  Restrictions
- Maximum clients: Limited by system resources and thread handling.
- Maximum groups: Theoretically unlimited but constrained by memory.
- Maximum message size: 1024 bytes per message.

### 8.  Sources
- Computer Networking: A top down Approach.
- C++ Reference for std::mutex , std::unordered_map.
- GeeksforGeeks articles on multi-threading and socket programming.