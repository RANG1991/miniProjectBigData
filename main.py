from DataSetSimulation import DataSetSimulation
from SocialGraph import SocialGraph


def main():
    simulation = DataSetSimulation("vertices.csv", "edges.csv", "parameters.json")
    simulation.generate_vertices_file()
    simulation.generate_edges_file()
    graph = SocialGraph("vertices.csv", "edges.csv")
    print(graph.find_all_paths("395d901d", "8e2755a1"))


if __name__ == "__main__":
    main()
