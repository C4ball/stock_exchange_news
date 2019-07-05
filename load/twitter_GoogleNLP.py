#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criado: 09/06/2019

@author: Rodrigo Dias
"""


import os
import pandas as pd
import numpy as np
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Imports the Google Cloud client library
from google.cloud import bigquery


#FUNCAO PARA EXIBIR STATUS DA CARGA
def backline():        
    print('\r', end='')  


def analise_sentimento(base):
    
    count = 0
    total = base.__len__()
    
    #ANALISE DOS TEXTOS
    for index, row in base.iterrows():
        count+= 1
        
        text = str(row[7])
        
            
        #ANALISE DE SENTIMENTO DOS TITULOS
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)
        
        
        
        try:
            sentiment = client.analyze_sentiment(document=document).document_sentiment
            
            base.iloc[index,11] = sentiment.score
            base.iloc[index,12] = sentiment.magnitude
            
            s = str(count) + ' / ' + str(total)                       # string for output 
            print("{} : {} = {} ".format(s,text,sentiment.score))                        # just print and flush
            print('\r', end='')  
            
        except Exception as e:
            
            base.iloc[index,11] = 'erro'
            base.iloc[index,12] = 'erro'
            print("{} : {} = ERRO ".format(str(count),text))                        # just print and flush
            print('\r', end='')  
            print(e)
              
        #ANALISE DE SENTIMENTO DAS NOTICIAS
        
        #EXIBE STATUS
        
    return base


# Importa JSON - Alta - e cria Dataframe - nome
df_list = []
for file in os.listdir("twitter/alta/nome/"):
    if file.endswith(".json"):
        twittes_alta = pd.read_json(os.path.join("twitter/alta/nome/", file))
        twittes_alta.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_alta)
        twittes_full_alta_nome=pd.concat(df_list)
        twittes_full_alta_nome['Empresa'] = twittes_full_alta_nome['Empresa'].str.replace("2018","")
        twittes_full_alta_nome['Empresa'] = twittes_full_alta_nome['Empresa'].str.replace("2019","")
        

# Importa JSON - Baixa - e cria Dataframe - nome
df_list = []
for file in os.listdir("twitter/baixa/nome/"):
    if file.endswith(".json"):
        twittes_baixa = pd.read_json(os.path.join("twitter/baixa/nome/", file))
        twittes_baixa.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_baixa)
        twittes_full_baixa_nome=pd.concat(df_list)
        twittes_full_baixa_nome['Empresa'] = twittes_full_baixa_nome['Empresa'].str.replace("2018","")
        twittes_full_baixa_nome['Empresa'] = twittes_full_baixa_nome['Empresa'].str.replace("2019","")

#################################################################################
        
# Importa JSON - Alta - e cria Dataframe - codigo
df_list = []
for file in os.listdir("twitter/alta/codigo/"):
    if file.endswith(".json"):
        twittes_alta = pd.read_json(os.path.join("twitter/alta/codigo/", file))
        twittes_alta.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_alta)
        twittes_full_alta_cod=pd.concat(df_list)
        twittes_full_alta_cod['Empresa'] = twittes_full_alta_cod['Empresa'].str.replace("2018","")
        twittes_full_alta_cod['Empresa'] = twittes_full_alta_cod['Empresa'].str.replace("2019","")
        

# Importa JSON - Baixa - e cria Dataframe - nome
df_list = []
for file in os.listdir("twitter/baixa/codigo/"):
    if file.endswith(".json"):
        twittes_baixa = pd.read_json(os.path.join("twitter/baixa/codigo/", file))
        twittes_baixa.insert(0,"Empresa",os.path.splitext(file)[0])
#        df = pd.DataFrame(twittes)
        df_list.append(twittes_baixa)
        twittes_full_baixa_cod=pd.concat(df_list)
        twittes_full_baixa_cod['Empresa'] = twittes_full_baixa_cod['Empresa'].str.replace("2018","")
        twittes_full_baixa_cod['Empresa'] = twittes_full_baixa_cod['Empresa'].str.replace("2019","")

#################################################################################



#################################################################################



twittes_full_alta_cod['TEXT_SENTIMENT'] = ''
twittes_full_alta_cod['TEXT_MAGNITUDE'] = ''

twittes_full_alta_nome['TEXT_SENTIMENT'] = ''
twittes_full_alta_nome['TEXT_MAGNITUDE'] = ''

twittes_full_baixa_cod['TEXT_SENTIMENT'] = ''
twittes_full_baixa_cod['TEXT_MAGNITUDE'] = ''

twittes_full_baixa_nome['TEXT_SENTIMENT'] = ''
twittes_full_baixa_nome['TEXT_MAGNITUDE'] = ''



twittes_full_alta_cod_2 = twittes_full_alta_cod.query('timestamp >= 20181001')

twittes_full_alta_nome_2 = twittes_full_alta_nome.query('timestamp >= 20181001')
twittes_full_baixa_cod_2 = twittes_full_baixa_cod.query('timestamp >= 20181001')
twittes_full_baixa_nome_2 = twittes_full_baixa_nome.query('timestamp >= 20181001')






os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="teste-ee4b54698e33.json"
# Instantiates a client
client = language.LanguageServiceClient()

twittes_full_alta_cod = analise_sentimento(twittes_full_alta_cod_2)

twittes_full_alta_nome = analise_sentimento(twittes_full_alta_nome_2)



os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="teste-ee4b54698e33.json"
# Instantiates a client
client = language.LanguageServiceClient()

twittes_full_baixa_cod = analise_sentimento(twittes_full_baixa_cod_2)

twittes_full_baixa_nome = analise_sentimento(twittes_full_baixa_nome_2)


to_drop = ['Weekday','Week','Month','Year']
twittes_full_alta_nome = twittes_full_alta_nome.drop(to_drop,axis=1)


twittes_full_alta_cod_2.insert(13,"Month",twittes_full_alta_cod['timestamp'].dt.month)
twittes_full_alta_cod_2.insert(14,"Year",twittes_full_alta_cod['timestamp'].dt.year)
twittes_full_alta_cod_2.insert(15,"Weekday",twittes_full_alta_cod['timestamp'].dt.weekday)
twittes_full_alta_cod_2.insert(16,"Week",twittes_full_alta_cod['timestamp'].dt.week)


twittes_full_alta_nome_2.insert(13,"Month",twittes_full_alta_nome['timestamp'].dt.month)
twittes_full_alta_nome_2.insert(14,"Year",twittes_full_alta_nome['timestamp'].dt.year)
twittes_full_alta_nome_2.insert(15,"Weekday",twittes_full_alta_nome['timestamp'].dt.weekday)
twittes_full_alta_nome_2.insert(16,"Week",twittes_full_alta_nome['timestamp'].dt.week)


twittes_full_baixa_cod_2.insert(15,"Weekday",twittes_full_baixa_cod['timestamp'].dt.weekday)
twittes_full_baixa_cod_2.insert(16,"Week",twittes_full_baixa_cod['timestamp'].dt.week)
twittes_full_baixa_cod_2.insert(13,"Month",twittes_full_baixa_cod['timestamp'].dt.month)
twittes_full_baixa_cod_2.insert(14,"Year",twittes_full_baixa_cod['timestamp'].dt.year)

twittes_full_baixa_nome_2.insert(15,"Weekday",twittes_full_baixa_nome['timestamp'].dt.weekday)
twittes_full_baixa_nome_2.insert(16,"Week",twittes_full_baixa_nome['timestamp'].dt.week)
twittes_full_baixa_nome_2.insert(13,"Month",twittes_full_baixa_nome['timestamp'].dt.month)
twittes_full_baixa_nome_2.insert(14,"Year",twittes_full_baixa_nome['timestamp'].dt.year)

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
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="BuscaInfomoney-1290108871c4.json"



# Instantiates a client
bigquery_client = bigquery.Client()

# The name for the new dataset
dataset_id = 'dados_b3'
table = 'twittes_full_alta_cod'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)




job_config = bigquery.LoadJobConfig()
job_config.autodetect = True
job_config.source_format = bigquery.SourceFormat.CSV

twittes_full_alta_nome.info()
twittes_full_alta_cod.info()

twittes_full_alta_cod['TEXT_SENTIMENT'] = twittes_full_alta_cod['TEXT_SENTIMENT'].replace( np.nan, 'erro', regex=True)
twittes_full_alta_cod['TEXT_MAGNITUDE'] = twittes_full_alta_cod['TEXT_MAGNITUDE'].replace( np.nan, 'erro', regex=True)


twittes_full_alta_nome['TEXT_SENTIMENT'] = twittes_full_alta_cod['TEXT_SENTIMENT'].replace( np.nan, 'erro', regex=True)
twittes_full_alta_nome['TEXT_MAGNITUDE'] = twittes_full_alta_cod['TEXT_MAGNITUDE'].replace( np.nan, 'erro', regex=True)

twittes_full_alta_nome.to_csv('analise_twitter_nome.csv')



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



