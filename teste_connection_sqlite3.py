# coding: utf-8

import sqlite3

path = r"C:\Desenvolvimento\SQLiteDB"

conn = sqlite3.connect(path + r"\teste.db")

print(conn.__str__())

conn.close()