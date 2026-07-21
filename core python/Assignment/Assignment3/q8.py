"""Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha) """
import random
user_id= input("enter the user id:")
password = int(input("enter the password"))

if user_id=="shivani" and password==1234:
    print("login successfuly")
    
    captcha= random.randint(1000,9999)
    print("captcha",captcha)
    user_captcha=int(input("enter  the captcha:"))
    
    if captcha==user_captcha:
        print("sucessful captcha match")
    else:
        print("captcha is not match")
else:
    print("invalid user id and password")