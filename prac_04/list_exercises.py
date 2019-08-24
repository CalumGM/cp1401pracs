numbers = []


def main():
    for count in range(5):
        numbers.append(input("Enter a number: "))
    print("The first number is: {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}.")






main()
