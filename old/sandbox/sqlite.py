import sqlite3

conn = sqlite3.connect('pupperweights.db')

c = conn.cursor()

#c.execute("""CREATE TABLE pupper (
#        weight real,
#        time blob
#        )""")

weight = 15.4

#c.execute(f"INSERT INTO pupper VALUES ({weight}, 5)")

#c.execute("SELECT * FROM pupper")

#print(c.fetchone())

#c.execute("""CREATE TABLE baseline (
#    baseline real
#    )""")

conn.commit()

conn.close()