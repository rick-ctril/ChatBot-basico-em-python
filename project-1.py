from mailbox import linesep
from tracemalloc import start
import os
def processar_resposta(resposta,nome, email):
    if resposta == '1':
        print(f'{os.linesep}{nome} No mundo tem um total de 196 paises.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} 1-Rússia, 2-Canadá, 3-China, 4-Estados Unidos, 5-Brasil {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Há perto de 1300 linguagens de programação conhecidas, sendo que o número das mais usadas bate os 50, segundo a Tiobe.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} A floresta ombrófila aberta é considerada um tipo de vegetação da área de transição entre a Floresta Amazônica e as áreas extra-amazônicas. Tem como característica ambientes com climas mais secos, que chegam de 2 a 4 meses por ano, com temperaturas de 24 à 25°C.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome} A cidade do Recife, capital do Pernambuco, é também conhecida como a Veneza brasileira, por causa de sua paisagem cortada por rios, canais e dezenas de pontes que ligam um bairro ao outro.{os.linesep}')
    else:
        print('Digite apenas 1,2,3,4 ou 5')


def start():
    #Apresentar o chatbot
     print('Olá! Bem-vindo. ')
    #Pedir um nome 
     nome = input('Digite seu nome: ')
    #Pedir um email
     email = input('Digite um E-mail:')
    #Lop infinito
     while True:
    #Oferecer o menu de opções 
        resposta= input(
            f'O que você gostaria de saber?{os.linesep}[1] - Quantos paises tem no mundo?{os.linesep}[2] - Quais são os 5 maiores países do mundo em extensão territorial?{os.linesep}[3] - Quantas linguagens de programação existem?{os.linesep}[4] - Quais às caracteristicas da floresta ombrófila aberta?{os.linesep}[5] - Qual é a veneza brasileira?')
    #Processar a resposta enviada
        processar_resposta(resposta, nome)
if __name__ == '__main__':
 start()