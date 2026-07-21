#Program to Find the Roots of a Quadratic Equation
import math

a = float(input("enter the value of a:"))
b = float(input("enter the value of b:"))
c = float(input("enter the value of c:"))

d = b**2-4*a*c
x1= (-b + math.sqrt(d))/(2*a)
x2 = (+b +math.sqrt(d))/(2*a)

print("root x1 is:",x1)
print("root x2 is1",x2)