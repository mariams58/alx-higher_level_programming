#!/usr/bin/python3
""" This python script lists all cities from the database hbtn_0e_4_usa
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
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON states.id=cities.state_id")
    # fetching and printing query result
    lines = cursor.fetchall()
    for line in lines:
        print(line)
    # close all open cursors
    cursor.close()
    # close the database
    conn.close()
