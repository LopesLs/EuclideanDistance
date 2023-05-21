import math

# Euclidian Distance Three Dimensional
x = (1, 3, 5)
y = (5, 6, 7)
distance = math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2) + math.pow((x[2] - y[2]), 2))
print(f'x = {x}')
print(f'y = {y}')
print(f'Δx = x1 - y1 = {x[0]} - {y[0]} = {x[0] - y[0]}')
print(f'Δy = x2 - y2 = {x[1]} - {y[1]} = {x[1] - y[1]}')
print(f'Δz = x3 - y3 = {x[2]} - {y[2]} = {x[2] - y[2]}')
print('d = √Δx²+Δy²+Δz² = ', distance)