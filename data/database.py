from sqlite3 import Cursor
import psycopg2


conn = psycopg2.connect('dbname=englishbot user=postgres password=maisal88')
cur = conn.cursor()
class Base():
    def __init__(self,) -> None:
        self.cur = cur
        self.conn = conn



class AddTaskDB(Base):
    def add_task_with_options(self,content, level_id, photo_id,cate_id):
        self.cur.execute('insert into two(content, level_id, photo_id,cate_id) values(%s,%s,%s,%s)',(content, level_id, photo_id,cate_id,))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return 
    
    def add_users(self,fullname, telegram_id, life, balans):
        self.cur.execute('insert into users(fullname, telegram_id, life, balans) values(%s,%s,%s,%s)',(fullname, telegram_id, life, balans))
        self.conn.commit()
        return  
    def add_options(self,option, task_id):
        self.cur.execute('insert into options(option, task_id) values(%s,%s)',(option, task_id))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return
    def add_words(self,words, value, cate_id):
        self.cur.execute('insert into words(words, value, cate_id) values(%s,%s,%s)',(words, value, cate_id))
        self.conn.commit()
        return
    def add_shop(self,value, user_id):
        self.cur.execute('insert into shop(value, user_id) values(%s,%s)',(value, user_id,))
        self.conn.commit()
        return
    


class GetTaskDB(Base):
    def get_id_level(self,level):
        self.cur.execute('select id from levels where level = %s;',(level,))
        level_id = self.cur.fetchone()
        for i in level_id:
            print(i)

    def get_id_categoria(self,title):
        self.cur.execute('select id from categoria where title = %s;',(title,))
        cate_id = self.cur.fetchone()
        for i in cate_id:
            print(i)

    def get_id_two(self,content):
        self.cur.execute('select id from two where title = %s;',(content,))
        cate_id = self.cur.fetchone()
        for i in cate_id:
            print(i)
