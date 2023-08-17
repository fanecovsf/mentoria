class Animal:
    size:int
    age:int

    def __init__(self, size:int, age:int):
        self.size = size
        self.age = age

    
    def years_remaining(self):
        return 20 - self.age