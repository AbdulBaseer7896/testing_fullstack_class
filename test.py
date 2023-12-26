import mysql.connector
from sqlalchemy import create_engine, text
import os
import random
from datetime import datetime

class test():
    engine = None

    def __init__(self):
        try:
            
            db_connection ="mysql+pymysql://ev2cic0aqzm7kxdea2eq:pscale_pw_2vgKRe3CXTQH9RXSPGDszsAsJWK4gu0wZMtHWGRFup5@aws.connect.psdb.cloud/test_db?charset=utf8mb4"
            self.engine = create_engine(db_connection, connect_args={
                "ssl": {
                    "ssl_ca": "/etc/ssl/cert.pem"
                }
            })
            print("connection build successfully admin")
        except:
            print("not work")



    def display(self):
        with self.engine.connect() as conn:

            query1 = text(f""" select * from user; """)
            data = conn.execute(query1).fetchall()
            print("this is = " , data)


            return True
        
obj = test()

obj.display()


