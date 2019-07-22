#!/usr/bin/python3

import csv

# Referencia da função open:

with open('arquivo.csv', 'w', newline = '') as arq:
    arquivo = csv.writer(arq, delimiter = ';')
    arquivo.writerow(['teste'] * 5)