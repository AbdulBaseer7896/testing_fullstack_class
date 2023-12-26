

import mysql.connector
from sqlalchemy import create_engine, text
import os
import random
from datetime import datetime

class testing():
    engine = None

    def init(self):
        try:
            
            db_connection = "mysql+pymysql://ev2cic0aqzm7kxdea2eq:pscale_pw_2vgKRe3CXTQH9RXSPGDszsAsJWK4gu0wZMtHWGRFup5@aws.connect.psdb.cloud/online_database?charset=utf8mb4"
            self.engine = create_engine(db_connection, connect_args={
                "ssl": {
                    "ssl_ca": "/etc/ssl/cert.pem"
                }
            })
            print("connection build successfully admin")
        except Exception as e:
            print(f"An error occurred: {e}")



    def display(self):
        with self.engine.connect() as conn:
            
            query2 = text(f""" Select * from JOBS; """)
            conn.execute(query2)
            return True


obj = testing()

obj.display()