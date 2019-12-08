from DataSetSimulation import DataSetSimulation
from SocialGraph import SocialGraph
from random import choice
import matplotlib.pyplot as plt
import numpy as np


def calc_probs_all_paths(all_paths, graph, MSP=0.5):
    all_probs = {}
    number_of_found_paths = 0
    for path in all_paths:
        mult = 1
        for i in range(1, len(path)):
            mult *= graph.get_users()[path[i]].get_prob()
            mult *= graph.get_connections()[(path[i-1], path[i])].get_prob()
        all_probs[tuple(path)] = mult
    for path in all_paths:
        mult = all_probs[tuple(path)]
        if mult >= MSP:
            number_of_found_paths += 1
            print("the mult is: ", mult, "the path is: ", path)
        else:
            print("can't find, the mult is:", mult, "the path is: ", path)
    return number_of_found_paths


def main():
    MSPs = np.linspace(0.1, 1, 10)
    MSPs_dict = {MSP: 0 for MSP in MSPs}
    for i in range(100):
        for MSP in MSPs_dict.keys():
            simulation = DataSetSimulation("vertices.csv", "edges.csv", "parameters.json")
            simulation.generate_vertices_file()
            simulation.generate_edges_file()
            graph = SocialGraph("vertices.csv", "edges.csv")
            random_connection = choice(list(graph.get_connections().keys()))
            all_paths = graph.find_all_paths(random_connection[0], random_connection[1])
            MSPs_dict[MSP] += calc_probs_all_paths(all_paths, graph, MSP=MSP)
    sorted_MSPs_keys = [key for (key, value) in sorted(MSPs_dict.items())]
    sorted_MSPs_values = [value for (key, value) in sorted(MSPs_dict.items())]
    plt.plot(sorted_MSPs_keys, sorted_MSPs_values, 'bo')
    plt.xlabel('MSP values')
    plt.ylabel('number of paths found in 100 runs')
    plt.show()


if __name__ == "__main__":
    main()
