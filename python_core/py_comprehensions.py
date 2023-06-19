# Python comprehensions
import time
from collections import defaultdict

if __name__ == "__main__":
    ext_str = lambda x: x[:2]
    animais = [
        ("Pato", "Ave"),
        ("Pato", "Ave"),
        ("Pato", "Ave"),
        ("Canário", "Ave"),
        ("Canário", "Ave"),
        ("Porco", "Mamífero"),
        ("Jacaré", "Réptil"),
    ]
    # Lista

    start_time = time.time()
    aves = []
    for index, animal in enumerate(animais):
        print(index)
        if animal[1] == "Ave":
            aves.append(animal[0])
    end_time = time.time()

    print("Normal", f"{aves}, {end_time - start_time}")
    start_time = time.time()
    aves_c = [animal[0] for animal in animais if animal[1] == "Ave"]
    end_time = time.time()
    print("Comprehension", f"{aves_c}, {end_time - start_time}")
    aves_c_2 = [
        ext_str(animal[0])
        for animal in animais
        if animal[1] == "Mamífero"
    ]
    print(aves_c_2)

    # Tuplas
    # DONE: Criar um gerador que tenha o mesmo comportamento que a compreehension
    start_time = time.time()

    def aves_generator():
        for animal in animais:
            if animal[1] == "Ave":
                yield animal[0]


    ave_g = aves_generator()
    for ave in ave_g:
        print("Normal", f"{ave}")
    end_time = time.time()
    print(f"Normal duration:{end_time - start_time}")

    start_time = time.time()
    aves_c = (animal[0] for animal in animais if animal[1] == "Ave")
    for ave in aves_c:
        print("Comprehension", f"{ave}")
    end_time = time.time()
    print(f"Comprehension duration:{end_time - start_time}")

    # Dicionário
    aves_dict = {
        animal[0]: animal[1]
        for animal in animais
        if animal[1] == "Ave"
    }
    mamals_dict = {
        animal[0]: animal[1]
        for animal in animais
        if animal[1] == "Mamifero"
    }
    reptiles_dict = {
        animal[0]: animal[1]
        for animal in animais
        if animal[1] == "Réptil"
    }
    print(aves_dict)
    animals_list = [aves_dict, mamals_dict, reptiles_dict]

    # DONE: transformar a lista de tuplas em um dicionário usando compreehensions
    animals_dict = defaultdict(list)
    [animals_dict[tipo].append(nome) for nome, tipo in animais if nome not in animals_dict[tipo]]
    print(animals_dict)

    # Set
    aves_set = {animal[0] for animal in animais if animal[1] == "Ave"}
    aves_dict_list = [animal for animal in animals_list]
    aves_dict_generator = (animal for animal in animals_list)
    print(aves_set)
    print(aves_dict_list)
    print(aves_dict_generator)

    for dict_item in aves_dict_generator:
        print(dict_item)
