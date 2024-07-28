"""
Real Python Book 1 Chapter 14 - SQL Database Connections
"""

import sqlite3

def afunction():
    # Enter a function here
    with sqlite3.connect("test_database.db") as connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS Roster")
        c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
        character_values = (
            ("Jean-Baptiste Zorg", "Human", 122),
            ("Korben Dallas", "Meat Popsicle", 100),
            ("Ak'not", "Mangalore", -5)
        )
        c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", character_values)
        c.execute("UPDATE Roster SET Species='Human' WHERE Name='Korben Dallas'")
        c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
        for row in c.fetchall():
            print(row)


def main():
    # Enter main function here
    afunction()


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"Runtime: ---{round(time.time() - start_time, 2)}---")