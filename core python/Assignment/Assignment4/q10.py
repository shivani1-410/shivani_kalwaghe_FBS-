# 10. WAP to check if given number is Perfect Number.

num = int(input("enter the number:"))

i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1

if num==sum:
    print("number is perfect number:")
else:
    print("number is not perfect number:")