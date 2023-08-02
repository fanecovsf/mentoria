from animal import Animal

class Rabbit(Animal):
    def __init__(self, size, age, eyeColor):
        super().__init__(size, age)
        self.eyeColor = eyeColor

    def __str__(self):
        return f'{self.size}cm, {self.age} years, {self.eyeColor}'
    

class Dog(Animal):
    def __init__(self, size, age, race):
        super().__init__(size, age)
        self.race = race

    def __str__(self):
        return f'{self.size}cm, {self.age} years, {self.race}'
    

class Cat(Animal):
    def __init__(self, size, age, color):
        super().__init__(size, age)
        self.color = color

    def __str__(self):
        return f'{self.size}cm, {self.age} years, {self.color}'
