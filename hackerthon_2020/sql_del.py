import sqlite3
from config import config
from os import getcwd,path
# db_path=path.join(getcwd(),"sqlite.db")
db_path=config['db_path']
try:
    con = sqlite3.connect(db_path)
    try:
        cur=con.cursor()
        cur.execute("drop table if exists 'congestion'")
        con.commit()
    except:
        raise
except:
    print("sql_ini error")
finally:
    con.close()
import model.sql_ini