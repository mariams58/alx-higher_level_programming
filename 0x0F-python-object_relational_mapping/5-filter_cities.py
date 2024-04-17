#!/usr/bin/python3
""" This python script lists all the states in the
cities table from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # creating a connection to the database with args from the cli
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    # creating a cursor object
    cursor = conn.cursor()
    # executing the query using the corspr object an execute function
    cursor.execute("""SELECT name FROM cities \
            WHERE state_id = (SELECT id FROM states \
            WHERE name = %s)""", (argv[4], ))
    # fetching and printing query result
    lines = cursor.fetchall()
    state_list = []
    for line in lines:
        state_list.append(line[0])
    print(*state_list, sep=", ")
    # close all open cursors
    cursor.close()
    # close the database
    conn.close()
