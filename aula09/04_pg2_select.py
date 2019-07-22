#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect(
        'host=localhost dbname=projeto\
         user=admin password=4linux'
    )

    cur = con.cursor()
except Exception as e:
        print('Erro: {}'. format(e))
        exit()

try:
    cur.execute("select * from usuarios;")
    # print (print(cur.fetchone())
    print(cur.fetchall())
except Exception as e:
    con.rollback()
    print('Erro: {}'.format(e))
finally:
    cur.close()
    con.close()