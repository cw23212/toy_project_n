from flask import abort
import sqlite3
import os
from config import config
import json
import base64
db_path=config['db_path']
a="{'person':22,'place':'hakgwan_food','complexity':'High','time':'2020-07-02-03-21'}"
b='{"person":22,"place":"hakgwan_food","complexity":"High","time":"2020-07-02-06-30"}'
def update(location,congestion,json_o):
    congestion=str(congestion)
    location=str(location)
    json_o=json.dumps(json_o)
    json_o=base64.encodestring(json_o.encode("utf-8")).decode()
    try:
        con = sqlite3.connect(db_path)
        try:
            cur=con.cursor()
            sql="select EXISTS( SELECT * FROM `congestion` where location='"+location+"' ) as exist "
            exi=cur.execute(sql).fetchone()[0]
            if exi==1:
                update_sql="update congestion set conge='"+congestion+"', json_o='"+json_o+"' where  location='"+location+"' "
                cur.execute(update_sql)
            else:
                sql="insert into congestion values('"+location+"','"+congestion+"','"+json_o+"')"
                cur.execute(sql)
            con.commit()
            return "OK"
        except:
            raise
    except:
        # abort(500)
        raise
    finally:
        con.close()
update("hakgwan_food",2,a)
