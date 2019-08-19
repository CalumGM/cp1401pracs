MIN_LENGTH = 5


def main():
    password = get_password(MIN_LENGTH)
    display_asterisks(password)


def display_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid Password")
        password = input("Please enter your password: ")
    return password


main()
