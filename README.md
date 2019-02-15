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
			
* Conta de Desenvolvimento no Google Search API
	* Realizar inscrição no Google Cloud como Desenvolvedor
		* *Os experimentos foram realizados com o tipo gratuito de conta*
	* Criar item de busca personalizada no console do Google informando o nome do site que você usará de domínio de busca (em nosso exemplo estamos utilizando: www.infomoney.com.br):
		* Link: (https://cse.google.com/all)
		* Passo a passo: (https://support.google.com/customsearch/answer/4513886?visit_id=636858480447685538-3446621163&rd=1)

* Conta de Desenvolvimento no Twitter **(Em desenvolvimento)**
	* Realizar inscrição no Twitter como Desenvolvedor
		* *Os experimentos foram realizados com o tipo gratuito de conta*
	* Criar um App no Twitter no link: https://developer.twitter.com/en/apps
	* Gerar:
		* Consumer API keys
		* Access token & access token secret
	
# Guia de Instalação - Crawler Sites (gsearch02.py)

* Lembre-se de ter criado a sua API Key e CSE ID conforme informado nos pré-requisitos.

* Faça checkout do projeto em:
(https://github.com/rodrigodds/tccbi17.git)

* Exporte o conteúdo do projeto para uma pasta a sua escolha.

* Abra o arquivo my_api_key.txt e o preencha com sua API Key do Google Search.
	* Formato: AIzaSyBRExxxxxxxxxagr7SrekU5c-xxxxxxxxx

* Abra o arquivo my_cse_id.txt e o preencha com o seu CSE ID do Google Search.
	* Formato: 000000024499823729082:xxxxxx-xxxx

* Verifique no programa "gsearch02.py" se as variaveis globais estão de acordo com a sua necessidade:

#Variáveis Globais
foldercargas = 'infomoney/Cargas/'
empresas = ['petrobras','vale', 'sabesp', 'cemig', 'Itaú Unibanco']

* Execute o programa "gsearch2.py" em seu console Python:
	* python gsearch2.py

* Aguardo o término da execução onde o programa criará a subpasta "infomoney/cargas" e uma sub-pasta para as empresas que estão em nosso estudo, que são:

			
# Continua....
