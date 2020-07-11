from flask import abort
import sqlite3
import os
from config import config
import json
import base64
db_path=config['db_path']
# db_path=os.path.join(os.getcwd(),"sqlite.db")
# class sql_model:
def select(location):
    try:
        con = sqlite3.connect(db_path)
        
        cur=con.cursor()
        sql="select EXISTS( SELECT * FROM `congestion` where location='"+location+"' ) as exist "
        exi=cur.execute(sql).fetchone()[0]
        if exi==1:
            sql="select * from 'congestion' where location='"+location+"'"
            res=cur.execute(sql).fetchall()
        else:
            res= "nonExistent" 
    except:
        print("sql_select_error")
    finally:
        con.commit()
        con.close()
    return res
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

def select(location):
    try:
        con = sqlite3.connect(db_path)
        
        cur=con.cursor()
        sql="select EXISTS( SELECT * FROM `congestion` where location='"+location+"' ) as exist "
        exi=cur.execute(sql).fetchone()[0]
        if exi==1:
            sql="select * from 'congestion' where location='"+location+"'"
            res=cur.execute(sql).fetchall()[0]
        else:
            res= "nonExistent" 
    except:
        print("sql_select_error")
    finally:
        con.commit()
        con.close()
    return res