#Write a program to swap two numbers without using third variable.
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
a=a+b
b=a-b
a=a-b
print(f"num1 = {a} and num2= {b}")