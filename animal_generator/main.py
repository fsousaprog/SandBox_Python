from typing import Optional

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

import animal_generator as generator

app = FastAPI()
animals = {}


class RequestAnimal(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None


@app.get("/")
def home():
    return {"Animals list": len(animals)}


@app.get("/animals")
def get_animals():
    return {"Animals": animals}


@app.post("/fish/{animal_id}/{character}")
def create_fish(animal_id: int, character: str = Path(None, description="Character to create name")):
    if animal_id in animals:
        return {"Animal ID already exists"}

    new_animal = generator.create_fish(character)
    animals[animal_id] = new_animal
    return {"Fish created": new_animal}


@app.post("/bird/{animal_id}/{character}")
def create_bird(animal_id: int, character: str = Path(None, description="Character to create name")):
    if animal_id in animals:
        return {"Animal ID already exists"}

    new_animal = generator.create_bird(character)
    animals[animal_id] = new_animal
    return {"Bird created": new_animal}


@app.post("/terrestrial/{animal_id}/{character}")
def create_terrestrial(animal_id: int, character: str = Path(None, description="Character to create name")):
    if animal_id in animals:
        return {"Animal ID already exists"}

    new_animal = generator.create_terrestrial(character)
    animals[animal_id] = new_animal
    return {"Terrestrial created": new_animal}


@app.put("/{animal_id}")
def update_animal(animal_id: int, new_animal: RequestAnimal):
    if animal_id not in animals:
        return HTTPException(status_code=404, detail="Animal ID not found")

    if new_animal.name is not None:
        animals[animal_id].name = new_animal.name

    if new_animal.color is not None:
        animals[animal_id].color = new_animal.color

    return {"Success": "Info updated"}


@app.delete("/{animal_id}")
def delete_animal(animal_id: int):
    if animal_id not in animals:
        return HTTPException(status_code=404, detail="Animal ID not found")

    animals.pop(animal_id)

    return {"Success": "Animal deleted"}
