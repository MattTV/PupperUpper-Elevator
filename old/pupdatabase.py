import time
import sqlite3

def AddWeight(weight):
    conn = sqlite3.connect('pupperweights.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO pupper VALUES ({weight}, {time.time()})")
    conn.commit()
    conn.close()

def GetBaseline():
    conn = sqlite3.connect('pupperweights.db')
    c = conn.cursor()
    c.execute("SELECT * FROM baseline")
    baseline = c.fetchone()[0]
    conn.close()
    return baseline

def GetTen():
    conn = sqlite3.connect('pupperweights.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pupper")
    weights = c.fetchmany(10)
    conn.close()
    return weights

def SetBaseline(baseline):
    conn = sqlite3.connect('pupperweights.db')
    c = conn.cursor()
    c.execute("DELETE FROM baseline")
    conn.commit()
    c.execute(f"INSERT INTO baseline VALUES ({baseline})")
    conn.commit()
    conn.close()

def DumpAll():
    conn = sqlite3.connect('pupperweights.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pupper")
    print(c.fetchall())
    conn.close()

def ClearDB():
    conn = sqlite3.connect('pupperweights.db')
    c = conn.cursor()
    c.execute("DELETE FROM pupper")
    conn.commit()
    conn.close()