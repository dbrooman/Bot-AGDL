#bibliotecas
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from threading import Thread

#dicionário de tag para emoticons
tag_to_emojis = {':books' : '📚',
                ':speaking' : '🗣️',
                ':ticket' : '🎟️',
                ':star' : '⭐️',
                ':clock' : '⏰',
                 ':aten' : '⚠',
                ':party' : '🥳',
                ':siren' : '🚨',
                 ':heart' : '❤',
                 ':shooting star' : '💫',
                 ':celular' : '📱'}

#dicionario de emoticon para tag
emojis_to_tag = {'📚' : ':books\t',
                '🗣️' : ':speaking\t',
                '🎟️' : ':ticket\t',
                '⭐' : ':star\t',
                '⏰' : ':clock\t',
                '⚠' : ':aten\t',
                '🥳' : ':party\t',
                '🚨' : ':siren\t',
                 '❤' : ':heart\t',
                 '💫' : ':shooting star\t',
                 '📱' : ':celular\t'}

#configurações iniciais
def initBot():
    #navegar até whatsapp web
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get('https://web.whatsapp.com/')
    time.sleep(10)
    return  driver


#definir grupos para receber
def definir_contatos():
    while(True):
        n = int(input("""Você quer enviar mensagem para:
        1- Apenas PROMOÇÕES
        2- Todos os grupos
        3- Cancelar \n"""))
        if n == 1:
            contatos = ['bots', 'PROMOÇÕES #AGDL 1.', 'PROMOÇÕES #AGDL 2', 'PROMOÇÕES #AGDL 3', 'PROMOÇÕES #AGDL 4', 'PROMOÇÕES #AGDL 5',
                        'PROMOÇÕES #AGDL 6', 'PROMOÇÕES #AGDL 7', 'PROMOÇÕES #AGDL 8', 'PROMOÇÕES #AGDL 9', 'PROMOÇÕES #AGDL 10',
                        'PROMOÇÕES #AGDL 11', 'PROMOÇÕES #AGDL 12', 'PROMOÇÕES #AGDL 13', 'PROMOÇÕES #AGDL 14', 'PROMOÇÕES #AGDL 15']
            break
        elif n == 2:
            contatos = ['bots', 'PROMOÇÕES #AGDL 1.', 'PROMOÇÕES #AGDL 2', 'PROMOÇÕES #AGDL 3', 'PROMOÇÕES #AGDL 4', 'PROMOÇÕES #AGDL 5',
                        'PROMOÇÕES #AGDL 6', 'PROMOÇÕES #AGDL 7', 'PROMOÇÕES #AGDL 8', 'PROMOÇÕES #AGDL 9', 'PROMOÇÕES #AGDL 10',
                        'PROMOÇÕES #AGDL 11', 'PROMOÇÕES #AGDL 12', 'PROMOÇÕES #AGDL 13', 'PROMOÇÕES #AGDL 14', 'PROMOÇÕES #AGDL 15',
                        'Traças Club #AGDL', 'LC ESTILHACA-ME', 'Churrasco das Traças']
            break
        elif n == 3:
            contatos = []
            break
        else:
            print("Opção não valida")
    return  contatos


def definir_telegram():
    enviar = False
    while (True):
        t = input("Enviar mensagem pro Telegram? s/n \n")[0].upper()
        if (t == 'S'):
            enviar = True
            break
        elif (t == 'N'):
            enviar = False
            break
        else:
            print("Opção não válida")
    return enviar


