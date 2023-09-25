import requests
import time

#id do chat do grupo bot: -692203402

class telegramBot:
    def __init__(self):
        self.token = '5113898431:AAGlFvAaUtblR5G4JLT7Q0wpEPtx-t8bLy0'
        self.url_base = f'http://api.telegram.org/bot{self.token}/'
        self.chat_id = str(-528387008)
        self.enviar("📚 livros blablabla")

    def enviar(self, mensagem):
        link_de_envio = f'{self.url_base}sendMessage?chat_id={self.chat_id}&text={mensagem}'
        requests.get(link_de_envio)

bot = telegramBot()
token = '5113898431:AAGlFvAaUtblR5G4JLT7Q0wpEPtx-t8bLy0'
url_base = f'http://api.telegram.org/bot{token}/getUpdates'
resultado = requests.get(url_base)
print(resultado.json())
print('\@')