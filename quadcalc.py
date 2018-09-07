#Copyright Ashrith Kanakanala 2018
import math
import sys

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

d = (b ** 2) - (4 * a * c)

if d < 1:
    sys.exit("No Solutions")
else:
    dsqrt = math.sqrt(d)
    x1 = ((-1 * b) + dsqrt) / (2 * a)
    x2 = ((-1 * b) - dsqrt) / (2 * a)

    print("Your Solutions are",x1,"and",x2)
