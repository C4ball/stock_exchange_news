#from googlesearch import search
import calendar
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

noticias = []
enderecos = []



my_api_key = "AIzaSyCTrqogVnf_Oh8QT52VsUAsBFiBPCKZWLk"
my_cse_id = "001357824499823729082:zjs1ww-woeu"

def google_search(search_term, api_key, cse_id, **kwargs):
      service = build("customsearch", "v1", developerKey=api_key)
      res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
      return res['items']

for mm in range(1,13):
    
    ult_dia = calendar.monthrange(2018,mm)[1]
    
    range_data = 'date:r:2018' + str(f'{mm:02}') + '01:2018' + str(f'{mm:02}') + str(f'{ult_dia:02}')
    print(range_data)
    for i in range(0,10):
        try:
            results = google_search("petrobras",my_api_key,my_cse_id,start=(i*10 +1),sort = range_data ) 
            
            for result in results:
                enderecos.append(result["link"])  
        except:
            break
        #print(result["link"])





#for url in search ('petrobras site:www.infomoney.com.br', stop=20):
#    enderecos.append(url)
    
    
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
    salva_arquivo('E:/Impacta/TCC/dados/infomoney/infomoney_'+str(noticias.index(noticia))+'.html', texto)    
