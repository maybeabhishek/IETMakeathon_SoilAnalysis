import sqlite3,time, datetime,hashlib
import json
from sqlite3 import Error

def createConnection():
    conn = sqlite3.connect('sensor.db')
    print("Opened database successfully")
    return conn

def createTable(conn):
    

    conn.execute('''CREATE TABLE SENSOR
            (ID varchar PRIMARY KEY not null,
              TIMESTAMP TIME    NOT NULL,
            DEVICE_ID           INT    NOT NULL,
            VALUE            INT,
            TYPE INT);''')
    print("Table created successfully")

def updateData(conn,device_id,value,typeD):
    conn = sqlite3.connect('sensor.db')
    print("Opened database successfully")
    ts = time.time()
    ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    id = hashlib.sha256((str(ts)+ str(value)+str(typeD)).encode('ascii')).hexdigest()
    try:
        conn.execute('''INSERT INTO SENSOR
                VALUES(?,?,?,?,?)''',(id,ts,device_id,value,typeD))
        print("Table created successfully")
        conn.commit()
    except Error as e:
        print(e)
    

def showAll(conn):
    conn = sqlite3.connect('sensor.db')
    cur = conn.cursor()
    try:
        cur.execute('''SELECT * from SENSOR;''')
    except Error as e:
        print(e)
    rows = cur.fetchall()
    print("The length of rows is: ")
    print(len(rows))
    for row in rows:
        print(row)


def latestData(conn):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM SENSOR ORDER BY TIMESTAMP DESC LIMIT 1''')
    rows = cur.fetchall()
    return json.dumps({'rows': rows[1:]})

def getRowsByDeviceID(conn, deviceID):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM SENSOR where DEVICE_ID = ?''',(deviceID,))
    rows = cur.fetchall()
    row = {}
    data = []
    for i in rows:
        row['time'] = i[1]
        row['device_id'] = i[2]
        row['val'] = i[3]
        row['type'] = i[4]
        data.append(row)
    # print(data)
    return json.dumps({'rows': rows})

def getRowsByType(conn, deviceID, sensorType):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM SENSOR where DEVICE_ID = ? AND TYPE = ?''',(deviceID,sensorType,))
    rows = cur.fetchall()
    row = {}
    data = []
    for i in rows:
        row['time'] = i[1]
        row['device_id'] = i[2]
        row['val'] = i[3]
        row['type'] = i[4]
        data.append(row)
    # print(data)
    return json.dumps({'rows': rows})