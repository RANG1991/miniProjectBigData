class User:

    def __init__(self, id, TF, AUA, FFR):
        self._id = id
        self._TF = TF
        self._AUA = AUA
        self._FFR = FFR
        self._connections = []

    def add_connection(self, connection):
        self._connections.append(connection)

    def get_connections(self):
        return self._connections

    def get_id(self):
        return self._id

    def __repr__(self):
        res = "id: {}, TF: {}, AUA: {}, FFR: {}".format(self._id, self._TF, self._AUA, self._FFR)
        for connection in self._connections:
            res += "\n" + connection.__repr__
        return res
