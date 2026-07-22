# 9. WAP to print all numbers in a range divisible by a given number.

start = int(input("enter the starting number:"))
end = int(input("enter the ending number:"))
d=int(input("entre the divisor:"))

for i in range(start,end-1):
    if i%d==0:
        print(i)