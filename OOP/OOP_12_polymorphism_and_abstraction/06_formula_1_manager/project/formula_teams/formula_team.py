from abc import ABC, abstractmethod

class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget
        if self.budget < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass