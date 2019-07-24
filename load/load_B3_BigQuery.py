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

col_num = ['TIPREG',
        'PREABE', 
        'PREMAX', 
        'PREMIN', 
        'PREMD ',
        'PREULT', 
        'PREOFC', 
        'PREOFV', 
        'QUATOT' ]

col_str = ['CODNEG', 
        'NOMRES', 
        'MODREF', 
        'CODISI' ]


df = pd.read_csv('bmf_load.csv', delimiter=',',names = colunas, parse_dates=['DATAPREG'])



for col in col_num:
    df[col] = pd.to_numeric(df[col])

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


tail = df.tail(20)
head = df.head(20)


job_config = bigquery.LoadJobConfig()
job_config.autodetect = True



job_config.source_format = bigquery.SourceFormat.CSV


load_job = bigquery_client.load_table_from_dataframe(
    df, dataset_ref.table("dadosb3_datas"), job_config=job_config
)  # API request
print("Starting job {}".format(load_job.job_id))

load_job.result()  # Waits for table load to complete.
print("Job finished.")

destination_table = bigquery_client.get_table(dataset_ref.table("dadosb3_datas"))
print("Loaded {} rows.".format(destination_table.num_rows))