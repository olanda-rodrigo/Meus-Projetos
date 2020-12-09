# importando bibliotecas
import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# cadastrando chaves

consumer_key = 'inserir consumer_key'
consumer_secret = 'inserir consumer_secret'

access_token = 'inserir access_token'
access_secret = 'inserir access_secret'

# definir arquivo de saída para armazenar dados 

data_hoje = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
out = open(f'dados_coletados_{data_hoje}.txt', 'w')

# implementar uma classe de conexão para o twitter

class MyListener (StreamListener):

    def on_data(self, data):
        item_string = json.dumps(data)
        out.write(item_string + '\n')
        return True

    def on_error(self, status):
        print(status)

# implementar uma função main 

if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#ForaBolsonaro'])





