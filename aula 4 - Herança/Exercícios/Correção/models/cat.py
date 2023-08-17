from models.animal import Animal

class Cat(Animal):
    color:str

    def __init__(self, size:int, age:int, color:str):
        super().__init__(size, age)
        self.color = color

    def __str__(self) -> str:
        return f'Cat: {self.size}cm, {self.age} years, {self.color}'