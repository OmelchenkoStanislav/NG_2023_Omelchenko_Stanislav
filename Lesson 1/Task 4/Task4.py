import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = pow(b, 2)-4*a*c

if D==0:
    x1=-b/(2*a)
    print("One root: ", x1)
if D>0:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
    print("Two roots: ", x1, x2)
if D<0:
    print("No roots")


