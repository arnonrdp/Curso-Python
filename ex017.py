'''
from math import sqrt

opo = float(input("Cateto oposto: "))
adj = float(input("Cateto adjacente: "))
hip = math.sqrt(opo ** 2 + adj ** 2)
'''
from math import hypot

opo = float(input("Cateto oposto: "))
adj = float(input("Cateto adjacente: "))
hip = hypot(opo, adj)

print(f'O comprimento da hipotenusa é {hip}.')
