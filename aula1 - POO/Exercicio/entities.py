class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        p = (self.lado1 + self.lado2 +self.lado3)/2
        return (p+self.lado1)*(p+self.lado2)*(p+self.lado3)
