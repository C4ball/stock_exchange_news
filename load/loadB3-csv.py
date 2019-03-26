# -*- coding: utf-8 -*-


bmf = open('D:\pycharm\COTAHIST_A2019.TXT','r')
bmfload = open("bmf_load.csv",'w')

data_cotacao = []

for l in bmf:

    TIPREG = l[0:2]
    DATAPREG = l[2:10]
    CODNEG = l[12:24]
    NOMRES = l[27:39]
    MODREF = l[52:56]
    PREABE = ((l[56:67]) + '.' + (l[67:69]))
    PREMAX = ((l[69:80]) + '.' + (l[80:82]))
    PREMIN = ((l[82:93]) + '.' + (l[93:95]))
    PREMD = ((l[95:106]) + '.' + (l[106:108]))
    PREULT = ((l[108:119]) + '.' + (l[119:121]))
    PREOFC = ((l[121:132]) + '.' + (l[132:134]))
    PREOFV = ((l[134:145]) + '.' + (l[145:147]))
    CODISI = l[230:242]
    
    if TIPREG == "01":
    
        bmfload.write(TIPREG  + ',' + DATAPREG  + ',' + CODNEG  + ',' + NOMRES  + ',' + MODREF  + ',' + \
              PREABE + ',' + PREMAX + ',' + PREMIN  + ',' + PREMD  + ',' + PREULT  + ',' + PREOFC  + ',' + PREOFV  + ',' + CODISI + "\n")

    
bmfload.close()
