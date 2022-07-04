import math

AB = int(input())
BC = int(input())

theta = (math.atan(AB/BC))

theta_to_degree = round(math.degrees(theta))

print(theta_to_degree, chr(176), sep = '')
