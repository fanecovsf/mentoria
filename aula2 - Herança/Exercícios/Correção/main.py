from entities import Rabbit, Dog, Cat

rabbit = Rabbit(10, 2, 'Red')
dog = Dog(60, 4, 'Pinscher')
cat = Cat(40, 5, 'Brown')

print(f'{rabbit}, {rabbit.yearsRemaining()} years remaining')
print(f'{dog}, {dog.yearsRemaining()} years remaining')
print(f'{cat}, {cat.yearsRemaining()} years remaining')