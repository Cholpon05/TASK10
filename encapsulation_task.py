class User:
    name = 'Cholpon'
    _phone = 777555
    __password = '157954vg'
    def __init__(self, name):
        self.name = name

    def get_password(self):
        return self.__password
b = User("Cholpon")
print(b.name)
print(b._phone)
print(b.get__password())