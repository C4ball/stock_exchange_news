# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:07:03 2019

@author: biel_
"""

import pandas
import os
import numpy as np

#from sklearn.model_selection import LeaveOneOut
#from sklearn import tree
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.preprocessing import StandardScaler

from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import TimeSeriesSplit
from sklearn.neural_network import MLPClassifier 


algors = { 
         'SVC_RBF' : svm.SVC(kernel='rbf', gamma = 0.051, C = 1), 
         'SVR_RBF' : svm.SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1) ,
         #'SVR_LIN' : svm.SVR(kernel='linear', C=100, gamma='auto'), 
         #'SVR_POLY' : svm.SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,coef0=1), 
         'SVR_SCAL' : svm.SVR(gamma='scale', C=1.0, epsilon=0.2), 
         'Rede_Neural' : MLPClassifier(activation='tanh', alpha=1e-05, batch_size='auto',
                           beta_1=0.9, beta_2=0.999, early_stopping=True,
                           epsilon=1e-08, hidden_layer_sizes=(10,20), learning_rate='constant',
                           learning_rate_init=0.001, max_iter=2000000, momentum=0.9,
                           nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
                           solver='sgd', tol=0.0001, validation_fraction=0.3, verbose=False,
                           warm_start=False) 
         
        } 



def SVM_TimeSplit(X,y,n_splits,algoritmo,name):
  tscv = TimeSeriesSplit(n_splits=n_splits)
  print(name)
  print(tscv)
  i=0
  acc = []
  yhat = y.copy()
  for train_index, test_index in tscv.split(X):
    #print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    #print(X_train, X_test, y_train, y_test)
    #scaler = StandardScaler()
    #X_train = scaler.fit_transform(X_train)
    #Standard parameters
    clf = algoritmo
    try:
        clf.fit(X_train,y_train.ravel())
    except:
        return 0, clf
    #X_test = scaler.transform(X_test)
    yhat[test_index] = clf.predict(X_test)
    acc.append(metrics.accuracy_score(yhat[test_index].round(), y_test.round(), normalize=False))
    i=i+1
  #print ('Score medio: '+ str(np.mean(acc)))
    return yhat, clf
  


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:/BuscaInfomoney-85bb0aa05d22.json"


sql = "SELECT * FROM dados_b3.historico_b3_N where D0_DATAPREG >= '2019-01-01' order by D0_DATAPREG"

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
            v_real = real_3['VARI_D0'] 
            v_real=  v_real.values
            y_real = y_real.values
        except:
            print(str(row[0]))
        print('EMPRESA: {} - {}'.format(row[0],row[1],))
        
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
          
      
        
        for name, algor in algors.items():
            
            col_algor = 'predito_' + str(name)
            try:
                df_3[col_algor], clf = SVM_TimeSplit(X,y,n_splits,algor,name)
         
            
            except:
                n_splits = int((df_3.__len__() * 0.6))
                df_3[col_algor], clf = SVM_TimeSplit(X,y,n_splits,algor,name)
            
            
    
            try:
                real_3[col_algor] = clf.predict(real_3.iloc[:,0:90])
                real_3['FLAG_VAR_D0'] = y_real
                real_3['VARI_D0'] = v_real
                real_3['CODNEG'] =  row[0]
                
                
            except:
                print(str(row[0]))
                
        
        try: 
            
            real_pred = pandas.concat([real_pred,real_3],sort=True)
        except:
            real_pred = real_3


#real_pred = real_pred.iloc[0:0]


to_drop_2 = ['NOMRES','EMPRESA','week','MONTH','YEAR',
       'day_1','day_2','day_3','day_4','day_5',
       'week_2_w','week_2_y','week_3_w','week_3_y','week_4_w','week_4_y',
       'month_2_w','month_2_y','month_3_w','month_3_y','month_4_w','month_4_y',
       'PREABE_D0','PREULT_D0','QUATOT_D0',]        
        
df_hist_2 = df_hist.drop(to_drop_2,axis=1)
df_hist_2.sort_values(by=['D0_DATAPREG'])
df_hist_2 = df_hist_2.set_index('D0_DATAPREG')


df_total = pandas.concat([df_hist_2,real_pred],sort=True)
#df_total['SCORE'] = df_total['predito_Rede_Neural'] + df_total['predito_SVC_RBF'] + df_total['predito_SVR_RBF'] + df_total['predito_SVR_SCAL']


df_total.to_csv('C:/Users/biel_/Documents/GitHub/tccbi17/load/BASE_PREDITA_B3.csv')


#Proximos Passo
#Incluir VARI_D0
#Loop para diversos Algoritmos






