# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:50:23 2019

@author: rodri
"""

import pandas as pd
import sqlalchemy  
import os

engine = sqlalchemy.create_engine("postgresql://postgres:123456@127.0.0.1/projetotcc")
con = engine.connect()

table_name = "dadosnoticias"

noticias = pd.read_csv("/twitter/coleta/noticias/dados_empresas.csv", sep='|', index_col=False, names=["url","empresa","data","titulo","noticia"] )

noticias.to_sql(table_name, con,  if_exists='append')
