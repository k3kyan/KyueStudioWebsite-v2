# DB structures
from pydantic import BaseModel
from typing import List

# fastapi can automatically validate data coming in
# and format data going out
# based on Pydantic models 
class FruitSchema(BaseModel):
    name: str

class FruitsSchema(BaseModel):
    fruits: List[FruitSchema]