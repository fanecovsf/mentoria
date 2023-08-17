from models.animal import Animal

class Dog(Animal):
    race:str

    def __init__(self, size:int, age:int, race:str):
        super().__init__(size, age)
        self.race = race

    def __str__(self) -> str:
        return f'Dog: {self.size}cm, {self.age} years, {self.race}'