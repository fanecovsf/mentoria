from models.animal import Animal

class Rabbit(Animal):
    eye_color:str

    def __init__(self, size:int, age:int, eye_color:str):
        super().__init__(size, age)
        self.eye_color = eye_color

    def __str__(self) -> str:
        return f'Rabbit: {self.size}cm, {self.age} years, {self.eye_color}'

