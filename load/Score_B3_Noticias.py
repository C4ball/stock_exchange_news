# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:07:03 2019

@author: biel_
"""

import pandas
import os
import numpy as np

from sklearn.model_selection import LeaveOneOut
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit
from sklearn.neural_network import MLPClassifier 


def SVM_TimeSplit(X,y,n_splits):
  tscv = TimeSeriesSplit(n_splits=n_splits)
  print(tscv)
  i=0
  acc = []
  yhat = y.copy()
  for train_index, test_index in tscv.split(X):
    #print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    #print(X_train, X_test, y_train, y_test)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    #Standard parameters
    clf = svm.SVC(kernel='rbf', gamma = 0.051, C = 1)
    clf.fit(X_train,y_train.ravel())
    X_test = scaler.transform(X_test)
    yhat[test_index] = clf.predict(X_test)
    acc.append(metrics.accuracy_score(yhat[test_index], y_test))
    i=i+1
  #print ('Score medio: '+ str(np.mean(acc)))
    return yhat, clf
  


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:/BuscaInfomoney-85bb0aa05d22.json"


sql = "SELECT * FROM dados_b3.historico_b3_N2 where D0_DATAPREG >= '2019-01-01' order by D0_DATAPREG"

empresas_sql = "SELECT * FROM dados_b3.DE_PARA_EMPRESAS"




# Run a Standard SQL query with the project set explicitly
project_id = 'buscainfomoney'
df = pandas.read_gbq(sql, project_id=project_id, dialect='standard')

empresas = pandas.read_gbq(empresas_sql, project_id=project_id, dialect='standard')


df_2 = df.replace(np.nan,0)


df_2 = df_2.drop('VARI_D0',axis=1)
df_2['VARI_D0'] = (df_2['PREABE_D0'] - df_2['PREULT_D0'])/df_2['PREABE_D0'] 

df_2.loc[df_2.VARI_D0 <= 0.01, 'FLAG_VAR_D0'] = 0
df_2.loc[df_2.VARI_D0 > 0.01, 'FLAG_VAR_D0'] = 1


    
real =  df_2[(df_2['D0_DATAPREG'] >= '2019-05-01')]

df_hist = df_2[(df_2['D0_DATAPREG'] < '2019-05-01')]

dias = real.D0_DATAPREG.unique()


for dia in dias:
    
    df_dia = df_2[(df_2['D0_DATAPREG'] < dia)]
    real_2 = real[(real['D0_DATAPREG'] == dia)]

    
    for index, row in empresas.iterrows():
        df_3 = df_dia[df_dia['CODNEG']==row[0]]
        try:
            real_3 = real_2[real_2['CODNEG']==row[0]]
            y_real = real_3['FLAG_VAR_D0']
        
            y_real = y_real.values
        except:
            print(str(row[0]))
        print('EMPRESA: {} - {}'.format(row[0],row[1]))
        
        y = df_3['FLAG_VAR_D0']

        print ("Flags positivos: ", sum(y))
        print ("Flags negativos: ", y.shape[0] - sum(y))
        
        to_drop = ['CODNEG','NOMRES','EMPRESA','week','MONTH','YEAR',
               'day_1','day_2','day_3','day_4','day_5',
               'week_2_w','week_2_y','week_3_w','week_3_y','week_4_w','week_4_y',
               'month_2_w','month_2_y','month_3_w','month_3_y','month_4_w','month_4_y',
               'PREABE_D0','PREULT_D0','QUATOT_D0','VARI_D0','FLAG_VAR_D0']
        df_3 = df_3.drop(to_drop,axis=1)
        real_3 = real_3.drop(to_drop,axis=1)
        
        df_3.sort_values(by=['D0_DATAPREG'])
        df_3 = df_3.set_index('D0_DATAPREG')
          
        real_3.sort_values(by=['D0_DATAPREG'])
        real_3 = real_3.set_index('D0_DATAPREG')
        
        features = df_3.columns
        n_splits = int((df_3.__len__() * 0.7))
          
        X = df_3.values
        y = y.values
          
      
    
     
        try:
            df_3['yhat'], clf = SVM_TimeSplit(X,y,n_splits)
     
        
        except:
            n_splits = int((df_3.__len__() * 0.6))
            df_3['yhat'], clf = SVM_TimeSplit(X,y,n_splits)
        
        
       
        try:
            real_3['yhat'] = clf.predict(real_3)
            real_3['FLAG_VAR_D0'] = y_real
        except:
            print(str(row[0]))
        
        real_3['CODNEG'] =  row[0]
        try: 
            
            real_pred = pandas.concat([real_pred,real_3],sort=True)
        except:
            real_pred = real_3


#real_pred = real_pred.iloc[0:0]


to_drop_2 = ['NOMRES','EMPRESA','week','MONTH','YEAR',
       'day_1','day_2','day_3','day_4','day_5',
       'week_2_w','week_2_y','week_3_w','week_3_y','week_4_w','week_4_y',
       'month_2_w','month_2_y','month_3_w','month_3_y','month_4_w','month_4_y',
       'PREABE_D0','PREULT_D0','QUATOT_D0','VARI_D0']        
        
df_hist_2 = df_hist.drop(to_drop_2,axis=1)
df_hist_2.sort_values(by=['D0_DATAPREG'])
df_hist_2 = df_hist_2.set_index('D0_DATAPREG')


df_total = pandas.concat([df_hist_2,real_pred],sort=True)

df_total.to_csv('C:/Users/biel_/Documents/GitHub/tccbi17/load/BASE_PREDITA.csv')


#Proximos Passo
#Incluir VARI_D0
#Loop para diversos Algoritmos






