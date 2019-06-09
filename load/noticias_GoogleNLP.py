#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Tue May 21 19:27:01 2019

#@author: caball
#"""

# Imports the Google Cloud client library
from google.cloud import bigquery
import os
import psycopg2
import pandas 

import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/caball/Documents/BuscaInfomoney-81e7f58e6908.json"

#conn = psycopg2.connect("host=35.211.196.189 dbname=projetotcc user=postgres password=123456")
conn = psycopg2.connect("host=localhost dbname=tcc user=postgres password=123456")

# Instantiates a client
client = language.LanguageServiceClient()

# Instantiates a client
bigquery_client = bigquery.Client()

# The name for the new dataset
dataset_id = 'dados_b3'
table = 'noticias'
table_historico = 'historico_noticias'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)

# Creates the new dataset
#dataset = bigquery_client.create_dataset(dataset)
#print('Dataset {} created.'.format(dataset.dataset_id))

#FUNCAO PARA EXIBIR STATUS DA CARGA
def backline():        
    print('\r', end='')  


#LEITURA DOS DADOS
pd = pandas.read_csv('dados_empresas.csv', header=None, delimiter='|',encoding = 'utf8')      

pd['TITLE_SENTIMENT'] = ''
pd['TITLE_MAGNITUDE'] = ''
pd['TEXT_SENTIMENT'] = ''
pd['TEXT_MAGNITUDE'] = ''

#PRIMEIRO TRATAMENTO DA DATA
pd.iloc[:,2] = pd.iloc[:,2].str.slice(2,14)

count = 0
total = pd.__len__()

#ANALISE DOS TEXTOS
for index, row in pd.iterrows():
    count+= 1
    
 #   if count%550 == 0 and count != 0:
 #       print('\n\nAguardando limite da API, pausa de 65 segundos.\n\n')
#        time.sleep(65)
        
     # The text to analyze
    title = str(row[3])
    text = str(row[4])
    
    #TRATAMENTO DAS DATAS
    pd.iloc[index,2] = datetime.strptime(pd.iloc[index,2],
                        "%d %b, %Y")

    #ANALISE DE SENTIMENTO DOS TITULOS
    document = types.Document(
        content=title,
        type=enums.Document.Type.PLAIN_TEXT)
    
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    
    pd.iloc[index,5] = sentiment.score
    pd.iloc[index,6] = sentiment.magnitude

    #ANALISE DE SENTIMENTO DAS NOTICIAS
    document_2 = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    
    sentiment_2 = client.analyze_sentiment(document=document_2).document_sentiment
    
    pd.iloc[index,7] = sentiment_2.score
    pd.iloc[index,8] = sentiment_2.magnitude
    
    
    #EXIBE STATUS
    s = str(count) + ' / ' + str(total)                        # string for output
    print(s, end='')                        # just print and flush
    backline()  

#CRIACAO DE CHAVES DE DATAS
pd['weekday'] = pd[2].dt.weekday
pd['week'] = pd[2].dt.week
pd['month'] = pd[2].dt.month
pd['year'] = pd[2].dt.year

#NOMEACAO DE COLUNAS
pd.columns = ['URL',
            'EMPRESA', 
            'DATA', 
            'TITULO', 
            'NOTICIA',
            'TITLE_SENTIMENT',
            'TITLE_MAGNITUDE',
            'TEXT_SENTIMENT',
            'TEXT_MAGNITUDE',
            'WEEKDAY',
            'WEEK',
            'MONTH',
            'YEAR']

#PROCESSO DE CARGA DE NOTICIAS ANALIZADAS
print("Limpando tabela de Carga.")
query = ('DELETE from dados_b3.noticias where URL <> ""')
query_job = bigquery_client.query(query)


print("Tabela Limpa.")

job_config = bigquery.LoadJobConfig()
job_config.autodetect = True
job_config.source_format = bigquery.SourceFormat.CSV


load_job = bigquery_client.load_table_from_dataframe(
    pd, dataset_ref.table(table), job_config=job_config
)  # API request

print("Carregando Tabela {}".format(table))

load_job.result()  # Waits for table load to complete.
print("Carga finalizada.")

destination_table = bigquery_client.get_table(dataset_ref.table(table))
print("Carregadas {} Linhas.".format(destination_table.num_rows))


query_2 = ('insert into dados_b3.historico_noticias  \
select * from dados_b3.noticias \
where URL not in (select URL from dados_b3.historico_noticias ) ')
query_job_2 = bigquery_client.query(query_2)
print("Dados carregados na tabela Historico.")






