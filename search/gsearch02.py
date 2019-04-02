#from googlesearch import search
import calendar
from urllib.request import urlopen
#from urllib.parse import urljoin
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from threading import Thread
#import os


#Variáveis Globais
foldercargas = 'infomoney/Cargas/'
empresas = ['petrobras','vale', 'Itaú Unibanco']
textos = []

#KEYS da API do Google
with open('my_api_key.txt', 'r',encoding='utf8') as api_key:
    my_api_key = api_key.readlines()

with open('my_cse_id.txt', 'r',encoding='utf8') as cse_id:
    my_cse_id = cse_id.readlines()



print(my_api_key)
print(my_cse_id)

with  open ('dados_empresas.csv', 'w', encoding='utf-8') as file:
    file.write('')
#Funções

#Salva arquivos no caminha indicado
def salva_arquivo(nome, conteudo):
    with  open (nome+'.csv', 'a', encoding='utf-8') as file:
        file.write(conteudo + '\n')
        file.close()

#Limpa conteúdo HTML da página e extrai conteúdo
def limpa_html(conteudo):    
    bsObj = BeautifulSoup(conteudo,'html.parser')
    for remove in bsObj (["script","style","links","h2"]):remove.extract()
    for remove in bsObj (attrs={'class':"cm-pad-10-t cm-pad-20-r"}):remove.extract()
    for remove in bsObj (attrs={'class':"info"}):remove.extract()
    for remove in bsObj (attrs={'class':"title-general"}):remove.extract()
    artigo = bsObj(attrs={'class':"article__content"})[0].text
    data = bsObj(attrs={'class':"article__date"})[0].text
    titulo = bsObj(attrs={'class':"article__title"})[0].text
    
    artigo = str.join(" ", artigo.splitlines())
    artigo = artigo.replace('|',' ')
    data = str.join(" ", data.splitlines())
    data = data.replace('|',' ')
    titulo = str.join(" ", titulo.splitlines())
    titulo = titulo.replace('|',' ')

    
    texto = data + '|' + titulo + '|' + artigo
  ##  texto = bsObj.text
    return texto  
 
#Função para retornar pesquisa no Google       
def google_search(search_term, api_key, cse_id, **kwargs):
          service = build("customsearch", "v1", developerKey=api_key)
          res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
          return res['items']


#Threads
def th(ur,foldercargas,empresa,ano):
    try:
        conteudo = urlopen(ur).read()#.decode('latin-1')
        texto = ur + '|' + empresa + '|' + limpa_html(conteudo) + '\n' 
        textos.append(texto)
        #salva_arquivo('dados_empresas', texto) 
#        print(str(ur.index(noticia)))
    except:
        print("Erro na carga de: " + ur)

#Executa consultas por empresa
for empresa in empresas:


    #Range de anos a serem buscados
    for ano in range(2018,2020):

        #Array de Links de noticias POR EMPRESA POR ANO
        noticias = []
        enderecos = []
            
        
        for mm in range(1,13):
            
            ult_dia = calendar.monthrange(ano,mm)[1]
            
            range_data = 'date:r:' + str(ano) + str(f'{mm:02}') + '01:' + str(ano) + str(f'{mm:02}') + str(f'{ult_dia:02}')
            print(empresa + ' ' + range_data)
            
            #Realiza busca no Google. Loop por . Limite de 10 Páginas (100 resultados)
            for i in range(0,10):
                try:
                    results = google_search(empresa,my_api_key[0],my_cse_id[0],start=(i*10 +1),sort = range_data ) 
                    
                    for result in results:
                        enderecos.append(result["link"])  
                except Exception as e :
                    print(e)
                    break
    
            #Extrai somente os Links de Notícias da Infomoney
            noticias =   [s for s in enderecos if "/noticia/" in s]
            
#        if not os.path.exists(foldercargas + empresa):   
#            os.makedirs(foldercargas + empresa)  
            
        threadlist = []
            
        for noticia in noticias:
            t = Thread(target=th,args=(noticia,foldercargas,empresa ,ano,))
            t.start()
            threadlist.append(t)
            
        for b in threadlist:
            b.join()

for i in textos:
    i = str(i)
    i = i.replace('\n','')
    i.encode('utf-8')   
        
    salva_arquivo('dados_empresas', i)             