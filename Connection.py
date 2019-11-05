class Connection:

    def __init__(self, id, MF, FD, OIR, RA, users):
        self._id = id
        self._MF = MF
        self._FD = FD
        self._OIR = OIR
        self._RA = RA
        self._users = users

    def get_id(self):
        return self._id

    def __repr(self):
        res = "id: {}, MF: {}, FD: {}, OIR: {}, RA: {}, Users: {}".format(self._id, self._MF, self._FD, self._OIR, self._RA,
                                                                          self._users)
        return res