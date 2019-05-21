# -*- coding: utf-8 -*-

import pandas as pd
import sqlalchemy  
import os

engine = sqlalchemy.create_engine("postgresql://postgres:123456@127.0.0.1/projetotcc")
con = engine.connect()

table_name = "dadostwitter"

# seta diretório raiz

for file in os.listdir("/twitter/coleta/twitter/alta/"):
    if file.endswith(".json"):
        twittes = pd.read_json(os.path.join("/twitter/coleta/twitter/alta/", file))
        twittes.to_sql(table_name, con,  if_exists='append')
        