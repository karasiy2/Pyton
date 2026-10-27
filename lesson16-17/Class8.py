class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["health"], data["damage"])

hero1 = Hero("Aragorn", 150, 25)

hero_data = hero1.to_dict()
print("Сохраненный словарь:", hero_data)

hero2 = Hero.from_dict(hero_data)

print(f"Health нового героя: {hero2.health}")
