from DataSetSimulation import DataSetSimulation
from SocialGraph import SocialGraph
from random import choice
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


def calc_probs_all_paths(all_paths, graph, edges_in_path, MSP=0.5):
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
            edges_in_path.extend([(path[i-1], path[i]) for i in range(1, len(path))])
            number_of_found_paths += 1
            print("the mult is: ", mult, "the path is: ", path)
        else:
            print("can't find, the mult is:", mult, "the path is: ", path)
    return number_of_found_paths


def draw_final_graph(graph, edges_in_paths, ego_node, target_node):
    g = nx.DiGraph(graph.get_dict_graph(), directed=True)
    pos = nx.spring_layout(g)
    colors_nodes_dict = {ego_node: "r", target_node: "g"}
    colors_edges = ["r" if edge in edges_in_paths else "b" for edge in g.edges()]
    colors_nodes = [colors_nodes_dict.get(node, "b") for node in g.nodes]
    shifted_pos = {k: [v[0], v[1] + .04] for k, v in pos.items()}
    node_label_handles = nx.draw_networkx_labels(g, pos=shifted_pos,
                                                 labels=graph.get_node_labels(), font_size=8)
    [label.set_bbox(dict(facecolor='white', edgecolor='none')) for label in
     node_label_handles.values()]
    nx.draw_networkx_nodes(g, pos, node_color=colors_nodes, node_size=3000)
    nx.draw_networkx_edges(g, pos, edge_color=colors_edges, arrowsize=20, arrowstyle='->', node_size=5000)
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=graph.get_edge_labels())
    plt.show()


def main():
    MSPs = np.linspace(0.1, 1, 10)
    MSPs_dict = {MSP: 0 for MSP in MSPs}
    for i in range(1):
        for MSP in MSPs_dict.keys():
            simulation = DataSetSimulation("vertices.csv", "edges.csv", "parameters.json")
            simulation.generate_vertices_file()
            simulation.generate_edges_file()
            graph = SocialGraph("vertices.csv", "edges.csv")
            edges_in_paths = []
            random_connection = choice(list(graph.get_connections().keys()))
            all_paths = graph.find_all_paths(random_connection[0], random_connection[1])
            MSPs_dict[MSP] += calc_probs_all_paths(all_paths, graph, edges_in_paths, MSP=MSP)
            draw_final_graph(graph, edges_in_paths, random_connection[0], random_connection[1])
    sorted_MSPs_keys = [key for (key, value) in sorted(MSPs_dict.items())]
    sorted_MSPs_values = [value for (key, value) in sorted(MSPs_dict.items())]
    plt.plot(sorted_MSPs_keys, sorted_MSPs_values, 'bo')
    plt.xlabel('MSP values')
    plt.ylabel('number of paths found in 100 runs')
    plt.show()


if __name__ == "__main__":
    main()
