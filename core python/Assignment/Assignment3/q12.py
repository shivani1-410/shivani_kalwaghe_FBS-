# 12. Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("enter the 3 digit number:"))
a= num%10
b= (num//10)%10
c = num//100
rev = a*100+b*10+c
if num==rev:
    print("palindrome number:")
else:
    print(" not palindrome number")
    