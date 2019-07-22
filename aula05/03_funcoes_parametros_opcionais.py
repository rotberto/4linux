#!/usr/bin/python3

def boas_vindas(nome=''):
    if nome !='':
        return 'seja bem vindo {}'.format(nome)
    else:
        
print(boas_vindas())
print(boas_vindas('Roberto'))