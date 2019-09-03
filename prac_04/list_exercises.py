USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = []
    for i in range(5):
        numbers.append(float(input("Enter a number: ")))
    print("The first number is: {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    average = (sum(numbers) / (len(numbers)))
    print("The average is {}".format(average))


def security_checker():
    user = input("Please enter your username: ")
    if user in USERNAMES:
        print("Access Granted")
    else:
        print("Access Denied")


main()
security_checker()
