from sqlite3 import Cursor
import psycopg2

from common.config import *

conn = psycopg2.connect(f'dbname={DBNAME} user={USER} password={PASS}')
cur = conn.cursor()
class Base():
    def __init__(self,) -> None:
        self.cur = cur
        self.conn = conn



class AddTaskDB(Base):
    def __init__(self,) -> None:
        self.cur = cur
        self.conn = conn
    def add_task_with_options(self,content, level_id, photo_id,cate_id):
        self.cur.execute('insert into two(content, level_id, photo_id,cate_id) values(%s,%s,%s,%s)',(content, level_id, photo_id,cate_id,))
        self.conn.commit()
    def add_task_with_options_without_photo(self,content, level_id,cate_id):
        self.cur.execute('insert into two(content, level_id,cate_id) values(%s,%s,%s)',(content, level_id,cate_id,))
        self.conn.commit()
    def add_users(self,fullname, telegram_id, life, balans):
        self.cur.execute('insert into users(fullname, telegram_id, life, balans) values(%s,%s,%s,%s)',(fullname, telegram_id, life, balans))
        self.conn.commit()
    def add_options(self,option, task_id):
        self.cur.execute('insert into options(options, task_id) values(%s,%s)',(option, task_id))
        self.conn.commit()
    def add_words(self,words, value, cate_id,photo_id):
        self.cur.execute('insert into word(words, value, cate_id,photo_id) values(%s,%s,%s,%s)',(words, value, cate_id,photo_id))
        self.conn.commit()

    def add_shop(self,value, user_id):
        self.cur.execute('insert into shop(value, user_id) values(%s,%s)',(value, user_id,))
        self.conn.commit()

    def add_answer(self,answer):
        self.cur.execute('insert into answer(answer) values(%s)',(answer,))
        self.conn.commit()

class GetTaskDB(Base):
    def __init__(self,) -> None:
        self.cur = cur
        self.conn = conn
        self.list_id = {}
    def get_id_level(self,level):
        self.cur.execute('select id from levels where level = %s;',(level,))
        level_id = self.cur.fetchone()
        for l in level_id:
            return l
    def get_id_categoria(self,title):
        self.cur.execute('select id from categoria where title = %s;',(title,))
        cate_id = self.cur.fetchone()
        for l in cate_id:
            return l

    def get_id_two(self,content):
        self.cur.execute('select id from two where content = %s;',(content,))
        two_id = self.cur.fetchone()
        for l in two_id:
            return l
class ViewDB(Base):
    def view_two_with_photo(self):
        self.cur.execute('select content from two; ')
        return self.cur.fetchall()
    def view_two_without_photo(self):
        self.cur.execute('select * from two; ')
        return self.cur.fetchall()
    def view_options(self):
        self.cur.execute("select two.content, string_agg(o.options,', ') from two join options o on o.task_id = two.id  group by two.content; ")
        return self.cur.fetchall()
    def word_view(self):
        self.cur.execute('select * from word; ')
        return self.cur.fetchall()
db = ViewDB()
# for i in db.word_view():
#         print(i[4])
# # d = AddTaskDB()
# d.add_task_with_options(content='Oa',level_id='14',cate_id='4',photo_id='bar1')
