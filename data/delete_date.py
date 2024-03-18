import psycopg2

from common.config import *

conn = psycopg2.connect(f'dbname={DBNAME} user={USER} password={PASS}')
cur = conn.cursor()


def delete_date2(title: str) -> any:
    cur.execute('delete from given_task where title = %s;',(title,))
    conn.commit()
def select_categoria(categorias):
    cur.execute('select categoria from given_task where content = %s;',(categorias,))
    conn.commit()
    # def delete_date(categorias):
    #     cur.execute('select categoria from given_task where content = %s;',(categorias,))
    #     conn.commit()

d = delete_date2(title='Щодо')

print(d)