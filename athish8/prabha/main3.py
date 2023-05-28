from shapes.circle import calculate_area as calculate_circle_area
from shapes.square import calculate_area as calculate_square_area

radius = 5
side = 4

circle_area = calculate_circle_area(radius)
square_area = calculate_square_area(side)

print("Circle Area:", circle_area)
print("Square Area:", square_area)
