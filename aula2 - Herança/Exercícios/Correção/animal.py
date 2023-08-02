class Animal:
    def __init__(self, size, age):
        self.size = size
        self.age = age

    def __str__(self):
        return f'Animal size: {self.size}, Animal age: {self.age}'
    
    def yearsRemaining(self):
        return 20 - self.age