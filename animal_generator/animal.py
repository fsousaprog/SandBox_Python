from abc import ABC, abstractmethod
from tkinter import messagebox


# Base class for Animals with necessary attributes and abstract methods
class Animal(ABC):
    name: str = ""
    color: str = ""

    #ToDo Test this code and check the differences between the structures
    def __new__(cls, name: str, color: str):
        """
        It's better to include the docstrings like this
        :param name:
        :param color:
        """
        cls.name = name
        cls.color = color
        return super(Animal, cls).__new__(cls)

    #ToDo include docstrings
    def __init__(self, name: str, color: str):
        super(Animal, self).__init__(self)
        self.name = name
        self.color = color

    #ToDo Include docstrings
    def __call__(self, name: str, color: str):
        self.name = name
        self.color = color

    #ToDo Include docstrings
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
