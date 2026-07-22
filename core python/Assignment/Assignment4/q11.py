# WAP to check if given number Strong Number.
num=int(input("enter the number:"))

temp=num
sum=0

while temp>0:
    d= temp%10
    
    fact=1
    for i  in range(1,d+1):
        fact=fact*i
    
    sum=sum+fact
    temp=temp//10

if  sum==num:
    print("number is strong number:")
else:
    print("number is not strong number:")