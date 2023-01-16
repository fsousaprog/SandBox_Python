from abc import ABC, abstractmethod
from tkinter import messagebox


class Animal(ABC):
    name = ""
    color = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color
        super().__init__()

    @abstractmethod
    def make_sound(self):
        pass

    def describe(self):
        messagebox.showinfo(self.name, self.color)


class Fish(Animal):
    def make_sound(self):
        messagebox.showinfo(self.name, "Blub blub")


class Bird(Animal):
    def make_sound(self):
        messagebox.showinfo(self.name, "Piu piu piu")


class Terrestrial(Animal):
    def make_sound(self):
        messagebox.showinfo(self.name, "Rawr!")
