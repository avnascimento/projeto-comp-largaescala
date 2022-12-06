import os

from sqlalchemy import (Column, Integer, MetaData, String, Table, Float,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

product = Table(
        'product',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(100)),
        Column('price', Float),
        Column('gender', String(50)),
        Column('category', String(100))
)

database = Database(DATABASE_URI)
