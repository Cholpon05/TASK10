class Animal:
    def ability(self):
        print('survive')

class Dog:
    def ability(self):
        print('identify different smells')


class Cat:
    def ability(self):
        print('klimbing')

class bird:
    def ability(self):
        print('fly')


chore = [Cat(), Dog(), bird()]
for i in chore:
    i.ability()