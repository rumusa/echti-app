import mysql.connector
import echti.config


class DBHelper(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBHelper, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user=echti.config.mysql_username,
            passwd=echti.config.mysql_password
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute("SHOW DATABASES")
        for db_name in self.cursor:
            print(db_name)
        # if echti.config.db_name not in self.cursor:
        #     self.cursor.execute("CREATE DATABASE " + echti.config.db_name)

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
