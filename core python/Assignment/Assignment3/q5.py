# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("enter the first side of triangle:"))
b = int(input("enter the second side of triangle:"))
c= int(input("enter the third side of triangle:"))
if a+b>c and b+c >a and c+a>b:
    print("triangle is valid")
    if a==b==c:
      print("triangle is equilateral")
    elif a==b and b==c and c==a:
      print("tringle is isosceles")
    elif a!=b and b!=c and c!=a:
        print("triangle is scalene")
else:
    print("triangle is invalid")