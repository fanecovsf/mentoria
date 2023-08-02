from entities import Triangle
from util import Util

print('Enter the measures of triangle X:')

aX = float(input())
bX = float(input())
cX = float(input())

print('Enter the measures of triangle Y:')

aY = float(input())
bY = float(input())
cY = float(input())

triangleX = Triangle(aX, bX, cX)
triangleY = Triangle(aY, bY, cY)

print(f"Triangle X area: {triangleX.area()}")
print(f"Triangle Y area: {triangleY.area()}")

print(Util.largerArea(triangleX.area(), triangleY.area()))