# TEMP: pydantic models
from pydantic import BaseModel
from typing import List

# fastapi can automatically validate data coming in
# and format data going out
# based on Pydantic models 
class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]