from abc import ABC, abstractmethod
import Parentfile as PF

class Recipe(PF, ABC):
    def __init__(self, filename = "Recipe.csv"):
        super().__init__(filename)
        
    @abstractmethod
    def show_recipe(self):
        pass
        