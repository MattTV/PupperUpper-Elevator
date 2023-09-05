import time
import sqlite3

conn = null
c = null

def OpenDB():
    conn = sqlite3.connect('pupperupper.db')
    c = conn.cursor()

def SaveAndCloseDB():
    conn.commit()
    conn.close()

def AddWeight(weight):
    conn = sqlite3.connect('pupperupper.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO weights VALUES ({weight}, {time.time()})")
    conn.commit()
    conn.close()

#Not sure if this works yet
#def GetLatestBaseline():
#    conn = sqlite3.connect('pupperweights.db')
#    c = conn.cursor()
#    c.execute("SELECT * FROM baselines")
#    baseline = c.fetchone()[0]
#    conn.close()
#    return baseline

def GetTen():
    conn = sqlite3.connect('pupperupper.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weights")
    weights = c.fetchmany(10)
    conn.close()
    return weights

def AddBaseline(baseline):
    conn = sqlite3.connect('pupperupper.db')
    c = conn.cursor()
    c.execute("DELETE FROM baselines")
    conn.commit()
    c.execute(f"INSERT INTO baselines VALUES ({baseline}, {time.time()})")
    conn.commit()
    conn.close()

def DumpAll():
    conn = sqlite3.connect('pupperupper.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weights")
    print(c.fetchall())
    conn.close()

def ClearDB():
    conn = sqlite3.connect('pupperupper.db')
    c = conn.cursor()
    c.execute("DELETE FROM weights")
    conn.commit()
    conn.close()