# Write a Python program to store two points as tuples and calculate the distance between them.


import math
point1 = (x1, y1) = (2, 3)
point2 = (x2, y2) = (7, 8)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between points:", distance)
