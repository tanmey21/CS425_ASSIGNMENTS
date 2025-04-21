#include <iostream>
#include <vector>
#include <limits>
#include <queue>
#include <fstream>
#include <sstream>
#include <iomanip>
#define arr array<int,2>

using namespace std;

const int INF = 9999;

void printDVRTable(int node, const vector<vector<int>>& table, const vector<vector<int>>& nextHop) {
    cout << "Node " << node << " Routing Table:\n";
    cout << "Dest\tCost\tNext Hop\n";
    for (int i = 0; i < table.size(); ++i) {
        cout << i << "\t" << table[node][i] << "\t";
        if (nextHop[node][i] == -1) cout << "-";
        else cout << nextHop[node][i];
        cout << endl;
    }
    cout << endl;
}

void simulateDVR(const vector<vector<int>>& graph) {
    int n = graph.size();
    vector<vector<int>> dist = graph;
    vector<vector<int>> nextHop(n, vector<int>(n, -1));

    // Initialize next-hop table for directly connected nodes
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            // if there is a direct link (non-zero, non-INF)
            if (graph[i][j] != 0 && graph[i][j] != INF) {
                nextHop[i][j] = j;
            }
        }
        // cost to itself is always zero
        dist[i][i] = 0;
    }

    // Iteratively update distance vectors until no change
    bool updated;
    do {
        updated = false;
        // for each source node i
        for (int i = 0; i < n; ++i) {
            // for each neighbor k of i
            for (int k = 0; k < n; ++k) {
                if (graph[i][k] != 0 && graph[i][k] != INF) {
                    // for each destination j
                    for (int j = 0; j < n; ++j) {
                        // if path through k is shorter, update
                        if (dist[k][j] != INF && graph[i][k] + dist[k][j] < dist[i][j]) {
                            dist[i][j] = graph[i][k] + dist[k][j];
                            nextHop[i][j] = k;
                            updated = true;
                        }
                    }
                }
            }
        }
    } while (updated);

    cout << "--- DVR Final Tables ---\n";
    for (int i = 0; i < n; ++i) {
        printDVRTable(i, dist, nextHop);
    }
}

void printLSRTable(int src, const vector<int>& dist, const vector<int>& prev) {
    cout << "Node " << src << " Routing Table:\n";
    cout << "Dest\tCost\tNext Hop\n";
    for (int i = 0; i < dist.size(); ++i) {
        if (i == src) continue;
        cout << i << "\t" << dist[i] << "\t";
        int hop = i;
        while (prev[hop] != src && prev[hop] != -1)
            hop = prev[hop];
        cout << (prev[hop] == -1 ? -1 : hop) << endl;
    }
    cout << endl;
}

void simulateLSR(const vector<vector<int>>& graph) {
    int n = graph.size();
    for (int src = 0; src < n; ++src) {
        vector<int> dist(n, INF);
        vector<int> prev(n, -1);
        vector<bool> visited(n, false);
        dist[src] = 0;
        
         //TODO: Complete this
        // min-heap priority queue: (distance, node)
        priority_queue<arr, vector<arr>, greater<arr>> pq;
        pq.push({0, src});

        // Dijkstra's algorithm
        while (!pq.empty()) {
            auto f = pq.top();
            auto distance=f[0];
            auto node=f[1];
            pq.pop();
            // relax edges from 'node' to every other node x
            for (int x = 0; x < n; ++x) {
                if (x == node) continue;
                int new_dis = distance + graph[x][node];
                if (new_dis < dist[x]) {
                    dist[x] = new_dis;
                    prev[x] = node;
                    pq.push({new_dis, x});
                }
            }
        }

        // print routing table for this source
        
        printLSRTable(src, dist, prev);
    }
}

vector<vector<int>> readGraphFromFile(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error: Could not open file " << filename << endl;
        exit(1);
    }
    
    int n;
    file >> n;
    vector<vector<int>> graph(n, vector<int>(n));

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            file >> graph[i][j];

    file.close();
    return graph;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <input_file>\n";
        return 1;
    }

    string filename = argv[1];
    vector<vector<int>> graph = readGraphFromFile(filename);

    cout << "\n--- Distance Vector Routing Simulation ---\n";
    simulateDVR(graph);

    cout << "\n--- Link State Routing Simulation ---\n";
    simulateLSR(graph);

    return 0;
}

