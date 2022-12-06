from app.api.models import Product
from app.api.db import product, database


async def add_product(payload: Product):
    query = product.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_products():
    query = product.select()
    return await database.fetch_all(query=query)

async def get_product(id):
    query = product.select(product.c.id==id)
    return await database.fetch_one(query=query)

async def delete_product(id: int):
    query = product.delete().where(product.c.id==id)
    return await database.execute(query=query)

async def update_product(id: int, payload: Product):
    query = (
        product
        .update()
        .where(product.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)