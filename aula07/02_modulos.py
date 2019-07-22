#!/usr/bin/python3

import os











import getpass

print ('Usuario logado no sistema', getpass.getuser (), sep= ': ')

print ('-----------------------------------------')





print('Listar diretorio', os.listdir(), sep=': ')
print('Listar diretorio', os.listdir('/home/developer'), sep=': ')













print ('-----------------------------------------')

# Criando diretorios
print('Criar diretorio', os.mkdir('pythondir'), sep=': ')
print('Criar diretorio', os.mkdir('pythondir2'), sep=': ')

# Gravando um arquivo
with open('pythondir2/testemodulo.txt', 'w') as arquivo:
    arquivo.write('teste')

# Renomeando diretorio
print('Renomear diretorio', os.rename('pythondir', 'pythonrenomeado'), sep=': ')


#Renomeando arquivo
print ('Renomear aquivo', os.rename('pythondir2/testemodulo.txt', 'pythondir2/renomemodulo.txt'), sep= ': ')



print ('-----------------------------------------')

#Executando comando do S.O
os.system('sudo apt update')

print ('-----------------------------------------')



