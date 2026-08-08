from abc import ABC, abstractmethod
from Insert import Insert


class Recipe(Insert, ABC):
    def __init__(self, filename = "Recipe.csv"):
        super().__init__(filename)
        
    @abstractmethod
    def show_recipe(self):
        pass
        