#!/usr/bin/python3

nome = 'Anonimo'

def boas_vindas():
    global nome
    nome = 'Roberto'
    return 'Seja bem vindo {}'.format(nome)

print (boas_vindas())
print(nome)