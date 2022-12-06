from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Product, ProductOut, ProductUpdate
from app.api import db_manager

products = APIRouter()

MESSAGE_PRODUCT_NOT_FOUND = "Sorry, Product not found"

@products.post('/', response_model=ProductOut, status_code=201)
async def create_product(payload: Product):
    product_id = await db_manager.add_product(payload)
    response = {
        'id': product_id,
        **payload.dict()
    }

    return response

@products.get('/', response_model=List[ProductOut])
async def get_products():
    return await db_manager.get_all_products()

@products.get('/{id}/', response_model=ProductOut)
async def get_movie(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail=MESSAGE_PRODUCT_NOT_FOUND)
    return product

@products.put('/{id}/', response_model=ProductOut)
async def update_movie(id: int, payload: ProductUpdate):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail=MESSAGE_PRODUCT_NOT_FOUND)

    update_data = payload.dict(exclude_unset=True)

    product_in_db = Product(**product)

    updated_product = product_in_db.copy(update=update_data)

    return await db_manager.update_product(id, updated_product)

@products.delete('/{id}/', response_model=None)
async def delete_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail=MESSAGE_PRODUCT_NOT_FOUND)
    return await db_manager.delete_product(id)
