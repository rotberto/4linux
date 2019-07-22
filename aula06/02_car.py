#!/usr/bin/python3

class Carro():
    __proprietario = 'Joaquim'

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 'gasolina'


    def __del__ (self):
        print('Metodo destrutor executado')


    def acelerar(self):
        print('Vruuun')


    def freiar(self):
        print('Freiando...')

    
    def getProprietario(self):
        return self.__proprietario


    def setProprietario(self, proprietario):
        self.__proprietario = proprietario

    
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.combustivel = 'eletrico'


    def acelerar(self):
        print('Shiiiiifffff...')

car1 = Carro('BMW', 'i320', 2016)

print(car1.modelo, car1.combustivel)

car1.acelerar()

print('Proprietario', car1.getProprietario(), sep= '\n')
# print('Proprietario', car1.__Proprietario, sep= '\n')

print('---------------------------------------------------')

car2 = CarroEletrico('Chevrolet', 'Bolt', 2018)

print(car2.modelo, car2.combustivel)
car2.acelerar()

print('Proprietario', car2.getProprietario(), sep='\n')
# print('Proprietario', car2.__Proprietario, sep='\n')

print('---------------------------------------------------')

proprietario = input('Informe o proprietario do carro eletrico')

car2.setProprietario(proprietario.strip())

print('Proprietario', car2.getProprietario(), sep='\n')