#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criado: 09/06/2019

@author: Rodrigo Dias
"""


import os
import pandas as pd
import numpy as np
import datetime
from pandas.tseries.offsets import BDay



# Importa JSON - Alta - e cria Dataframe - nome
df_list = []
for file in os.listdir("D://Desktop//load-bigquery//twitter//alta//nome//"):
    if file.endswith(".json"):
        twittes_alta = pd.read_json(os.path.join("D://Desktop//load-bigquery//twitter//alta//nome//", file))
        twittes_alta.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_alta)
        twittes_full_alta_nome=pd.concat(df_list)
        twittes_full_alta_nome['Empresa'] = twittes_full_alta_nome['Empresa'].str.replace("2018","")
        twittes_full_alta_nome['Empresa'] = twittes_full_alta_nome['Empresa'].str.replace("2019","")
        

# Importa JSON - Baixa - e cria Dataframe - nome
df_list = []
for file in os.listdir("D://Desktop//load-bigquery//twitter//baixa//nome//"):
    if file.endswith(".json"):
        twittes_baixa = pd.read_json(os.path.join("D://Desktop//load-bigquery//twitter//baixa//nome//", file))
        twittes_baixa.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_baixa)
        twittes_full_baixa_nome=pd.concat(df_list)
        twittes_full_baixa_nome['Empresa'] = twittes_full_baixa_nome['Empresa'].str.replace("2018","")
        twittes_full_baixa_nome['Empresa'] = twittes_full_baixa_nome['Empresa'].str.replace("2019","")

#################################################################################
        
# Importa JSON - Alta - e cria Dataframe - codigo
df_list = []
for file in os.listdir("D://Desktop//load-bigquery//twitter//alta//codigo//"):
    if file.endswith(".json"):
        twittes_alta = pd.read_json(os.path.join("D://Desktop//load-bigquery//twitter//alta//codigo//", file))
        twittes_alta.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_alta)
        twittes_full_alta_cod=pd.concat(df_list)
        twittes_full_alta_cod['Empresa'] = twittes_full_alta_cod['Empresa'].str.replace("2018","")
        twittes_full_alta_cod['Empresa'] = twittes_full_alta_cod['Empresa'].str.replace("2019","")
        

# Importa JSON - Baixa - e cria Dataframe - nome
df_list = []
for file in os.listdir("D://Desktop//load-bigquery//twitter//baixa//codigo//"):
    if file.endswith(".json"):
        twittes_baixa = pd.read_json(os.path.join("D://Desktop//load-bigquery//twitter//baixa//codigo//", file))
        twittes_baixa.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_baixa)
        twittes_full_baixa_cod=pd.concat(df_list)
        twittes_full_baixa_cod['Empresa'] = twittes_full_baixa_cod['Empresa'].str.replace("2018","")
        twittes_full_baixa_cod['Empresa'] = twittes_full_baixa_cod['Empresa'].str.replace("2019","")

#################################################################################


twittes_full_alta_cod.insert(11,"Weekday",twittes_full_alta_cod['timestamp'].dt.weekday)
twittes_full_alta_cod.insert(12,"Week",twittes_full_alta_cod['timestamp'].dt.week)
twittes_full_alta_cod.insert(13,"Month",twittes_full_alta_cod['timestamp'].dt.month)
twittes_full_alta_cod.insert(14,"Year",twittes_full_alta_cod['timestamp'].dt.year)

twittes_full_alta_nome.insert(11,"Weekday",twittes_full_alta_nome['timestamp'].dt.weekday)
twittes_full_alta_nome.insert(12,"Week",twittes_full_alta_nome['timestamp'].dt.week)
twittes_full_alta_nome.insert(13,"Month",twittes_full_alta_nome['timestamp'].dt.month)
twittes_full_alta_nome.insert(14,"Year",twittes_full_alta_nome['timestamp'].dt.year)

twittes_full_baixa_cod.insert(11,"Weekday",twittes_full_baixa_cod['timestamp'].dt.weekday)
twittes_full_baixa_cod.insert(12,"Week",twittes_full_baixa_cod['timestamp'].dt.week)
twittes_full_baixa_cod.insert(13,"Month",twittes_full_baixa_cod['timestamp'].dt.month)
twittes_full_baixa_cod.insert(14,"Year",twittes_full_baixa_cod['timestamp'].dt.year)

twittes_full_baixa_nome.insert(11,"Weekday",twittes_full_baixa_nome['timestamp'].dt.weekday)
twittes_full_baixa_nome.insert(12,"Week",twittes_full_baixa_nome['timestamp'].dt.week)
twittes_full_baixa_nome.insert(13,"Month",twittes_full_baixa_nome['timestamp'].dt.month)
twittes_full_baixa_nome.insert(14,"Year",twittes_full_baixa_nome['timestamp'].dt.year)

#################################################################################


# Imports the Google Cloud client library
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D://Desktop//load-bigquery//BuscaInfomoney-81e7f58e6908.json"

# Instantiates a client
bigquery_client = bigquery.Client()

# The name for the new dataset
dataset_id = 'dados_b3'
table = 'twittes_full_alta_cod'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)

####


##PROCESSO DE CARGA DE TWITTES 
#print("Limpando tabela de Carga.")
#query = ('DELETE from dados_b3.twittes_full_alta_cod where URL <> ""')
#query_job = bigquery_client.query(query)
#query = ('DELETE from dados_b3.twittes_full_alta_nome where URL <> ""')
#query_job = bigquery_client.query(query)
#query = ('DELETE from dados_b3.twittes_full_baixa_cod where URL <> ""')
#query_job = bigquery_client.query(query)
#query = ('DELETE from dados_b3.twittes_full_baixa_nome where URL <> ""')
#query_job = bigquery_client.query(query)
#
#
#print("Tabelas Limpas.")

# INICIO DO PROCESSO DE CARGA DE TWITTES

job_config = bigquery.LoadJobConfig()
job_config.autodetect = True
job_config.source_format = bigquery.SourceFormat.CSV


load_job = bigquery_client.load_table_from_dataframe(
    twittes_full_alta_cod, dataset_ref.table(table), job_config=job_config
)  # API request

table = 'twittes_full_alta_nome'

load_job = bigquery_client.load_table_from_dataframe(
    twittes_full_alta_nome, dataset_ref.table(table), job_config=job_config
)  # API request



table = 'twittes_full_baixa_cod'

load_job = bigquery_client.load_table_from_dataframe(
    twittes_full_baixa_cod, dataset_ref.table(table), job_config=job_config
)  # API request

table = 'twittes_full_baixa_nome'

load_job = bigquery_client.load_table_from_dataframe(
    twittes_full_baixa_nome, dataset_ref.table(table), job_config=job_config
)  # API request



