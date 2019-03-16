import sqlite3,time
def createTable():
    conn = sqlite3.connect('sensor.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE SENSOR
            (TIMESTAMP TIME  PRIMARY KEY     NOT NULL,
            DEVICE_ID           INT    NOT NULL,
            VALUE            INT,
            TYPE INT);''')
    print("Table created successfully")
    conn.close()

def updateData(time,device_id,value,typeD):
    conn = sqlite3.connect('sensor.db')
    print("Opened database successfully")
    conn.execute('''INSERT INTO SENSOR
            VALUES(?,?,?,?)''',(time,device_id,value,typeD))
    print("Table created successfully")
    conn.close()
