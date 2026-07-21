num = int(input("Enter a 3-digit number: "))
a = num % 10
b = (num // 10) % 10
c = num // 100

rev = a * 100 + b * 10 + c
print("Reversed number =", rev)