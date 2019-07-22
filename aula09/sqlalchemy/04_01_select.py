#!/usr/bin/python3

from sqlalchemy import select
from core import user_table

#result = select([user_table])
result = select([user_table]).where(user_table.c.nome == 'João das Neves')

#for usuario in result.execute()
# print(usuario)

print (usuario for usuario in result.execute())