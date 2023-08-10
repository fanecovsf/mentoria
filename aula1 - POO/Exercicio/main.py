from entities import Triangulo

print('Digite as medidas do triangulo 1')

t1_lado1 = float(input())
t1_lado2 = float(input())
t1_lado3 = float(input())

triangulo1 = Triangulo(t1_lado1,t1_lado2,t1_lado3)

print('Digite as medidas do triangulo 2')

t2_lado1 = float(input())
t2_lado2 = float(input())
t2_lado3 = float(input())

triangulo2 = Triangulo(t2_lado1,t2_lado2,t2_lado3)

print(triangulo1.area())
print(triangulo2.area())

if triangulo1.area() > triangulo2.area():
    print('A area do triangulo 1 é maior')
else:
    print('A area do triangulo 2 é maior')
