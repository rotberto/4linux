#!/usr/bin/python3

def boas_vindas(nome):
    return 'Seja bem vindo {}'.format(nome)
    
print(boas_vindas('Roberto'))

nome = input('Informe seu nome: ')
print(boas_vindas(nome))

print(boas_vindas(nome))