class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        print(self.a * self.b)


chore = [Rectangle(3, 4)]
for i in chore:
    i.get_area()

class Square:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        print(self.a * self.b)

chore = [Square(2,2)]
for i in chore:
    i.get_area()


class Circle:
    def __init__(self, r, π):
        self.r = r
        self.π = π

    def get_area(self):
        print(self.r * self.π)

chore = [Circle(3,3)]
for i in chore:
    i.get_area()
