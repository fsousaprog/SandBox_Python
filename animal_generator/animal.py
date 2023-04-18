from abc import ABC, abstractmethod
from tkinter import messagebox


# Base class for Animals with necessary attributes and abstract methods
class Animal(ABC):
    name: str = ""
    color: str = ""

    # Constructor with necessary attributes
    def __new__(cls, name: str, color: str):
        cls.name = name
        cls.color = color
        return super(Animal, cls).__new__(cls)

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
