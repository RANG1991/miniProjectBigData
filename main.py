from DataSetSimulation import DataSetSimulation
from SocialGraph import SocialGraph
from random import choice


def calc_probs_all_paths(all_paths, graph, MSP=0.9):
    all_probs = {}
    for path in all_paths:
        mult = 1
        for i in range(1, len(path)):
            mult *= graph.get_users()[path[i]].get_prob()
            mult *= graph.get_connections()[(path[i-1], path[i])].get_prob()
        all_probs[tuple(path)] = mult
        if mult >= MSP:
            print("the mult is: ", mult)
            return True
    print("can't found!")
    return False

def main():
    for i in range(10):
        simulation = DataSetSimulation("vertices.csv", "edges.csv", "parameters.json")
        simulation.generate_vertices_file()
        simulation.generate_edges_file()
        graph = SocialGraph("vertices.csv", "edges.csv")
        random_connection = choice(list(graph.get_connections().keys()))
        all_paths = graph.find_all_paths(random_connection[0], random_connection[1])
        calc_probs_all_paths(all_paths, graph)


if __name__ == "__main__":
    main()
