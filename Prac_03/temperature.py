"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    get_choice(choice, MENU)
    print("Thank you.")


def get_choice(choice, MENU):
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            calculate_celsius(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            calculate_fahrenheit(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def calculate_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def calculate_fahrenheit(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


main()