#definir arquivo das msgs
#Caminhos dos arquivos precisam ser atualizados
def definir_mensagem():
    while (True):
        n = input("""Qual o tipo de mensagem?
        1 - Links gerais
        2 - Promoções e cupoms avulsos
        3 - Ebooks grátis
        4 - Programadas
        5 - Cancelar \n""")
        if n == '1':
            with open('C:\\Users\\Daniele\\Documents\\Documentos\\aleatórios\\botAGDL.txt', 'r', encoding='utf8') as f:
                mensagens = f.read()
            break
        elif n == '2':
            with open('C:\\Users\\Daniele\\Documents\\Documentos\\aleatórios\\botAGDL.txt', 'r', encoding='utf8') as f:
                mensagens = f.read()
            break
        elif n == '3':
            with open('C:\\Users\\Daniele\\Documents\\Documentos\\aleatórios\\botAGDL.txt', 'r', encoding='utf8') as f:
                mensagens = f.read()
            break
        elif n == '4':
            with open('C:\\Users\\Daniele\\Documents\\Documentos\\aleatórios\\botAGDL.txt', 'r', encoding='utf8') as f:
                mensagens = f.read()
            break
        elif n == '5':
            mensagens = ""
            break
        else:
            print("Opção não valida")
    return mensagens


#definir a hora da msg
def definir_horario():
    programar = False
    while(True):
        t = input("Gostaria de definir um horario? s/n  \n")[0].upper()
        if(t == 'S'):
            resposta = input("Informe um horário (HH:MM)  ")
            horario = resposta.split(':')
            hora = int(horario[0])
            minuto = int(horario[1])
            programar = True
            break
        elif (t == 'N'):
            hora = datetime.today().hour
            minuto = datetime.today().minute
            break
        else:
            print("Opção não válida")
    return programar, hora, minuto


