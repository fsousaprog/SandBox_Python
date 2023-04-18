import random

import animal

names = ['Muffin', 'Jerry', 'Cake', 'George VII', 'Spartacus', 'Leopold', 'Little Dean', 'Cookie', 'Xavier', 'William',
         'Zeus', 'Ygor', 'Biscuit', 'Ferdinand', 'Hugg']
colors = ['blue', 'green', 'brown', 'orange', 'black', 'white', 'striped']
name, color = '', ''


# Creates and underwater animal
def create_fish(character=None):
    define_animal(character)
    new_animal = animal.Fish(name=name, color=color)
    new_animal.make_sound()
    return new_animal


# Creates a flying animal
def create_bird(character=None):
    define_animal(character)
    new_animal = animal.Bird(name=name, color=color)
    new_animal.make_sound()
    return new_animal


# Creates a ground animal
def create_terrestrial(character=None):
    define_animal(character)
    new_animal = animal.Terrestrial(name=name, color=color)
    new_animal.make_sound()
    return new_animal


# Generates the animal data
def define_animal(character=None):
    global name
    global color
    if len(character) > 1 or character.isnumeric():
        raise ValueError("It must be a single non-numerical character")
    criteria_names = [word.upper() for word in names if word.__contains__(character.upper())
                      or word.__contains__(character)]
    name = criteria_names[random.randint(0, len(criteria_names) - 1)]
    color = colors[random.randint(0, 6)]
