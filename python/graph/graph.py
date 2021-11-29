from collections import deque


class Vertex:
    """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """
    def __init__(self, value):
        """
    Initalization for a Vertex to hold a value.
    """
        self.value = value


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self,item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)
    def __len__(self):
        return len(self.data)


class Stack:
    def __init__(self):
        """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
		Store the passed value in a node and then push the node on top of the stack.
		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
        self.dq.append(value)

    def pop(self):
        """
		Return the top node in a stack.
		"""
        self.dq.pop()


class Edge:
    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
  """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
    Initalization for a hashmap to hold the vertices
    """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
        this method Adds a new node to the graph
        Arguments: value
        Returns: The added node
        """
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
        if not self.size():
            return None
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        this method gets the nodes that are connected to the input node by edges
        Arguments: Vertex
        Returns: list
        """
        return self.__adjacency_list.get(vertex, [])


    def breadth_first_search(self, start_vertex):
        """
        this method gets the values inside all of the nodes stored in the graph
        Args:
            start_vertex (Vertex object)
            action (function, optional): [description]. Defaults to (lambda vertex: None).
        Returns:
            set of values
        """
        if not start_vertex:
            raise Exception('no starting node')
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex.value)
        while len(queue):
            current_vertex = queue.dequeue()
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor.value)
                    queue.enqueue(neighbor)
        return visited

def business_trip(graph:Graph, arr):
    sum = 0
    result = False
    if not len(arr) or not graph.size:
        raise Exception("one of the inputs are empty, check it !! ")
    for city in arr:
        if city not in list(graph.get_nodes()):
            raise Exception("one or more of the cities you entered doesn't exist, check it !!")
        if graph.get_neighbors(city):
            for neighbor in graph.get_neighbors(city):
                if neighbor.vertex in arr:
                    result = True
                    sum = sum + neighbor.weight
    return result, f"${sum}"




if __name__ == "__main__":
    graph =Graph()
    node1=graph.add_node('1')
    node2=graph.add_node('2')
    node3=graph.add_node('3')
    node4=graph.add_node('4')
    graph.add_edge(node1,node2,40)
    graph.add_edge(node1,node3,40)
    graph.add_edge(node1,node4,22)
    graph.add_edge(node2,node3,12)
    n = Vertex(1)
    # print(graph.get_neighbors(node1)[0].vertex.value)
    print(business_trip(graph, [node4,n]))
    # queue = Queue()
    # queue.enqueue('1')
    # queue.enqueue('2')
    # queue.enqueue('3')
    # print(queue.dequeue())