#buscar contatos no whatsapp web
#campo de pesquisa: copyable-text selectable-text
def buscar_contato(contato, driver):
    campo_pesquisa = driver.find_elements(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(1)
    campo_pesquisa[0].click()
    campo_pesquisa[0].send_keys(contato)
    campo_pesquisa[0].send_keys(Keys.ENTER)
    return

def substituir_emojis(mensagem):
    nova_mensagem = mensagem
    for key in emojis_to_tag:
        nova_mensagem = nova_mensagem.replace(key, emojis_to_tag[key])
    return nova_mensagem


#escrever msg
#campo de msg: copyable-text selectable-text
"""
time.sleep foi utilizado para lidar com alguns delays frutos dos funcionamento do whatsapp web de maneira prática
plinha é uma flag criada para lidar com a divisão e envio de alguns estilos de mensagem
'###' foi definido como um padrão a ser utilizado nos arquivos de texto como separador de mensagens a serem enviadas
"""
def enviar_msg(mensagem, driver, primeiro):
    campo_msg = driver.find_elements(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
    #time.sleep(3)
    campo_msg[1].click()
    mensagem = substituir_emojis(mensagem)
    msgs = mensagem.splitlines()
    plinha = True
    for part in msgs:
        if(part.find('###') >= 0):
            if (primeiro):
                time.sleep(4)
            else:
                time.sleep(1)
            campo_msg[1].send_keys(Keys.ENTER)
            plinha = True
        elif(part == ''):
            campo_msg[1].send_keys(Keys.SHIFT + Keys.ENTER)
            campo_msg[1].send_keys(part)
        else:
            campo_msg[1].send_keys(Keys.SHIFT + Keys.ENTER)
            campo_msg[1].send_keys(Keys.SHIFT + Keys.ENTER)
            campo_msg[1].send_keys(part)
            if(plinha):
                campo_msg[1].send_keys(Keys.SHIFT+Keys.ENTER)
                plinha = False
    if(primeiro):
        time.sleep(4)
    else:
        time.sleep(1)
    campo_msg[1].send_keys(Keys.ENTER)
    return


#Classe da Thread para conseguir programar várias msgs sem travar as instantâneas
class Demo(Thread):
    def __init__(self, d, cont, msgs, h, m, tele):
        self.driver = d
        self.contatos = cont
        self.mensagens = msgs
        self.hora = h
        self.minuto = m
        self.enviar_telegram = tele
        Thread.__init__(self)
        self.daemon = False
        self.stop = False
        self.start()

    def get_mensagens(self):
        return self.mensagens

    def set_mensagens(self):
        self.mensagens = definir_mensagem()
        return

    def get_hora(self):
        t = ""
        t = (str(self.hora) + ":" + str(self.minuto))
        return t

    def set_hora(self):
        resposta = input("Informe um horário (HH:MM)  ")
        horario = resposta.split(':')
        self.hora = int(horario[0])
        self.minuto = int(horario[1])
        return

    def parar(self):
        self.stop = True

    def run(self):
        if(self.enviar_telegram):
            tBot = telegramBot()
        while(True):
            if (self.stop):
                break
            if ((datetime.today().hour == self.hora) and (datetime.today().minute >= self.minuto)):
                flag = True
                for contato in self.contatos:
                    buscar_contato(contato, self.driver)
                    enviar_msg(self.mensagens, self.driver, flag)
                    flag = False
                if (self.enviar_telegram):
                    tBot.enviar(self.mensagens)
                break
        return


def alterar_programada(selecionada):
    remover = False
    while(True):
        c = input("""O que você quer fazer?
        1- Mudar horário
        2- Mudar mensagem
        3- Cancelar envio
        4- Confirmar envio\n""")
        if(c == '1'):
            selecionada.set_hora()
            break
        elif(c == '2'):
            selecionada.set_mensagens()
            break
        elif(c == '3'):
            selecionada.parar()
            remover = True
            break
        elif(c == '4'):
            break
        else:
            print("Opcão não válida")
    return remover

#Classe do bot do telegram
class telegramBot:
    def __init__(self):
        self.token = '5113898431:AAGlFvAaUtblR5G4JLT7Q0wpEPtx-t8bLy0' #token agdl
        self.url_base = f'http://api.telegram.org/bot{self.token}/'
        #self.chat_id = str(-692203402)         #id grupo bot
        #self.chat_id = str(-528387008)          #id Trio JDL
        self.chat_id = str(-1001526875636)     #id Promoções AGDL

    def substituir_tags(self, mensagem):
        nova_mensagem = mensagem
        for key in tag_to_emojis:
            nova_mensagem = nova_mensagem.replace(key, tag_to_emojis[key])
        return nova_mensagem

    def enviar(self, mensagem):
        mensagem_emojis = self.substituir_tags(mensagem)
        txt = mensagem_emojis.split('###')
        for part in txt:
            link_de_envio = f'{self.url_base}sendMessage?chat_id={self.chat_id}&text={part}&parse_mode=Markdown'
            requests.get(link_de_envio)
        return


######################################################################################################
#main
driver = initBot()
tBot = telegramBot()
programadas = []
while(True):
    s = input("""O que você quer fazer?
        1- Enviar algo novo
        2- Editar uma msg programada \n""")
    if(s == '1'):
        contatos = definir_contatos()
        telegram = definir_telegram()
        if((not contatos) and (not telegram)):
            continue
        mensagens = definir_mensagem()
        if not mensagens:
            continue
        programada, hora, minuto = definir_horario()
        if(programada):
            programadas.append(Demo(driver, contatos, mensagens, hora, minuto, telegram))
        else:
            flag = True
            for contato in contatos:
                buscar_contato(contato, driver)
                enviar_msg(mensagens, driver, flag)
                flag = False
            if(telegram):
                tBot.enviar(mensagens)
    elif(s == '2'):
        while (True):
            ja_enviadas = []
            for th in programadas:
                if (th.is_alive()):
                    continue
                else:
                    ja_enviadas.append(th)
            for msg in ja_enviadas:
                programadas.remove(msg)
            if(not programadas):
                print("Você não tem mensagens programadas")
                break
            else:
                print("Lista de msgs:")
                i = 1
                for th in programadas:
                    print("msg " + str(i) + ": " + th.get_hora() + " -> " + th.get_mensagens() + '\n')
                    print("---------------------------------------------------------------------\n")
                    i+=1
                m = 0
                while True:
                    m = int(input("Qual mensagem deseja editar? (Informe 0 para voltar)\n"))
                    if(m > len(programadas)):
                        print("Opção não válida")
                    else:
                        break
                if (m == 0):
                    break
                m-=1
                msg_progamada = programadas[m]
                apagar = alterar_programada(msg_progamada)
                if(apagar):
                    programadas.remove(msg_progamada)