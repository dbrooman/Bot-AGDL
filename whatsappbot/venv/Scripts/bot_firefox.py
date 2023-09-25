#bibliotecas
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#navegar até whatsapp web
s = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=s)
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#definir grupos e msgs
contatos = ['Trio JDL']
mensagens = """Testando bot no Firefox"""


#buscar contatos
#campo de pesquisa: copyable-text selectable-text
def buscar_contato(contato):
    campo_pesquisa = driver.find_elements(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa[0].click()
    campo_pesquisa[0].send_keys(contato)
    campo_pesquisa[0].send_keys(Keys.ENTER)

#escrever msg
#campo de msg: copyable-text selectable-text
def enviar_msg(mensagem):
    campo_msg = driver.find_elements(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_msg[1].click()
    campo_msg[1].send_keys(mensagem)
    campo_msg[1].send_keys(Keys.ENTER)
    time.sleep(3)
    campo_msg[1].send_keys(Keys.ENTER)


#main
s = input("""O que você quer fazer?
        1- Enviar algo novo
        2- Editar uma msg programada \n""")
for contato in contatos:
    buscar_contato(contato)
    enviar_msg(mensagens)