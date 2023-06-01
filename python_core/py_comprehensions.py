# Python comprehensions
import time

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

    # TODO: Criar um gerador que tenha o mesmo comportamento que a compreehension
    aves = []
    def aves_generator(animais):
        for animal in animais:
            if animal[1] == "Ave":
                yield animal[0]

    ave_g = aves_generator(animais)
    print("Normal", f"{ave_g}")

    aves_c = (animal[0] for animal in animais if animal[1] == "Ave")
    for ave in aves_c:
        print("Comprehension", f"{ave}")

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

    # TODO: transformar a lista de tuplas em um dicionário usando compreehensions

    # Set
    aves_set = {animal[0] for animal in animais if animal[1] == "Ave"}
    aves_dict_list = [animal for animal in animals_list]
    aves_dict_generator = (animal for animal in animals_list)
    print(aves_set)
    print(aves_dict_list)
    print(aves_dict_generator)

    for dict_item in aves_dict_generator:
        print(dict_item)
