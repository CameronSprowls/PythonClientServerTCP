"""
Python 3
Cameron Sprowls

Yes, I did already submit this on accident, I thought there was going to be a spot to rename the file before
it just updated. My bad.
"""
import re
from random import randint


class Graph:
    @staticmethod
    def num_vertices(vertices):
        """
        Function to counter the number of vertices in the graph does
        So by counting unique number of keys.
        :param vertices A list of the vertices in a graph.
        """
        print("Number of vertices in the graph: ", len(vertices))

    @staticmethod
    def num_edges(list_edges):
        """
        Returns number of edges in the list of edges provided
        :param list_edges A list of the edges in the graph.
        """
        print("Number of edges in the graph:    ", int(len(list_edges)/2))

    @staticmethod
    def degree_sequence(edges):
        """
        Returns degree sequence of graph
        :param edges List of the edges in the graph to be checked
        :return int That is the degree sequence.
        """
        print("Degree Sequence:                  ", end="")
        counter = 0
        marker = edges[1][:1]
        for x in edges:
            if x[:1] == marker:
                counter += 1
            else:
                print(counter, "", end='')
                marker = x[:1]
                counter = 1
        print(counter, "")

    @staticmethod
    def eulerian(edges):
        """
        Checks to see if the graph is Eulerian by checking
        The degrees of all nodes if all are even, the graph is
        Eulerian, else, false. If is it, return that circuit.
        :param edges List of edges in the graph, can be useful
        :return boolean Whether the graph is Eulerian or not.
        """
        # Checking to see if the graph as any odd vertices, if it does, return false
        counter = 0
        temp_key = ""
        for x in edges:
            if x[:1] == temp_key:
                counter += 1
                continue
            else:
                temp_key = x[:1]
                if counter % 2 == 1:
                    print("The graph is not Eulerian because there is at least "
                          "one edge that has an odd number of vertices")
                    return False
                counter += 1

        current_circuit = []
        temp_circuit = []
        current_vertex = edges[randint(0, len(edges)-1)]

        # Go through list of edges and keep track of any sub-circuits found, they will form Eulerian circuit
        while len(edges) > 0:
            edges.remove(current_vertex)
            edges.remove(current_vertex[::-1])
            temp_circuit.append(current_vertex)
            for x in edges:
                if x[:1] == current_vertex[2:]:
                    current_vertex = x
                    break
            if current_vertex[2:] == temp_circuit[0][:1]:
                temp_circuit.append(current_vertex)
                current_circuit.append(temp_circuit)
                edges.remove(current_vertex)
                edges.remove(current_vertex[::-1])
                temp_circuit = []
                if len(edges) == 0:
                    break
                else:
                    current_vertex = edges[0]

        # Rebuilding the sub-circuits to one big circuit
        final_circuit = current_circuit.pop(0)
        while len(current_circuit) > 0:
            for x in current_circuit:
                skip_next = False
                for y in x:
                    if skip_next:
                        continue
                    for z in final_circuit:
                        if skip_next:
                            continue
                        if y[:1] is z[2:]:
                            counter = 1
                            for a in x:
                                final_circuit.insert(final_circuit.index(z)+counter, a)
                                counter += 1
                            skip_next = True
                            current_circuit.remove(x)
                            continue
                if len(x) is 0:
                    current_circuit.remove(x)
        print("The graph is Eulerian as follows:")
        print(final_circuit)
        return

    @staticmethod
    def bipartite(edges):
        """
        Check to see if the graph is bipartite. If it is, returns proper coloring.
        :param edges List of all of the edges in the graph that is to be checked.
        """
        current_vertex = edges[0][:1]
        color_one = [current_vertex]
        color_two = []

        # Assign each node a color, and assign its connected nodes the opposite color
        for x in edges:
            current_vertex = x[:1]
            # edges.remove(x)
            if x[:1] == current_vertex:
                if current_vertex in color_one:
                    if x[2:] in color_two:
                        continue
                    color_two.append(x[2:])
                if current_vertex in color_two:
                    if x[2:] in color_one:
                        continue
                    color_one.append(x[2:])

        # Check to see is any node is of improper color, if it is, return false
        for x in color_two:
            if x in color_one:
                print("The graph is not bipartite.")
                return False

        print("The graph is bipartite as follows: ")
        print("Color 1:", color_one, " ", "Color 2:", color_two)

    @staticmethod
    def main():
        # Get graph input form the user
        vertices = input("Enter vertices (a, b, c): ")
        edges = input("Enter edges between vertices (a-b, a-c, b-c): ")

        # Move vertices and edges to a more accessible list
        vertices = re.split(', |\n', vertices)
        edges = re.split(', |\n', edges)

        # Create every possible edge, not just the edges input
        temp_list = []
        for x in edges:
            temp_list.append(x)
            temp_list.append(x[2:] + x[1:2] + x[:1])

        # Print everything
        print("---Info for graph---")
        edges = sorted(temp_list)
        Graph().num_vertices(vertices)
        Graph().num_edges(edges)
        Graph().degree_sequence(edges)
        print()
        Graph().bipartite(edges)
        edges = sorted(temp_list)
        print()
        Graph().eulerian(edges)
        print("---Analysis completed---")

Graph().main()
