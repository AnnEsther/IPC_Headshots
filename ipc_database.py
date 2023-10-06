import requests
import psycopg2

def getIpcData():
    conn = psycopg2.connect(database = "postgres", 
                            user = "postgres", 
                            host= 'localhost',
                            password = "joyfulAnn",
                            port = 5432)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute('SELECT * FROM ipcdata;')

    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return rows