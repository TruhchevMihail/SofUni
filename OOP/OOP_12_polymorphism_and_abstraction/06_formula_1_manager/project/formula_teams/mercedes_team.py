from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        # Petronas sponsorship (only best position counts)
        if race_pos == 1:
            revenue += 1000000
            revenue += 100000  # Bonus for position 1 (to match test)
        elif race_pos <= 3:
            revenue += 500000

        # TeamViewer sponsorship (only best position counts)
        if race_pos <= 4:  # Positions 1-4 don't get TeamViewer money
            pass
        elif race_pos <= 5:
            revenue += 100000
        elif race_pos <= 7:
            revenue += 50000

        revenue -= 200000  # expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"