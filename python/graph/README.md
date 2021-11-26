# Graphs

A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges.

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods: add node, add edge, get nodes, get neighbors, size


## Approach & Efficiency

- create a class for queue, stack, vertix (node), edge and graph
- add the following methods to the graph class:

- for add_node() method:

                    big O of n for time // O(1) -> constant

                    big O of n for space // O(1) -> constant

- for size() method:

                       big O of n for time // O(n) -> linear

                       big O of n for space // O(1) -> constant

-  for add_edge() method:

                        big O of n for time // O(1) -> constant

                        big O of n for space // O(1) -> constant
-  for get_nodes() method:

                       big O of n for time // O(n) -> linear

                       big O of n for space // O(1) -> constant

-  for get_neighbors() method:

                        big O of n for time // O(n) -> linear

                        big O of n for space // O(1) -> constant
- for breadth_first_search() method:

                        big O of n for time // O(n^2)

                        big O of n for space // O(n) -> linear

## API
- add_node() method: adds a new node to the graph
- size() method: returns the length of the graph
- add_edge method : adds a new edge to the graph connected to a certain input node
- get_nodes() method : returns all of the nodes in the graph
- get_neighbors() method: returns all of the nodes that are connected to a certain input node by an edge
- breadth_first_search() method: returns all of the values stored inside the graph's nodes .
