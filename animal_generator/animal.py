from abc import ABC, abstractmethod
from tkinter import messagebox


# Base class for Animals with necessary attributes and abstract methods
class Animal(ABC):
    name: str = ""
    color: str = ""

    # Constructor with necessary attributes
    # ToDo: the __init__ is not the constructor. The __new__ method that is the constructor.
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        super().__init__()

    # Each instance needs to implement its own
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
