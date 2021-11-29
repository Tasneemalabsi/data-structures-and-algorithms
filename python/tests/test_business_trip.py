from graph.business_trip.business_trip import Graph, Vertex, business_trip
import pytest

def test_business_trip_true():
    graph =Graph()
    node1=graph.add_node('Metroville')
    node2=graph.add_node('Pandora')
    graph.add_edge(node1,node2,82)
    expected = True, f"${82}"
    actual = business_trip(graph, [node1,node2])
    assert actual == expected

def test_business_trip_false():
    graph =Graph()
    node1=graph.add_node('Naboo')
    node2=graph.add_node('Pandora')
    expected = False, f"${0}"
    actual = business_trip(graph, [node1,node2])
    assert actual == expected

def test_business_trip_empty_graph():
    graph =Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    with pytest.raises(Exception):
        business_trip(graph,[v1, v2])

def test_business_trip_empty_array():
    graph =Graph()
    node1=graph.add_node('Metroville')
    node2=graph.add_node('Pandora')
    with pytest.raises(Exception):
        business_trip(graph,[])

def test_business_trip_city_not_in_graph():
    graph =Graph()
    node1=graph.add_node('Metroville')
    node2=graph.add_node('Pandora')
    v= Vertex('amman')
    with pytest.raises(Exception):
        business_trip(graph,[node1, node2, v])

