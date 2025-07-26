# # TEMP: pydantic models
# # TODO: REFERENCE THESE BEFORE U DELETE THEM BC IT SHOWS WHERE THEY'VE BEEN USED !!!!

# from pydantic import BaseModel
# from typing import List

# # fastapi can automatically validate data coming in
# # and format data going out
# # based on Pydantic models 
# class Fruit(BaseModel):
#     name: str

# class Fruits(BaseModel):
#     fruits: List[Fruit]
    
    
    
    
# the actual fruits_models.py ----------------------------------------------------

from schemas.fruit_schema import FruitSchema, FruitsSchema

class FruitModel:
    def __init__(self, name: str):
        self.name = name
        
    # TODO: EXPLAIN: ???
    # Creates a FruitModel from a FruitSchema
    @classmethod
    def from_schema(cls, fruit: FruitSchema):
        return cls(fruit.name)
    
    # Converts the model into a Python dict (for JSON/db/etc)
    def to_dict(self):
        return {
            "name": self.name
        }
        
    # Converts the model back into a FruitSchema
    def to_schema(self): # maybe should be named model_to_schema
        return FruitSchema(name=self.name)
    
    # The methods are purely conversions of models to/from schema, not actual persistance or read/write etc
