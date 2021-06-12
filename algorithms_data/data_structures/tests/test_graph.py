"""
Module for testing graph.py
"""

import pytest

from algorithms_data.data_structures.graph import Graph


friend_list = ['Dim', 'Nik', 'Margo', 'Eugen', 'Vlada', 'Dan', 'Roma', 'Alex', 'Max', 'Artem']


@pytest.fixture
def test_graph():
    test_graph = Graph()
    for i in friend_list:
        test_graph.add_node(i)
    test_graph.create_connection('Dim', 'Roma')
    test_graph.create_connection('Nik', 'Eugen')
    test_graph.create_connection('Nik', 'Vlada')
    test_graph.create_connection('Margo', 'Eugen')
    test_graph.create_connection('Dan', 'Roma')
    test_graph.create_connection('Alex', 'Artem')
    test_graph.create_connection('Max', 'Dim')
    return test_graph


def test_str_nodes(test_graph):
    graph_string = ''
    for i in test_graph.nodes:
        graph_string += f"{i}, "
    assert graph_string == 'Dim, Nik, Margo, Eugen, Vlada, Dan, Roma, Alex, Max, Artem, '


def test_str_edges(test_graph):
    edges_list = []
    for i in test_graph.edges:
        edges_list.append(i)
    assert edges_list == [('Dim', 'Roma'), ('Nik', 'Eugen'), ('Nik', 'Vlada'), ('Margo', 'Eugen'),
                          ('Dan', 'Roma'), ('Alex', 'Artem'), ('Max', 'Dim')]


def test_lookup(test_graph):
    with pytest.raises(ValueError):
        test_graph.lookup('Some guy')
    assert test_graph.lookup('Nik') == "The node with value 'Nik' has index <1>"


def test_show_node_connections(test_graph):
    assert test_graph.show_node_connections('Dim') == "('Dim', 'Roma') ('Max', 'Dim') "
    assert test_graph.show_node_connections('Dan') == "('Dan', 'Roma') "


def test_add_node(test_graph):
    test_graph.add_node('Some chick')
    assert test_graph.lookup('Some chick') == "The node with value 'Some chick' has index <10>"
    with pytest.raises(ValueError):
        test_graph.add_node('Nik')


def test_create_connection(test_graph):
    test_graph.create_connection('Nik', 'Max')
    assert ('Nik', 'Max') in test_graph.edges
    assert test_graph.edges[len(test_graph.edges) - 1] == ('Nik', 'Max')
    assert test_graph.show_node_connections('Nik') == "('Nik', 'Eugen') ('Nik', 'Vlada') ('Nik', 'Max') "
    with pytest.raises(ValueError):
        test_graph.create_connection('Nik', 'Vlada')
    with pytest.raises(ValueError):
        test_graph.create_connection('Some chick', 'Some guy')


def test_disconnect(test_graph):
    assert test_graph.show_node_connections('Dim') == "('Dim', 'Roma') ('Max', 'Dim') "
    test_graph.disconnect('Dim', 'Roma')
    assert test_graph.show_node_connections('Dim') == "('Max', 'Dim') "
    with pytest.raises(ValueError):
        test_graph.disconnect('Some guy', 'Margo')


def test_delete_node(test_graph):
    assert test_graph.lookup('Nik') == "The node with value 'Nik' has index <1>"
    assert test_graph.show_node_connections('Nik') == "('Nik', 'Eugen') ('Nik', 'Vlada') "
    test_graph.delete_node('Nik')
    assert 'Nik' not in test_graph.nodes
    assert ('Nik', 'Eugen') and ('Nik', 'Vlada') not in test_graph.edges
    with pytest.raises(ValueError):
        test_graph.delete_node('Some guy')
