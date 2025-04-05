a, b, c = 10, 20, 30


# print(a)

cpf = "58372078807"

# print(cpf[-5:])

# print (cpf.isalnum())

rua = "Brauna, SP, Jardim Garrocini, Rua das rosas, 50"

# print(rua.split(","))

lista = ["Cauã", "Matheus", "Murilo", "João"]

lista.pop(0)

# print(lista)
# lista.append("Kaik")
# print(lista)
# lista.sort()
# print(lista)
# lista.insert(0, "Kauã")
# lista.index("Matheus")
# print(lista.index("Matheus"))

import datetime

# diaHoje = datetime.datetime.today().date()

# dataCriada = datetime.date(2024, 12, 1)
# data = diaHoje - dataCriada

# dataConvertida = diaHoje.strftime('%d/%m/%y')
# print(dataConvertida)

# somaData = diaHoje + datetime.timedelta(days=10)

# print(somaData)

import time

# print("Começando...")
# time.sleep(3)
# print("Carregando...")
# time.sleep(3)
# print("Iniciado!")

# dataEncontrada = "25 june, 2004"
# data = time.strptime(dataEncontrada,"%d %B, %Y")
# print(data)

# dataNova = time.strftime("%d/%m/%y, %H:%M:%S", data)
# print(dataNova)

import statistics

# lista = [20,10,40,10,85,74]

# print(statistics.mean(lista))
# print(statistics.fmean(lista))
# print(statistics.median(lista))
# print(statistics.mode(lista))

# parar = 0

# while parar <= 10:
#     parar+=1

#     print(parar)

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        print(nome , '', idade)

    def maiorIdade(self):
        if self.idade >= 18:
            print("Pode ir no rolê")
        else:
            print("Não Pode Sair")


pessoa1 =  Pessoa("Cauã", 20)
pessoa1.maiorIdade()