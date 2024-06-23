#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa."""

import MySQLdb


def list_all_states(username, password, database):
    """Lists all states from the database hbtn_0e_0_usa.

    Args:
        username: MySQL username
        password: MySQL password
        database: Database name
    """

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cur = conn.cursor()
        
        cur.execute("SELECT states.id, states.name FROM states ORDER BY states.id ASC")
        rows = cur.fetchall()


        for row in rows:

    except MySQLdb.Error as err:
        print("Error: {}".format(err))

    finally:
        if conn:
            conn.close()
            cur.close()


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    database = input("Enter database name: ")

    list_all_states(username, password, database)

