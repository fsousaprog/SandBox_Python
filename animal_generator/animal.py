from abc import ABC, abstractmethod
from tkinter import messagebox

"""
# Base class for Animals with necessary attributes and abstract methods
"""


class Animal(ABC):
    name: str = ""
    color: str = ""

    """
    Animal class instance creator
    :param name: Name of the animal
    :param color: Color of the animal
    """

    def __new__(cls, name: str, color: str):
        cls.name = name
        cls.color = color
        return super(Animal, cls).__new__(cls)

    """
    Animal initializer method
    :param name: Name of the animal
    :param color: Color of the animal
    """

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    """
    Animal calling method as a function
    :param name: Name of the animal
    :param color: Color of the animal
    """

    def __call__(self, name: str, color: str):
        self.name = name
        self.color = color

    """
    Abstract method that's required when implementing a new animal.
    It's supposed to make a visual notification specific for the type of animal.
    """

    @abstractmethod
    def make_sound(self):
        pass


# Underwater animal
class Fish(Animal):
    def make_sound(self):
        messagebox.showinfo(self.name, "Blub blub")


# Flying animal
class Bird(Animal):
    def make_sound(self):
        messagebox.showinfo(self.name, "Piu piu piu")


# Ground animal
class Terrestrial(Animal):
    def make_sound(self):
        messagebox.showinfo(self.name, "Rawr!")
