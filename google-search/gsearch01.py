# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 20:43:23 2019

@author: rodri
"""

from googlesearch import search
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup

noticias = []
enderecos = []

for url in search ('petrobras site:www.infomoney.com.br', stop=20):
    enderecos.append(url)
    
    
def salva_arquivo(nome, conteudo):
    with  open (nome, 'w', encoding='utf-8') as file:
        file.write(conteudo)

        
def limpa_html(conteudo):
    bsObj = BeautifulSoup(conteudo,'html.parser')
    for remove in bsObj (["script","style","links","h2"]):remove.extract()
    for remove in bsObj (attrs={'class':"cm-pad-10-t cm-pad-20-r"}):remove.extract()
    for remove in bsObj (attrs={'class':"info"}):remove.extract()
    for remove in bsObj (attrs={'class':"title-general"}):remove.extract()
        
        
        
        
    texto = bsObj(attrs={'class':"article__content"})[0].text
  ##  texto = bsObj.text
    return texto

noticias =   [s for s in enderecos if "/noticia/" in s]

for noticia in noticias:    
    conteudo = urlopen(noticia).read().decode('utf-8')
    texto = limpa_html(conteudo)
    salva_arquivo('C:/Users/rodri/OneDrive/Faculdade/Impacta/10 - TCC/coleta-google-search/infomoney_'+str(noticias.index(noticia))+'.html', texto)    