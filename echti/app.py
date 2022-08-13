from echti.auth.user import User
from echti.model.db_helper import DBHelper

def run():
    print('DB Helper')
    db_conn = DBHelper(r'echti/db/main.db')
    print('DB Helper End')