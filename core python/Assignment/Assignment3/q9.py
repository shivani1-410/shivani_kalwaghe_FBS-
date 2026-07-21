# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
s1 = int(input("enter the first subject mark :"))
s2 = int(input("enter the second subject mark:"))
s3 = int(input("enter the third subject mark:"))
s4 = int(input("enter the fourth subject mark:"))
s5 = int(input("enter the five subject mark:"))
total=s1+s2+s3+s4+s5
per=(total/500)*100

if per>=35:
    print("pass")
    if per>=80:
        print("grade O (first class)")
    elif per<80 and per>=65:
        print("grade A (second class)")
    else:
        print("grade B(third class)")
else:
    print("fail")
        
    