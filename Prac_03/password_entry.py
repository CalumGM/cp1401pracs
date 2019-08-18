MIN_LENGTH = 5
password = input("Please enter your password: ")
while len(password) < MIN_LENGTH:
    print("Invalid Password")
    password = input("Please enter your password: ")
print("*" * len(password))
