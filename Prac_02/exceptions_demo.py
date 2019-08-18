"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when either the numerator or denominator are not valid integers
2. When will a ZeroDivisionError occur?
when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
done
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("cannot divide by 0")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        valid_input = True
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")
