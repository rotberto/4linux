#!/usr/bin/python3

def cadastro(**pessoa):
    #return pessoa
    #return type(pessoa)
    return 'O usuario {} {} foi cadastrado com sucesso!'.format(pessoa['nome'], pessoa['sobrenome'])


    print (cadastro(nome='Ivan',
                    sobrenome= 'Ferro',
                    idade=44))


def cadastro(pessoa):
    #return pessoa
    #return type(pessoa)
    return 'O usuario {} {} foi cadastrado com sucesso!'.format(pessoa['nome'], pessoa['sobrenome'])


    pessoa = {
                'nome': 'Ivan',
                'sobrenome': 'Ferro',
                'idade': 44             
}

print(cadastro(pessoa))