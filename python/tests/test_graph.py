import pytest
from graph.graph import  Edge, Graph, Vertex

# Node can be successfully added to the graph
def test_add_node_to_graph():
  graph = Graph()
  expected = "1"
  actual = graph.add_node('1').value
  assert actual == expected

# An edge can be successfully added to the graph
def test_add_edge_to_graph():

    graph = Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    graph.add_edge(node1,node2)
    actual = graph.get_neighbors(node1)[0].vertex.value
    expected = 2
    assert actual == expected


# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes():
    graph =Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    node3=graph.add_node(3)
    node4=graph.add_node(4)
    arr = []
    for i in range(len(list(graph.get_nodes()))):
        val=list(graph.get_nodes())[i].value
        arr.append(val)
    expected = [1,2,3,4]
    actual = arr
    assert actual == expected

# All appropriate neighbors can be retrieved from the graph
def test_get_neighbors():
    graph=Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    node3=graph.add_node(3)
    node4=graph.add_node(4)
    graph.add_edge(node1,node2)
    graph.add_edge(node1,node3)
    graph.add_edge(node1,node4)
    arr = []
    for i in range(len(graph.get_neighbors(node1))):
        arr.append(graph.get_neighbors(node1)[i].vertex.value)
    actual = arr
    expected = [2,3,4]
    assert actual == expected

# Neighbors are returned with the weight between nodes included
def test_get_neighbors_with_weights():

    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3=graph.add_node(3)
    graph.add_edge(node1,node2,20)
    graph.add_edge(node1,node3,30)

    arr_of_neighbor_values = []
    arr_of_weights = []

    for i in range(len(graph.get_neighbors(node1))):
        arr_of_neighbor_values.append(graph.get_neighbors(node1)[i].vertex.value)
        arr_of_weights.append(graph.get_neighbors(node1)[i].weight)

    actual1 = arr_of_neighbor_values
    actual2 = arr_of_weights

    assert actual1 == [2,3]
    assert actual2 == [20,30]


# The proper size is returned, representing the number of nodes in the graph
def test_graph_size():

    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3=graph.add_node(3)
    actual = graph.size()
    assert actual == 3

# A graph with only one node and edge can be properly returned
def test_graph_with_one_node():

    graph = Graph()
    node1 = graph.add_node(1)
    actual = graph.breadth_first_search(node1)
    assert actual == {1}

# An empty graph properly returns null
def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    expected = None
    assert actual == expected




