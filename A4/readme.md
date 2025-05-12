# Routing Algorithms Simulator 

## Group Members
1. Kumar Kanishk Singh (210544)

2. Sunny Raja Prasad (218171078)

3. Tanmey Agarwal (211098)

## 📌 Objective
This project implements and simulates two core routing algorithms in computer networks:

1. Distance Vector Routing (DVR)

2. Link State Routing (LSR) (using Dijkstra's Algorithm)

The program reads an adjacency matrix and outputs routing tables for each node, allowing a side-by-side comparison of both algorithms.

## ⚙️ Compilation & Execution
### 🔧 Compile:
```` g++ -std=c++17 -o routing_sim routing_sim.cpp ````
### ▶️ Run:
```` ./routing_sim inputfile.txt ````

## 📝 Input Format
First line: number of nodes n

Next n lines: space-separated adjacency matrix

        0 → No direct link (diagonal allowed)

        9999 → Infinite cost (unreachable)

## 📤 Output
For each node, the program prints:

DVR Table: shows destination, cost, and next hop after convergence

LSR Table: computed using Dijkstra’s algorithm
