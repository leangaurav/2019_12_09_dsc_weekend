#WAP that takes area of a circle and gives back radius and circumference.

# Area = (pi)r^2                       
# circumference = 2(pi)r               ## pi = (22/7)or 3.14
# r = circumference /(2*pi)

import math 

Area = float(input('Enter area of a circle '))
radius = math.sqrt(Area/3.14)
print('radius of the circle is :{}'.format(radius))

circumference = 2*(math.pi)*radius

print('circumference of the circle is : {}'.format(circumference))

