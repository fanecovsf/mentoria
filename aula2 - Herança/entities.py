class User:
    def __init__(self, name, lastName, email):
        self.name = name
        self.lastName = lastName
        self.email = email

    def __str__(self):
        return f'Name: {self.name}, Last name: {self.lastName}, Email: {self.email}'
    
class Manager(User):
    def __init__(self, name, lastName, email, salary):
        super().__init__(name, lastName, email)
        self.salary = salary

    def __str__(self):
        return f'{self.salary}'


user1 = User('Gustavo', 'Faneco', 'gustavo.faneco@mobyweb.com.br')

manager1 = Manager('Henrique', 'Freire', 'henrique@mobyweb.com.br', 10000)

print(manager1)


