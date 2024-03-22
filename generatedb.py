import time
import sqlite3

def main():

    conn = sqlite3.connect('pupperupper.db')

    c = conn.cursor()

#     c.execute("""CREATE TABLE weights (
#             weight REAL,
#             datetime INTEGER
#             )""")
    
#     c.execute("""CREATE TABLE baselines (
#             baseline REAL,
#             datetime INTEGER
#             )""")

    weight = 15.4

    c.execute(f"INSERT INTO weights VALUES ({weight}, {time.time()})")

    c.execute("SELECT * FROM weights")

    c.execute(f"INSERT INTO baselines VALUES (25, {time.time()})")

    c.execute("SELECT * FROM baselines")

    print(c.fetchall())

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()