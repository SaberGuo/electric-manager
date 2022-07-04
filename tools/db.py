import sqlite3


class ElectricDatabase(object):
    def __init__(self, db = "em.sqlite"):
        self.db = db
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()

    