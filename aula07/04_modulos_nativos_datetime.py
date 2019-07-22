#!/usr/bin/python3

# Referencia


from datetime import datetime
from datime import datetime

print ('-----------------------------------------')

print('data atual', datetime.now(), sep=': ')

print ('-----------------------------------------')

#
#

print('Data atual formatada', datetime.now().strftime('%d/%m/%Y %H:%M:%S'), sep=': ')



print ('-----------------------------------------')

hoje = date.today

# hoje + 45 dias
data_final = date.frommordinal(hoje.toordinal() + 45)
diferenca = data_final - hoje

print ('Inicio {}\nFim {}\nDiferença {} dias'\
    .format(hoje.strftime('%d/%m/%Y'), data_final.strftime('%d/%m/%Y'), diferenca.days))



print ('-----------------------------------------')

data_nascimento = date(1975,7,11)
hoje = date.today()
dias = hoje - data_nascimento
idade = int(dias.day / 365)

print ('Idade: {} anos'.format(idade))

print ('-----------------------------------------')