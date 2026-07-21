# Write a program to check if person is eligible to marry or not (male age >=21 andfemale age>=18)
gender = input("enetr the gender: ")
age = int(input("enetr the age :"))
if gender=='M':
    if age>=21:
        print("person is eligible to marry")
    else:
        print("person is not eligible ")
else:
    if age>=18:
        print("girl is eligible to marry")
    else:
        print("girl is not eligible to marry")