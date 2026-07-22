# WAP to check if a given number is prime number or not.

n= int(input("enter the number you  want:"))

if n>1:
    for i in range(2,n):
        print(i)
        if(n%i==0):
            print(f"{n} is not prime number")
            break
    else:
            print(f'{n} is prime number ')
else:
    print(f'{n} is not prime number.')
        
    