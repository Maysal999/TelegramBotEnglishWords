from sqlalchemy import create_engine, delete, String

from .config import *

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}/task_1",echo=True)




stmt = (delete(engine).where(engine.c.id == 2)) 