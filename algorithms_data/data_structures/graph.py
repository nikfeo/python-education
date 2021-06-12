"""
This module implements graph structure
"""

from algorithms_data.data_structures.linked_list import LinkedList, Node


class GraphNode(Node):
    """
    Describes GraphNode class, that inherits from Node
    """
    def __init__(self, data):
        super().__init__(data)

    def __iter__(self):
        item = self.data
        while item:
            yield item.data
            item = item.next_data


class Graph:
    """
    Describes Graph class
    """
    def __init__(self):
        self.nodes = LinkedList()
        self.edges = LinkedList()

    def __str__(self):
        cur_node = self.nodes.head
        output = ''
        while cur_node:
            output += str(cur_node.data) + ', '
            cur_node = cur_node.next_data
        output += '\n'

        cur_edge = self.edges.head
        while cur_edge:
            output += str(cur_edge.data) + ', '
            cur_edge = cur_edge.next_data
        if len(self.edges) == 0:
            output += 'No connections in this graph'
        return output

    def add_node(self, data):
        """
        Creates new node and adds it to the list 'nodes' of current graph
        """
        new_node = GraphNode(data)
        if self.nodes.lookup(data):
            raise ValueError('Node with such value is already in Graph')
        else:
            self.nodes.append(new_node.data)

    def show_node_connections(self, data):
        """
        Returns string of connections of specified node with other nodes
        """
        node_connections = ''
        for item in self.edges:
            if data in item:
                node_connections += str(item) + ' '
        return node_connections

    def delete_node(self, data):
        """
        Deletes node from the list 'nodes' and all connections
        from the list 'edges' of current graph
        """
        del_node = GraphNode(data)
        if del_node.data not in self.nodes:
            raise ValueError("The node does not exist")
        del_node_ind = self.nodes.lookup(del_node.data)
        if del_node.data in self.nodes:
            self.nodes.delete(del_node_ind)
        cur_connect = self.edges.head
        cur_index = 0
        while cur_connect:
            if data in cur_connect.data:
                self.edges.delete(cur_index)
            else:
                cur_index += 1
            cur_connect = cur_connect.next_data

    def lookup(self, data):
        """
        Prints data and index of node with specified data
        """
        node = GraphNode(data)
        if node.data in self.nodes:
            return f"The node with value '{node.data}' has index <{self.nodes.lookup(node.data)}>"
        else:
            raise ValueError('There is no node with such value in this graph')

    def create_connection(self, data1, data2):
        """
        Creates new connection between two nodes and adds this connection
        as tuple to the list 'edges' of current graph
        """
        new_node1 = GraphNode(data1)
        new_node2 = GraphNode(data2)
        if (new_node1.data, new_node2.data) in self.edges:
            raise ValueError("This connection is already exist")
        elif new_node1.data and new_node2.data in self.nodes:
            self.edges.append((new_node1.data, new_node2.data))
        else:
            raise ValueError("One of node does not exist")

    def disconnect(self, data1, data2):
        """
        Breakes connection between two nodes and
        deletes tuple with nodes data from list 'edge"
        """
        new_node1 = GraphNode(data1)
        new_node2 = GraphNode(data2)
        if (new_node1.data, new_node2.data) in self.edges:
            connection_index = self.edges.lookup((new_node1.data, new_node2.data))
            self.edges.delete(connection_index)
        else:
            raise ValueError(f"There no connection between nodes {new_node1.data} and {new_node2.data}")
