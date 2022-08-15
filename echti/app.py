from echti.auth.user import User
from echti.db.helper import DBHelper

def run():
    db_conn = DBHelper()
    db_conn.__del__()
    