class Connection:

    def __init__(self, id, MF, FD, OIR, RA, users):
        self._id = id
        self._MF = MF
        self._FD = FD
        self._OIR = OIR
        self._RA = RA
        self._users = users
        self._prob = self.calc_prob()

    def get_id(self):
        return self._id

    def get_prob(self):
        return self._prob

    def __repr__(self):
        res = "id: {}, MF: {}, FD: {}, OIR: {}, RA: {}, Users: {}".format(self._id, self._MF, self._FD, self._OIR, self._RA,
                                                                          self._users)
        return res

    def calc_prob(self):
        mf = 1 if self._MF >= 20 else (self._MF / 20)
        fd = 1 if self._FD >= 365 else (self._FD / 365)
        oir = 1 if self._OIR >= 1 else self._OIR
        return (mf + fd + oir + self._RA) / 4
