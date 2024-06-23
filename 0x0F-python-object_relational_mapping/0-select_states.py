#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.

Args:
    username: MySQL username
    password: MySQL password
    database: Database name
"""

import MySQLdb


def list_all_states(username, password, database):
    """Lists all states from the database hbtn_0e_0_usa.

    Args:
        username: MySQL username
        password: MySQL password
        database: Database name
    """

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = conn.cursor()

    cur.execute("SELECT states.id, states.name FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row[1]) 
    conn.close()
    cur.close()


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    database = input("Enter database name: ")

    list_all_states(username, password, database)

