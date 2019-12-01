import csv
from random import randrange, uniform, choice
import uuid
import json


class DataSetSimulation:
    def __init__(self, vertices_file, edges_file, params_file):
        self._output_filename_vertices = vertices_file
        self._output_filename_edges = edges_file
        with open(params_file) as f:
            self._paramsJson = json.load(f)
        self._users_ids = []

    def generate_vertices_file(self):
        csv_file_vertices = open(self._output_filename_vertices, 'w')
        vertices_file_writer = csv.writer(csv_file_vertices, delimiter=',', quotechar='"')
        vertices_file_writer.writerow(["ID", "TF", "AUA", "FFR"])
        number_of_users = int(self._paramsJson["users"]["number"])
        params = self._paramsJson["users"]["params"]
        TF = params["TF"]
        AUA = params["AUA"]
        FFR = params["FFR"]
        for i in range(number_of_users):
            id_to_write = uuid.uuid4().hex[:8]
            tf_to_write = randrange(TF["min"], TF["max"], TF["step"])
            aua_to_write = randrange(AUA["min"], AUA["max"], AUA["step"])
            ffr_to_write = uniform(FFR["min"], FFR["max"])
            self._users_ids.append(id_to_write)
            vertices_file_writer.writerow([id_to_write, tf_to_write, aua_to_write, ffr_to_write])
        csv_file_vertices.close()

    def generate_edges_file(self):
        csv_file_edges = open(self._output_filename_edges, 'w')
        vertices_file_writer = csv.writer(csv_file_edges, delimiter=',', quotechar='"')
        vertices_file_writer.writerow(["ID", "users_IDs", "MF", "FD", "OIR", "RA"])
        number_of_connections = int(self._paramsJson["connections"]["number"])
        params = self._paramsJson["connections"]["params"]
        MF = params["MF"]
        FD = params["FD"]
        P_RA = params["P_RA"]
        OIR = params["OIR"]
        connections_generator = self.get_rand_connections()
        for i in range(number_of_connections):
            id_to_write = uuid.uuid4().hex[:8]
            mf_to_write = randrange(MF["min"], MF["max"], MF["step"])
            fd_to_write = randrange(FD["min"], FD["max"], FD["step"])
            p_ra_to_write = uniform(P_RA["min"], P_RA["max"])
            oir_to_write = uniform(OIR["min"], OIR["max"])
            edge_to_write = next(connections_generator)
            edge_to_write = edge_to_write[0] + ":" + edge_to_write[1]
            vertices_file_writer.writerow([id_to_write, edge_to_write, mf_to_write, fd_to_write, oir_to_write, p_ra_to_write])
        csv_file_edges.close()

    def get_rand_connections(self):
        seen = set()
        x, y = choice(self._users_ids), choice(self._users_ids)
        while True:
            seen.add((x, y))
            yield (x, y)
            x, y = choice(self._users_ids), choice(self._users_ids)
            while (x, y) in seen or x is y:
                x, y = choice(self._users_ids), choice(self._users_ids)




