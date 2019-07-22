#!/usr/bin/python3

nomes = ['daniel', 'maria', 'joao', 'pedro']

busca = input('Digite o nome de uma pessoa: ')

for nome in nomes:
    if busca.lower().strip() == nome:
        print('Convidado {} está na lista!'.format(nome))
        break
else:
    print('{} não está na lista!'.format(busca))