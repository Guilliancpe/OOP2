from abc import ABC, abstractmethod
from InsertnDelete import InsertnDelete


class Recipe(InsertnDelete, ABC):
    def __init__(self, filename = "Recipe.csv"):
        super().__init__(filename)
        
    @abstractmethod
    def show_recipe(self):
        pass
        