
import json
from dateutil import parser

tweets = []
for line in open('petrobras_2019-03-14_to_2019-03-20.json', 'r'):
    tweets.append(json.loads(line))


txt = open("tweets.csv","w", encoding="utf-8")

for tweet in tweets:
    ID = ()
    CRIADO = ()
    USER = ()
    EMPRESA = ()
    TEXTO = ()
    LINGUA = ()
    RETWEET = ()    
    ID =        str(tweet['id'])
    CRIADO =    parser.parse(str(tweet['created_at']))
    USER =      str(tweet['user']['screen_name'])
    EMPRESA =   'Petrobras'
    TEXTO =     str(tweet['text']).replace("\n", "")
    LINGUA =    str(tweet['lang'])
    RETWEET =   str(tweet['retweet_count'])  
    texto = ID + "|" + str(CRIADO) + "|" + USER + "|"  + EMPRESA + "|" + TEXTO + "|" + LINGUA + "|" + RETWEET + "\n"
#    print(texto)
    txt.write(texto)

txt.close()