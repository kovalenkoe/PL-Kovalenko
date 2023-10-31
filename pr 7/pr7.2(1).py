import math
a=int(input())
def triangle(a):
    return (a ** 2) * math.sqrt(3) / 4
def triangle6(a):
    return triangle(a) * 6
print(triangle6(a))
