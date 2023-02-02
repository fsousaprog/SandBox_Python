import random

import animal
import utils

names = ['Muffin', 'Jerry', 'Cake', 'George VII', 'Spartacus', 'Leopold', 'Little Dean', 'Cookie', 'Xavier', 'William',
         'Zeus', 'Ygor', 'Biscuit', 'Ferdinand']
colors = ['blue', 'green', 'brown', 'orange', 'black', 'white', 'striped']
name, color, new_animal = '', '', animal


# Creates and underwater animal
def create_fish():
    global new_animal
    define_animal()
    new_animal = new_animal.Fish(name=name, color=color)
    new_animal.make_sound()


# Creates a flying animal
def create_bird():
    global new_animal
    define_animal()
    new_animal = animal.Bird(name=name, color=color)
    new_animal.make_sound()


# Creates a ground animal
def create_terrestrial():
    global new_animal
    define_animal()
    new_animal = animal.Terrestrial(name=name, color=color)
    new_animal.make_sound()


# Generates the animal data
def define_animal():
    global name
    global color
    character = input('Type a single character that must be included in the name: ')
    if len(character) > 1 or character.isnumeric():
        raise ValueError("It must be a single non-numerical character")
    criteria_names = [word.upper() for word in names if word.__contains__(character.upper())
                      or word.__contains__(character)]
    name = criteria_names[random.randint(0, len(criteria_names) - 1)]
    color = colors[random.randint(0, 6)]


# Iterated menu
utils.log('Starting Animal Generator 3000')
while True:
    print('Animal generator 3000')
    print('1-Generate a random Bird')
    print('2-Generate a random Terrestrial animal')
    print('3-Generate a random Fish')
    print('4-Describe last animal generated')
    print('5-Exit')
    choice = input('Choice: ')

    match choice:
        case '1':
            create_bird()
        case '2':
            create_terrestrial()
        case '3':
            create_fish()
        case '4':
            new_animal.describe()
        case '5':
            break

utils.log('Finishing Animal Generator 3000')
