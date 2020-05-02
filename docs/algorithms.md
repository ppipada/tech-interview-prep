# Algorithms

## Sorting

### Quicksort

- Stable: `No`

Time Complexity:

| Operation    | Complexity   |
| ------------ | ------------ |
| Best Case    | `O(nlog(n))` |
| Worst Case   | `O(n^2)`     |
| Average Case | `O(nlog(n))` |

![Alt text](images/quicksort.gif?raw=true "Quicksort")

### Mergesort

- _Mergesort_ is also a divide and conquer algorithm. It continuously divides an array into two halves, recurses on both the left subarray and right subarray and then merges the two sorted halves
- Stable: `Yes`

Time Complexity:

| Operation    | Complexity   |
| ------------ | ------------ |
| Best Case    | `O(nlog(n))` |
| Worst Case   | `O(nlog(n))` |
| Average Case | `O(nlog(n))` |

![Alt text](images/mergesort.gif?raw=true "Mergesort")

### Bucket Sort

- _Bucket Sort_ is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm

Time Complexity:

| Operation    | Complexity |
| ------------ | ---------- |
| Best Case    | `Ω(n + k)` |
| Worst Case   | `O(n^2)`   |
| Average Case | `Θ(n + k)` |

![Alt text](images/bucketsort.png?raw=true "Bucket Sort")

### Radix Sort

- _Radix Sort_ is a sorting algorithm that like bucket sort, distributes elements of an array into a number of buckets. However, radix sort differs from bucket sort by 're-bucketing' the array after the initial pass as opposed to sorting each bucket and merging

Time Complexity:

| Operation    | Complexity |
| ------------ | ---------- |
| Best Case    | `Ω(nk)`    |
| Worst Case   | `O(nk)`    |
| Average Case | `Θ(nk)`    |

## Graph Algorithms

### Depth First Search

- _Depth First Search_ is a graph traversal algorithm which explores as far as possible along each branch before backtracking
- Time Complexity: `O(|V| + |E|)`

![Alt text](images/dfsbfs.gif?raw=true "DFS / BFS Traversal")

### Breadth First Search

- _Breadth First Search_ is a graph traversal algorithm which explores the neighbor nodes first, before moving to the next level neighbors
- Time Complexity: `O(|V| + |E|)`

![Alt text](images/dfsbfs.gif?raw=true "DFS / BFS Traversal")

### Topological Sort

- _Topological Sort_ is the linear ordering of a directed graph's nodes such that for every edge from node u to node v, u comes before v in the ordering
- Time Complexity: `O(|V| + |E|)`

### Dijkstra's Algorithm

- _Dijkstra's Algorithm_ is an algorithm for finding the shortest path between nodes in a graph
- Time Complexity: `O(|V|^2)`

![Alt text](images/dijkstra.gif?raw=true "Dijkstra's")

### Bellman-Ford Algorithm

- _Bellman-Ford Algorithm_ is an algorithm that computes the shortest paths from a single source node to all other nodes in a weighted graph
- Although it is slower than Dijkstra's, it is more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers
- Time Complexity:
  - Best Case: `O(|E|)`
  - Worst Case: `O(|V||E|)`

![Alt text](images/bellman-ford.gif?raw=true "Bellman-Ford")

### Floyd-Warshall Algorithm

- _Floyd-Warshall Algorithm_ is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights, but no negative cycles
- A single execution of the algorithm will find the lengths (summed weights) of the shortest paths between _all_ pairs of nodes
- Time Complexity:
  - Best Case: `O(|V|^3)`
  - Worst Case: `O(|V|^3)`
  - Average Case: `O(|V|^3)`

### Prim's Algorithm

- _Prim's Algorithm_ is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. In other words, Prim's find a subset of edges that forms a tree that includes every node in the graph
- Time Complexity: `O(|V|^2)`

![Alt text](images/prim.gif?raw=true "Prim's Algorithm")

### Kruskal's Algorithm

- _Kruskal's Algorithm_ is also a greedy algorithm that finds a minimum spanning tree in a graph. However, in Kruskal's, the graph does not have to be connected
- Time Complexity: `O(|E|log|V|)`

![Alt text](images/kruskal.gif?raw=true "Kruskal's Algorithm")

## Greedy Algorithms

- _Greedy Algorithms_ are algorithms that make locally optimal choices at each step in the hope of eventually reaching the globally optimal solution
- Problems must exhibit two properties in order to implement a Greedy solution:
  - Optimal Substructure
    - An optimal solution to the problem contains optimal solutions to the given problem's subproblems
  - The Greedy Property
    - An optimal solution is reached by "greedily" choosing the locally optimal choice without ever reconsidering previous choices
- Example: [Coin Change](all-problems/coin-change.md)

## Bitmasks

- Bitmasking is a technique used to perform operations at the bit level. Leveraging bitmasks often leads to faster runtime complexity and helps limit memory usage.

| Operation                 | Expression                |
| ------------------------- | ------------------------- |
| Test kth bit              | `s & (1 << k);`           |
| Set kth bit               | `s |= (1 << k);`          |
| Turn off kth bit          | `s &= ~(1 << k);`         |
| Toggle kth bit            | `s ^= (1 << k);`          |
| Multiple by 2<sup>n</sup> | `s << n;`                 |
| Divide by 2<sup>n</sup>   | `s >> n;`                 |
| Intersection              | `s & t;`                  |
| Union                     | `s | t;`                  |
| Set Subtraction           | `s & ~t;`                 |
| Extract lowest set bit    | `s & (-s);`               |
| Extract lowest unset bit  | `~s & (s + 1);`           |
| Swap Values               | `x ^= y; y ^= x; x ^= y;` |
