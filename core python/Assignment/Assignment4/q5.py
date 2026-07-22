# 5. WAP to print Fibonacci series upto n.
n=int(input("how many fibonacci number you want:"))
a =int(input("enter the number"))
b = int(input("enter the number"))
for i in range(n):
    c= a+b
    print(c)
    
    a=b
    b=c