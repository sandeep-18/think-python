# Sandeep Sadarangani 5/12/18
# Password Login

import getpass

username = "sandy"
password = "hello123"

user = input("Enter Username: ")
passw = getpass.getpass("Enter Password: ")

if user != username and passw != password:
    print("Invalid login details")
else:
    print("Access Granted")
