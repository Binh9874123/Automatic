
import sqlite3 as lite
import sys
import os
import re

list_pole = []
with open('prostak-db.ru_RU.UTF-8.sqlt3.in',encoding='utf-8', mode='r') as file:
        all_file = file.readlines()
        for line in all_file:
            s1 = "Operators ("
            s2 = ") VALUES"
            
            if('INSERT OR REPLACE INTO Operators' in line):
                first = line.index(s1) + len(s1)
                last =  line.index(s2) 
                list_p = line[first:last].split(", ")
                # print(list_p)
                p =  list(map(lambda pole : list_pole.append(pole),list_p))
        
poles = set(list_pole)   
file_string = ''
with open('prostak-db.ru_RU.UTF-8.sqlt3.in',encoding='utf-8', mode='r') as file1:
    file_string = file1.read()

pattern = "INSERT OR REPLACE INTO Operators"
x = file_string.split(pattern)
list_sql = list(filter(lambda str : "INSERT OR" not in str,x))



path = os.path.dirname(__file__) + "mySql.db"
con = lite.connect(path)

#con = lite.connect("prostak-db.ru_RU.UTF-8.sqlt3.in")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Operators")    
    cur.execute('CREATE TABLE Operators ('+', '.join(poles)+')')
    for sql in list_sql:
        cur.execute('INSERT OR REPLACE INTO Operators' + sql)
        cur.execute("SELECT name, message, outputs FROM Operators")
        rows = cur.fetchall()
    for row in rows:
        print (row)


def get_ouput(name):
    for row in rows:
        if name in row:
            return row[2]

def get_message(name):
    for row in rows:
        if name in row:
            return row[1]
