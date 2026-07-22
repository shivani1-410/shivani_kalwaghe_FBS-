# 12. Write a program to check if given number is Armstrong number or not.

no = int(input("enter the number you want to check:"))
count=len(str(no))
temp=no
rev=0
while no>0:
    d=no%10
    rev=rev+(d**count)
    no=no//10
print(rev)
if rev==temp:
    print("number is armstrong")
else:
    print(" number is not armstrong")