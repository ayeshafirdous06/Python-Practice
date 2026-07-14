#login system using exception handling
try:
    username=input("Enter username:")
    password=int(input("enter password:"))
    if username=="wizard" and password==1234:
        print("Welcome Wizard!")
    elif username!="wizard"and password==1234:
        print("Invalid username!")
    elif username=="wizard"and password!=1234:
         print("incorrect password")
    else:
         print("invalid username and password")
except ValueError:
        print("please enter a numeric password")
finally:
     print("login system closed")
