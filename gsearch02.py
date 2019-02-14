#from googlesearch import search
import calendar
from urllib.request import urlopen
#from urllib.parse import urljoin
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

#Variáveis Globais
foldercargas = 'infomoney/Cargas/'
empresas = ['petrobras','vale', 'sabesp', 'cemig', 'Itaú Unibanco']

#KEYS da API do Google
my_api_key = "AIzaSyBREm0Qs7PV_Kagr7SrekU5c-L0DQPnbRk"
my_cse_id = "001357824499823729082:zjs1ww-woeu"


#Funções

#Salva arquivos no caminha indicado
def salva_arquivo(nome, conteudo):
    with  open (nome, 'w', encoding='utf-8') as file:
        file.write(conteudo)

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
    
    
    
    texto = data + '|' + titulo + '|' + artigo
  ##  texto = bsObj.text
    return texto  
 
#Função para retornar pesquisa no Google       
def google_search(search_term, api_key, cse_id, **kwargs):
          service = build("customsearch", "v1", developerKey=api_key)
          res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
          return res['items']



for empresa in empresas:
    noticias = []
    enderecos = []
    for mm in range(1,13):
        
        ult_dia = calendar.monthrange(2018,mm)[1]
        
        range_data = 'date:r:2018' + str(f'{mm:02}') + '01:2018' + str(f'{mm:02}') + str(f'{ult_dia:02}')
        print(empresa + ' ' + range_data)
        for i in range(0,10):
            try:
                results = google_search(empresa,my_api_key,my_cse_id,start=(i*10 +1),sort = range_data ) 
                
                for result in results:
                    enderecos.append(result["link"])  
            except:
                break

        #Extrai somente os Links de Notícias da Infomoney
        noticias =   [s for s in enderecos if "/noticia/" in s]
    
    for noticia in noticias:
        try:
            conteudo = urlopen(noticia).read().decode('utf-8')
            texto = empresa + '|' + limpa_html(conteudo)
            salva_arquivo(foldercargas + empresa +'/infomoney_' + empresa + '_' + str(noticias.index(noticia)) +'.html', texto)    
        except:
            print(noticia)
            