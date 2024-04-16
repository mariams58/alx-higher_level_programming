#!/usr/bin/python3
""" This python script lists all states that starts with 'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == " __main__":
    # creating a connection to the database with args from the cli
    d_b = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    # creating a cursor object
    cursor = d_b.cursor()
    # executing the query using the corspr object an execute function
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    # fetching and printing query result
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # close all open cursors
    cursor.close()
    # close the database
    d_b.close()
