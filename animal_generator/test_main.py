from fastapi.testclient import TestClient

import animal
from main import app, animals

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Animals list": len(animals)}


def test_get_animals():
    response = client.get("/animals")
    assert response.status_code == 200
    assert response.json() == {"Animals": animals}


def test_create_fish():
    animal_id = 1
    character = "a"
    response = client.post(f"/fish/{animal_id}/{character}")
    assert response.status_code == 200
    assert character.upper() in animals[animal_id].name
    assert isinstance(animals[animal_id], animal.Fish)


def test_create_bird():
    animal_id = 2
    character = "b"
    response = client.post(f"/bird/{animal_id}/{character}")
    assert response.status_code == 200
    assert character.upper() in animals[animal_id].name
    assert isinstance(animals[animal_id], animal.Bird)


def test_create_terrestrial():
    animal_id = 3
    character = "c"
    response = client.post(f"/terrestrial/{animal_id}/{character}")
    assert response.status_code == 200
    assert character.upper() in animals[animal_id].name
    assert isinstance(animals[animal_id], animal.Terrestrial)


def test_update_animal():
    animal_id = 4
    character = "c"
    client.post(f"/terrestrial/{animal_id}/{character}")

    new_name = "Marlin"
    new_color = "orange"
    data = {"name": new_name, "color": new_color}
    response = client.put(f"/{animal_id}", json=data)
    assert response.status_code == 200
    assert response.json() == {"Success": "Info updated"}
    assert animals[animal_id].name == new_name
    assert animals[animal_id].color == new_color


def test_delete_animal():
    animal_id = 4
    character = "b"
    response = client.post(f"/bird/{animal_id}/{character}")
    assert response.status_code == 200
    assert animal_id in animals

    response = client.delete(f"/{animal_id}")
    assert response.status_code == 200
    assert response.json() == {"Success": "Animal deleted"}
    assert animal_id not in animals
