import csv
from User import User
from Connection import Connection
import networkx as nx
import matplotlib.pyplot as plt


class SocialGraph:

    def __init__(self, vertices_file, edges_file):
        self._graph = {}
        self._connections_by_ids = {}
        self._users_by_ids = {}
        node_labels = {}
        edge_labels = {}
        vertices_reader = csv.reader(open(vertices_file, "r"), delimiter=',', quotechar='"')
        next(vertices_reader, None)
        edges_reader = csv.reader(open(edges_file, "r"), delimiter=",", quotechar='"')
        next(edges_reader, None)
        for row in vertices_reader:
            if row:
                user_id = row[0]
                user = User(user_id, int(row[1]), int(row[2]), float(row[3]))
                self._graph[user_id] = []
                self._users_by_ids[user_id] = user
                node_labels[user_id] = "{0:.2f}".format(user.get_prob())
        for row in edges_reader:
            if row:
                users_ids = tuple(row[1].split(":"))
                connection = Connection(row[0], int(row[2]), int(row[3]), float(row[4]), float(row[5]), users_ids)
                self._connections_by_ids[users_ids] = connection
                self._graph[users_ids[0]].append(users_ids[1])
                edge_labels[users_ids] = "{0:.2f}".format(connection.get_prob())
        g = nx.DiGraph(self._graph)
        pos = nx.spring_layout(g)
        plt.figure()
        nx.draw_networkx_labels(g, pos, labels=node_labels)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='red')
        nx.draw_networkx(g, arrows=True, node_size=500, with_labels=True)
        plt.show()

    def get_dict_graph(self):
        return self._graph

    def get_connections(self):
        return self._connections_by_ids

    def get_users(self):
        return self._users_by_ids

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self._graph.keys():
            return []
        paths = []
        for node in self._graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


