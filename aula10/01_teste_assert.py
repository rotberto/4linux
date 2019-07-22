#!/usr/bin/python3

def somar (x, y):
    return x + y


def subtrair (x, y):
    return x - y


def dividir (x, y):
    return x / y


def multiplicar (x, y):
    return x * y


#assert 2 == 2, 'Não'
#assert 2 != 2, 'Não'

# testar função somar
assert somar(2, 2) == 4 , 'Obtido: {}, Esperado: 4'.format(somar(2, 2))
assert somar(2, 3) == 6 , 'Obtido: {}, Esperado: 5'.format(somar(2, 3))

# # testar função subtrair
# assert subtrair(2, 2) == 0 , 'Obtido: {}, Esperado: 0'.format(somar(2, 3))
# assert subtrair(2, 3) == 1 , 'Obtido: {}, Esperado: 1'.format(somar(5, 3))

# # testar função dividir
# assert dividir(4, 2) == 2 , 'Obtido: {}, Esperado: 2'.format(somar(4, 2))
# assert dividir(9, 3) == 2 , 'Obtido: {}, Esperado: 2'.format(somar(9, 3))

# # testar função multiplicar
# assert multiplicar(10, 2) == 20 , 'Obtido: {}, Esperado: 20'.format(somar(10, 2))
# assert multiplicar(1, 3) == 2 , 'Obtido: {}, Esperado: 4'.format(somar(1, 3))

