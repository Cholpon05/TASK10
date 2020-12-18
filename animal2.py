class Animal:  # parent
    def can_survive(self):
        print('Init Animal')

    def can_breathe(self):
        print('Animals can survive')


class Cat(Animal):
    def can_hunt(self):
        print('Init Tiger')

    def can_climb(self):
        print('Cat can climb')


class Tiger(Cat):
    def can_run(self):
        print('Init Tiger')


d = Tiger()
d.can_breathe()
d.can_hunt()
print(Tiger.__mro__)