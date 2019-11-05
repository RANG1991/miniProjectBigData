from DataSetSimulation import DataSetSimulation
from SocialGraph import SocialGraph
from random import choice


def main():
    simulation = DataSetSimulation("vertices.csv", "edges.csv", "parameters.json")
    simulation.generate_vertices_file()
    simulation.generate_edges_file()
    graph = SocialGraph("vertices.csv", "edges.csv")
    random_connection = choice(list(graph.get_connections().keys()))
    for path in graph.find_all_paths(random_connection[0], random_connection[1]):
        print(path)


if __name__ == "__main__":
    main()
