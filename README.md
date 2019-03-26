# tccbi17
Material TCC - Pos BI 17 - Impacta

# Integrantes do Time:
* Alberica Macedo
* Gabriel Caballeria
* Pedro Coelho
* Rodrigo Dias

# Objetivo deste Projeto:
* Criação de crawler para download de sites de notícias sobre determinadas empresas que operam na bolsa de valores.
* Criação de crawler para download de Tweets referentes a determinadas empresas que operam na bolsa de valores.

# Pré-Requisitos para Utilização:
	
* Python 3.6 ou superior
	* Bibliotecas em uso:
		* calendar
		* urllib.request
		* bs4
		* googleapiclient.discovery
		* JSON
		* Tweepy
		* datetime
		* time
		* sys
			
* Conta de Desenvolvimento no Google Search API
	* Realizar inscrição no Google Cloud como Desenvolvedor
		* *Os experimentos foram realizados com o tipo gratuito de conta*
	* Criar item de busca personalizada no console do Google informando o nome do site que você usará de domínio de busca (em nosso exemplo estamos utilizando: www.infomoney.com.br):
		* Link: (https://cse.google.com/all)
		* Passo a passo: (https://support.google.com/customsearch/answer/4513886?visit_id=636858480447685538-3446621163&rd=1)

* Conta de Desenvolvimento no Twitter
	* Realizar inscrição no Twitter como Desenvolvedor
		* *Os experimentos foram realizados com o tipo gratuito de conta*
	* Criar um App no Twitter no link: https://developer.twitter.com/en/apps
	* Gerar:
		* Consumer API keys
		* Access token & access token secret
	
# Guia de Instalação - Crawler Sites (search\gsearch02.py)

* Lembre-se de ter criado a sua API Key e CSE ID conforme informado nos pré-requisitos.

* Faça checkout do projeto em:
(https://github.com/rodrigodds/tccbi17.git)

* Exporte o conteúdo do projeto para uma pasta a sua escolha.

* Abra o arquivo my_api_key.txt e o preencha com sua API Key do Google Search.
	* Formato: AIzaSyBRExxxxxxxxxagr7SrekU5c-xxxxxxxxx

* Abra o arquivo my_cse_id.txt e o preencha com o seu CSE ID do Google Search.
	* Formato: 000000024499823729082:xxxxxx-xxxx

* Verifique no programa "gsearch02.py" se as variaveis globais estão de acordo com a sua necessidade:

```
#Variáveis Globais
foldercargas = 'infomoney/Cargas/'
empresas = ['petrobras','vale', 'sabesp', 'cemig', 'Itaú Unibanco']
```

* Execute o programa "gsearch2.py" em seu console Python:
	* python gsearch2.py

* Aguardo o término da execução onde o programa criará a sub-pasta com o nome da variável "foldercargas" e uma sub-pasta para cada empresa informada em "empresas"


# Guia de Instalação - Crawler Twitter - (search\tsearch01.py)

* Baseado no projeto de Cralwer - Twitter disponível em:
	* https://galeascience.wordpress.com/2016/03/18/collecting-twitter-data-with-python/ 
	* Projeto GitHub: https://github.com/agalea91/twitter_search

* Objetivo:
	* Coleta de Tweets com determinada palavra chave, limitado a 100 tweets por retorno, onde foi criado fluxo de operação onde é possível:
		* Customizar palavras chave a serem buscadas;
		* Looping auto-gerenciável considerando a limitação da API do Twitter que suspende por 15 minutos o limite de operações sem custo;
		* Limitar a quantidade de tempo que o Crawler ficará rodando na máquina;
		* Captura e armazenagem do ID do Twitter para que a cada busca seja possível trazer somente os ID's ainda não armazenados;
		* Parametrização do range de dias que serão considerados dentro do looping de busca (limitado a 7 dias - retroativos à data atual)
		* Parametrização da região por geolocalização e range de busca dos tweets;]
		* Criação de subpasta com nome de cada palavra que será buscada, onde será armazenado o JSON gerado pelo crawler;

* Instruções de Uso:
	* Baixe o projeto em sua máquina e abra o programa tsearch01.py

	* Preencha os campos abaixo com os dados gerados no Twitter:

		```	
	    consumer_key = 'xxxxxxxxxxxxxxxx'
    	consumer_secret = 'xxxxxxxxxxxxxxxxxxx'
    	access_token = 'xxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxx'
    	access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
		```

	* Preencha os parametros de busca (search_phrases, time_limit, max_tweets, min_days_old, max_days_old):
		* Obs.: em nosso projeto estamos limitando as buscas com a geolocalização do Brasil, configurando a latitude e longitude na variável BRA;


		```
	    search_phrases = ['itau', '#itau', 
                     '#vale', 'petrobras',
                     '#petrobras']
    	time_limit = 1.5                           # runtime limit in hours
    	max_tweets = 100                           # number of tweets per search (will be
        	                                       # iterated over) - maximum is 100
    	min_days_old, max_days_old = 0, 7          # search limits e.g., from 7 to 8
                	                               # gives current weekday from last week,
            	                                   # min_days_old=0 will search from right now
    	BRA = '-23.533773, -46.625290,2500km'      # Brazil location and region
		```												   

	* Executar o programa e aguardar a execução onde serão apresentadas algumas mensagens em tela de acordo com o retorno da busca, como por exemplo:

		* Search phrase = petrobras   ----> palavra sendo buscada
		* search limit (start/stop): 2019-02-25 23:59:59     ----> limite de busca
		* since id (ending point) = 1100183661570347008     ----> ultimo ID coletado
		* found 100 tweets    ----> quantidade de tweets encontrados
		* exception raised, waiting 15 minutes      ----> limite excedido, aguardando 15 minutos
		* (until: 2019-03-04 14:37:04.087542 )      ----> próxima execução

		* Exemplo:

		![Alt text](https://github.com/rodrigodds/tccbi17/blob/master/images/img-search-json.JPG?raw=true "Exemplo Exportação")

		* Maximum number of empty tweet strings reached - exiting 	      ----> final da execução

# Guia de Instalação - Importação de Dados p/ Transformação - Dados B3 - (load\loadB3-csv.py)
	
* Realizar download da serie histórica desejada no link:
	* http://www.bmfbovespa.com.br/pt_br/servicos/market-data/historico/mercado-a-vista/series-historicas/
* Layout usado como referência:
	* http://www.bmfbovespa.com.br/lumis/portal/file/fileDownload.jsp?fileId=8A828D294E9C618F014EB7924B803F8B	 
* Abrir o programa antes de executar e alterar as variáveis:
	* bmf -> Informar o local do arquivo baixado;
	* bmfload -> informar o local de saída do arquivo CSV que será gerado;
* Na finalização do programa será geradao o arquivo: "bmf_load.csv"
* Observações: 
	* O programa está fazendo o filtro das linhas que contém o tipo de Registro - 01 - Cotações dos papéis por dia;

# Guia de Instalação - Importação de Dados p/ Transformação - Dados Twitter -  (load\loadTwitter-csv.py)
	
* Verificar qual arquivo JSON gerado anteriormente deseja ser transformado em CSV;
* Alterar o local do arquivo JSON na linha 6:
	* for line in open('petrobras_2019-03-14_to_2019-03-20.json', 'r'):
* Na finalização do programa será geradao o arquivo: "tweets_load.csv"

# Guia de Instalação - Importação de Dados p/ Transformação - Dados Notícias

* O programa de busca já gera o arquivo CSV para posterior importação, com nome: "dados_empresas.csv"




