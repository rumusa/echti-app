from distutils.command.config import config
import mysql.connector
import echti.config

class DBHelper(object):
    _conn = None
    cursor = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBHelper, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if self._conn is None:
            self._conn = mysql.connector.connect(
                host = "localhost",
                user = echti.config.mysql_username,
                passwd = echti.config.mysql_password
            )
        self.cursor = self._conn.cursor()
        self.cursor.execute("SHOW DATABASES")
        # for db_name in self.cursor:
            # print(db_name)
        if echti.config.db_name not in self.cursor:
            self.cursor.execute("CREATE DATABASE " + echti.config.db_name)
        
    def __del__(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None
