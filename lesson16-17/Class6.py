class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        if name in self.items:
            self.items[name] += qty
        else:
            self.items[name] = qty

    def total(self):
        return sum(self.items.values())

inv = Inventory()
inv.add("Sword", 1)
inv.add("Shield", 1)
inv.add("Potion", 5)

print(f"Общее количество предметов: {inv.total()}")
