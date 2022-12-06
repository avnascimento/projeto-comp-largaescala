from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    name: str
    price: float
    gender: str
    category: str
    
class ProductOut(Product):
    id: int

class ProductUpdate(Product):
    name: Optional[str] = None
    price: Optional[float] = 0.0
    gender: Optional[str] = None
    category: Optional[str] = None