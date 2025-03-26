class Weapon:
    def __init__(self, name, damage, bullets: int):
        self.name = name
        self.damage = damage
        self.bullets = bullets

    def __str__(self):
        return f"{self.name} (damage: {self.damage})"

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Weapon('{self.name}', {self.damage}), Remaining bullets: {self.bullets}"