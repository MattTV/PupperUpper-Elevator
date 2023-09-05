import time
import sqlite3

conn = None
c = None

def _OpenDB():
    
    conn = sqlite3.connect('pupperupper.db')
    c = conn.cursor()

def _SaveAndCloseDB():

    conn.commit()
    conn.close()

def _CloseNoSave():

    conn.close()

def _SaveNoClose():

    conn.commit()

def AddWeight(weight):

    _OpenDB()

    c.execute(f"INSERT INTO weights VALUES ({weight}, {time.time()})")

    _SaveAndCloseDB()

#Not sure if this works yet
def GetLatestBaseline():

    _OpenDB()

    c.execute("SELECT * FROM baselines")

    baseline = c.fetchone()[0]

    _CloseNoSave()

    return baseline

def GetTen():

    _OpenDB()

    c.execute("SELECT * FROM weights")

    weights = c.fetchmany(10)

    _CloseNoSave()

    return weights

def AddBaseline(baseline):

    _OpenDB()

    c.execute("DELETE FROM baselines")

    _SaveNoClose()

    c.execute(f"INSERT INTO baselines VALUES ({baseline}, {time.time()})")

    _SaveAndCloseDB()

def DumpAll():

    _OpenDB()

    c.execute("SELECT * FROM weights")

    print(c.fetchall())

    _CloseNoSave()

def ClearDB():

    _OpenDB()

    c.execute("DELETE FROM weights")

    _SaveAndCloseDB()