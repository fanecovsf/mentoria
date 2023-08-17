from util.util import Util

from models.cat import Cat
from models.dog import Dog
from models.rabbit import Rabbit

rabbit = Rabbit(10, 2, 'Red')
dog = Dog(60, 4, 'Pinscher')
cat = Cat(40, 5, 'Brown')

print(rabbit)
print(dog)
print(cat)

print('')

print(f"{rabbit}, {rabbit.years_remaining()} years remaining")
print(f"{dog}, {dog.years_remaining()} years remaining")
print(f"{cat}, {cat.years_remaining()} years remaining")

print(Util.bigger_number(rabbit.size, dog.size, cat.size))
