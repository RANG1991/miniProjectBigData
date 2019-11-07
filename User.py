class User:

    def __init__(self, id, TF, AUA, FFR):
        self._id = id
        self._TF = TF
        self._AUA = AUA
        self._FFR = FFR
        self._prob = self.calc_prob()

    def get_id(self):
        return self._id

    def get_prob(self):
        return self._prob

    def __repr__(self):
        res = "id: {}, TF: {}, AUA: {}, FFR: {}".format(self._id, self._TF, self._AUA, self._FFR)
        return res

    def calc_prob(self):
        tf = 1 if self._TF >= 100 else (self._TF / 100)
        aua = 1 if self._AUA >= 365 else (self._AUA / 365)
        ffr = 1 if self._FFR >= 1 else self._FFR
        return (tf + aua + ffr) / 3

