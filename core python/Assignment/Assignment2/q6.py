# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
basic = float(input("enter the basic salary:"))
DA = basic*10/100
TA = basic*12/100
Hra = basic*15/100
total_salary = basic+DA+TA+Hra

print("Total_Salary",total_salary)