import sqlite3

def main():

    conn = sqlite3.connect('pupperupper.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE weights (
            weight real,
            datetime blob
            )""")
    
    c.execute("""CREATE TABLE baselines (
            basline real,
            datetime blob
            )""")

    weight = 15.4

    #c.execute(f"INSERT INTO pupper VALUES ({weight}, 5)")

    #c.execute("SELECT * FROM pupper")

    #print(c.fetchone())

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()