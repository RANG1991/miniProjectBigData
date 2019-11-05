import csv
from User import User
from Connection import Connection


class SocialGraph:

    def __init__(self, vertices_file, edges_file):
        self._graph = {}
        self._connections_by_ids = {}
        self._users_by_ids = {}
        vertices_reader = csv.reader(open(vertices_file, "r"), delimiter=',', quotechar='"')
        edges_reader = csv.reader(open(edges_file, "r"), delimiter=",", quotechar='"')
        for row in vertices_reader:
            if row:
                print(row)
                user_id = row[0]
                user = User(user_id, int(row[1]), int(row[2]), int(row[3]))
                self._graph[user_id] = []
                self._users_by_ids[user_id] = user
        for row in edges_reader[1:]:
            if row:
                users_ids = tuple(row[1].split(":"))
                connection = Connection(row[0], row[2], row[3], row[4], row[5], tuple())
                self._connections_by_ids[users_ids] = connection
                self._graph[users_ids[0]].append(users_ids[1])
                self._graph[users_ids[1]].append(users_ids[0])

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

