#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 02:48:02 2019

@author: caball
"""

# Imports the Google Cloud client library
from google.cloud import bigquery
import os
import pandas as pd
import pandas_gbq
import numpy as np
import datetime
from pandas.tseries.offsets import BDay


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/caball/Downloads/BuscaInfomoney-f2a64ca737d4.json"

# Instantiates a client
bigquery_client = bigquery.Client()

# The name for the new dataset
dataset_id = 'dados_b3'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)

# Creates the new dataset
#dataset = bigquery_client.create_dataset(dataset)
#print('Dataset {} created.'.format(dataset.dataset_id))


colunas = ['TIPREG',
        'DATAPREG',
        'CODNEG', 
        'NOMRES', 
        'MODREF', 
        'PREABE', 
        'PREMAX', 
        'PREMIN', 
        'PREMD ',
        'PREULT', 
        'PREOFC', 
        'PREOFV', 
        'CODISI', 
        'QUATOT' ]

col_num = ['PREABE', 
        'PREMAX', 
        'PREMIN', 
        'PREMD ',
        'PREULT', 
        'PREOFC', 
        'PREOFV']

col_int = ['TIPREG',
           'QUATOT' ]

col_str = ['CODNEG', 
        'NOMRES', 
        'MODREF', 
        'CODISI' ]


df = pd.read_csv('bmf_load.csv', delimiter=',',names = colunas, parse_dates=['DATAPREG'])



for col in col_num:
    df[col] = pd.to_numeric(df[col], downcast='float')
    
for col in col_int:
    df[col] = pd.to_numeric(df[col], downcast='integer')
    

for col in col_str:
    df[col] = df[col].str.strip()

#The day of the week with Monday=0, Sunday=6
df['weekday'] = df['DATAPREG'].dt.weekday

df['week'] = df['DATAPREG'].dt.week
df['month'] = df['DATAPREG'].dt.month
df['year'] = df['DATAPREG'].dt.year


#DIAS ANTERIORES
df['day_1'] = df['DATAPREG'] - BDay(1)
df['day_2'] = df['DATAPREG'] - BDay(2)
df['day_3'] = df['DATAPREG'] - BDay(3)
df['day_4'] = df['DATAPREG'] - BDay(4)
df['day_5'] = df['DATAPREG'] - BDay(5)

#SEMANAS ANTERIORES
df['week_2_w'] = (df['DATAPREG']+datetime.timedelta(weeks=-2)).dt.week
df['week_2_y'] = (df['DATAPREG']+datetime.timedelta(weeks=-2)).dt.year
df['week_3_w'] = (df['DATAPREG']+datetime.timedelta(weeks=-3)).dt.week
df['week_3_y'] = (df['DATAPREG']+datetime.timedelta(weeks=-3)).dt.year
df['week_4_w'] = (df['DATAPREG']+datetime.timedelta(weeks=-4)).dt.week
df['week_4_y'] = (df['DATAPREG']+datetime.timedelta(weeks=-4)).dt.year


#MESES ANTERIORES
df['month_2_w'] = (df['DATAPREG'] + np.timedelta64(-2, 'M')).dt.month
df['month_2_y'] = (df['DATAPREG'] + np.timedelta64(-2, 'M')).dt.year
df['month_3_w'] = (df['DATAPREG'] + np.timedelta64(-3, 'M')).dt.month
df['month_3_y'] = (df['DATAPREG'] + np.timedelta64(-3, 'M')).dt.year
df['month_4_w'] = (df['DATAPREG'] + np.timedelta64(-4, 'M')).dt.month
df['month_4_y'] = (df['DATAPREG'] + np.timedelta64(-4, 'M')).dt.year


df = df.rename(columns={"PREMD ": "PREMD_"})
df = df.rename(columns={"PREMD": "PREMD_"})

tail = df.tail(20)
head = df.head(20)



try:
    pandas_gbq.to_gbq(
        df, 'dados_b3.dadosb3_datas', project_id='buscainfomoney', if_exists='replace',
    )
    print('Base carregada com sucesso!')
except Exception as e:
    print('Erro ao carregadar os dados: {}'.format(e))
    
query =  open("INSERT_historico_b3_N.SQL", "r")    
query = query.read()
 
query_job = bigquery_client.query(query)

try:
    query_job.result()
    print("Dados carregados na tabela Historico.")
except Exception as e:
    print('Erro ao carregadar os dados HistoricoS: {}'.format(e))