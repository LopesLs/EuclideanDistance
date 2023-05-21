import math

x = (1, 3)
y = (5, 6)
distance = math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2))
print(f'x = {x}')
print(f'y = {y}')
print(f'Δx = x1 - y1 = {x[0]} - {y[0]} = {x[0] - y[0]}')
print(f'Δy = x2 - y2 = {x[1]} - {y[1]} = {x[1] - y[1]}')
print('d = √Δx²+Δy² = ', distance)