import random

import Animal
import utils

names = ['Muffin', 'Jerry', 'Cake', 'George VII', 'Spartacus', 'Leopold', 'Little Dean', 'Cookie', 'Xavier', 'William',
         'Zeus', 'Ygor', 'Biscuit', 'Ferdinand']
colors = ['blue', 'green', 'brown', 'orange', 'black', 'white', 'striped']
name, color, animal = '', '', Animal


def create_fish():
    global animal
    define_animal()
    animal = Animal.Fish(name=name, color=color)
    animal.make_sound()


def create_bird():
    global animal
    define_animal()
    animal = Animal.Bird(name=name, color=color)
    animal.make_sound()


def create_terrestrial():
    global animal
    define_animal()
    animal = Animal.Terrestrial(name=name, color=color)
    animal.make_sound()


def define_animal():
    global name
    global color
    letter = input('Type a single letter that must be included in the name: ')
    criteria_names = [word.upper() for word in names if word.__contains__(letter.upper()) or word.__contains__(letter)]
    name = criteria_names[random.randint(0, len(criteria_names) - 1)]
    color = colors[random.randint(0, 6)]


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
            animal.describe()
        case '5':
            break

utils.log('Finishing Animal Generator 3000')
