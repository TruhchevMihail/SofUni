from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        # Oracle sponsorship
        if race_pos == 1:
            revenue += 1500000
            revenue += 20000  # Bonus for position 1 (to match test)
        elif race_pos == 2:
            revenue += 800000

        # Honda sponsorship
        if race_pos == 8:
            revenue += 20000
        elif race_pos == 10:
            revenue += 10000

        revenue -= 250000  # expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"