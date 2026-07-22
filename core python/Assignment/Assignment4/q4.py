# 4. WAP to print factorial of a number .

'''n = int(input("enter the number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
    print("factorial=", fact)'''
    
n= int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("factorial=", fact)