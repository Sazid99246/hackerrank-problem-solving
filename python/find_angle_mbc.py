import math

a= float(input())
b = float(input())

r = math.atan2(a,b)
d = math.degrees(r)

print(int(round(d)),chr(176),sep="")