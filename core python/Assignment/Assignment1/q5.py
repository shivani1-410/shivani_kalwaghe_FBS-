#Write a program to enter P, T, R and calculate Compound Interest.

P = int(input("enter the principal amount:"))
R  = int(input("enter the rate of interest:"))
T = int (input("enter the time:"))

A = P*(1+(R/100))
CI = A-P
print("compund interest is:",CI)
