class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

p = Point(5, 10)
p.shift(3, -2)
print(f"Координаты после смещения: x = {p.x}, y = {p.y}")
