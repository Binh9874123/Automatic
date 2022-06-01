

import sqlite3 as lite
import sys
import os
import re

def atributes(name_file):
    list_pole = []
    with open(name_file,encoding='utf-8', mode='r') as file:
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
    return list_pole
def read_file(name_file):
    file_string = ''
    with open(name_file,encoding='utf-8', mode='r') as file1:
        file_string = file1.read()

    pattern = "INSERT"
    x = file_string.split(pattern)
    list_sql_filter = list(filter(lambda str : "Operators"  in str,x))
    list_sql_result = list(map(lambda str: pattern + " " + str, list_sql_filter)) 

    return list_sql_result
name_file1 = 'prostak-db.ru_RU.UTF-8.sqlt3.in'
name_file2 = 'convert.sqlt3.in'
list_atribute = []
list_result_sql = []
# con co gia tri trung nhau
list_atribute = atributes(name_file1) + atributes(name_file2)
set_atribute = set(list_atribute)
list_result_sql = read_file(name_file1) + read_file(name_file2)
# print(list_result_sql)
# list_pole = []
# with open('prostak-db.ru_RU.UTF-8.sqlt3.in',encoding='utf-8', mode='r') as file:
#         all_file = file.readlines()
#         for line in all_file:
#             s1 = "Operators ("
#             s2 = ") VALUES"
            
#             if('INSERT OR REPLACE INTO Operators' in line):
#                 first = line.index(s1) + len(s1)
#                 last =  line.index(s2) 
#                 list_p = line[first:last].split(", ")
#                 # print(list_p)
#                 p =  list(map(lambda pole : list_pole.append(pole),list_p))
        
# poles = set(list_pole)   
# file_string = ''
# with open('prostak-db.ru_RU.UTF-8.sqlt3.in',encoding='utf-8', mode='r') as file1:
#     file_string = file1.read()

# pattern = "INSERT OR REPLACE INTO Operators"
# x = file_string.split(pattern)
# list_sql = list(filter(lambda str : "INSERT OR" not in str,x))



# list_pole = []
# with open('convert.sqlt3.in',encoding='utf-8', mode='r') as file:
#         all_file = file.readlines()
#         for line in all_file:
#             s1 = "Operators ("
#             s2 = ") VALUES"
            
#             if('INSERT OR REPLACE INTO Operators' in line or 'INSERT INTO Operators' in line ):
#                 first = line.index(s1) + len(s1)
#                 last =  line.index(s2) 
#                 list_p = line[first:last].split(", ")
#                 # print(list_p)
#                 p =  list(map(lambda pole : list_pole.append(pole),list_p))
        
# poles = set(list_pole)   
# file_string = ''
# with open('convert.sqlt3.in',encoding='utf-8', mode='r') as file1:
#     file_string = file1.read()


# def read_file(name_file):
#     file_string = ''
#     with open(name_file,encoding='utf-8', mode='r') as file1:
#         file_string = file1.read()

#     pattern = "INSERT"
#     x = file_string.split(pattern)
#     list_sql_filter = list(filter(lambda str : "Operators" not in str,x))
#     list_sql_result = map(lambda str: pattern + " " + str, list_sql_filter) 

#     return list_sql_result





path = os.path.dirname(__file__) + "mySql.db"
con = lite.connect(path)

#con = lite.connect("prostak-db.ru_RU.UTF-8.sqlt3.in")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Operators")    
    cur.execute('CREATE TABLE Operators ('+', '.join(set_atribute)+')')
    for sql in list_result_sql:
        cur.execute(sql)
        cur.execute("SELECT name, message, outputs FROM Operators")
        rows = cur.fetchall()
    # for row in rows:
    #     print (row)

for row in rows:
        if 'imcanny' in row:
            print(row[1]+ " \n"+ row[2])

def get_ouput(name):
    for row in rows:
        if name in row:
            return row[2]

def get_message(name):
    for row in rows:
        if name in row:
            return row[1]
