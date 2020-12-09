# importando bibliotecas
import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# cadastrando chaves

consumer_key = 'RG52I3lXP3Sik5rVayqNHJB89'
consumer_secret = 'd2NEPQuzFFYNCYtxJFdBpgiDB7wB8Tf0ke4MW5jsXjuWf2TQjk'

access_token = '1332386851274043395-GSz66Y4R1OJTI46dR6d4ySC6xoXgXw'
access_secret = 'yYuuBT7Viqke6TsZwzDqVHuGWvQZsF1zpulnsClg63Wpu'

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





