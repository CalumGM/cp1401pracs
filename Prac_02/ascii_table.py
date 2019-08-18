valid_input = False
LOWER_LIMIT = 33
UPPER_LIMIT = 127

while valid_input is not True:
    character = input("Input a character: ")
    number = int(input("Enter a number between 33 and 127: "))
    if LOWER_LIMIT <= number >= UPPER_LIMIT:
        valid_input = True


print("The ASCII code for {} is: {}".format(character, ord(character)))
print("The character for {} is: {}".format(number, chr(number)))

for i in range(33, 127, 1):
    print("{} {}".format(i, chr(i)))
