gender=input("enter the gender{M or F}")
age =int(input("enter the age:"))

if gender == 'M':
    if age>=18:
        print("girl is eligibale to maryy")
    else:
        print("girl is not eligible to marry")
else:
    if age>=21:
        print("boy is eligible to maryy")
    else:
        print("boy is not eligible to maryy")
        