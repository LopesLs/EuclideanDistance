import math
import random

x, y = [], []
dimensions = int(input("Enter the number of dimensions: "))
distance = 0

for i in range(dimensions):
  x.append(random.randint(1, 10))
  y.append(random.randint(1, 10))

print(f'x = {x}')
print(f'y = {y}')

for x, y in zip(x, y):
  distance += math.pow((x - y), 2)

print(f'Δn = nN - nN')
print('d = √Δx²+Δy²+...+Δn² = ', math.sqrt(distance))