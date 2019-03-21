# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import mysql.connector


cnx = mysql.connector.connect(user='gabriel', password='caballeria',
                              host='35.243.253.193',
                              database='dados')

bmf = open('/home/caball/Documents/bovespa/COTAHIST_A2019.TXT','r')

data_cotacao = []

for l in bmf:

    TIPREG = l[0:1]
    DATAPREG = l[2:9]
    NOMRES = l[27:38]
    MODREF = l[52:55]
    PREABE = l[56:68]
    PREMAX = l[69:81]
    PREMIN = l[82:94]
    PREMD = l[95:107]
    PREULT = l[108:120]
    PREOFC = l[121:133]
    PREOFV = l[134:146]
    CODISI = l[230:241]
    
    data_cotacao.append((
    TIPREG ,
    DATAPREG ,
    NOMRES ,
    MODREF ,
    PREABE ,
    PREMAX ,
    PREMIN ,
    PREMD ,
    PREULT ,
    PREOFC ,
    PREOFV ,
    CODISI)
    )
    

cursor = cnx.cursor(prepared=True)

    
add_cotacao = ("INSERT INTO cotacaob3  \
               (TIPREG, DATAPREG, NOMERES, MODREF, PREABE, PREMAX, PREMIN, PREMD, PREULT, PREOFC, PREOFV, CODISI)  \
               VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )")


result  = cursor.executemany(add_cotacao, data_cotacao)

cnx.commit()
print ("{} Record inserted successfully into python_users table".format(cursor.rowcount))


cursor.close()
cnx.close()
print("MySQL connection is closed")
