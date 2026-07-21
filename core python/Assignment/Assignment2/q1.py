#1. Convert the time entered in hh,min and sec into seconds.

h = int(input("enter the Hours:"))
m = int(input("enter the minute:"))
s = int(input("enter the second:"))

Total_Seconds = (h*360)+(m*60)+s
print("total_seconds",Total_Seconds)
