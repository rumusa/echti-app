import sqlite3

class DBHelper(object):
    _conn = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBHelper, cls).__new__(cls)
        return cls.instance

    def __init__(self, db_file):
        if self._conn is None:
            self._conn = sqlite3.connect(db_file)
        self.cursor = self._conn.cursor()

    def __del__(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None
        