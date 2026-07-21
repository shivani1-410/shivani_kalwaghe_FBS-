# Write a program to enter P, T, R and calculate simple Interest.
P = int (input("enter the principal amount:"))
R = int (input("enter the rate of interest:"))
T = int(input("enter the time:"))
SI = (P*R*T)/100
print("simple interest is:",SI)