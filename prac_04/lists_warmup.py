'''
numbers = [3, 1, 4, 1, 5, 9, 2]

What values do the following expressions have?
Without running the code, write down your answers to these questions (on paper, or in your Python file as a comment)
then use Python to see if you were correct.

numbers[0]
3
numbers[-1]
2
numbers[3]
1
numbers[:-1]
[3, 1, 4, 1, 5, 9, 2]
numbers[3:4]
[1, 5] # [1]
5 in numbers
True
7 in numbers
False
"3" in numbers
False
numbers + [6, 5, 3]
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
'''
numbers = [3, 1, 4, 1, 5, 9, 2]


def main():
    numbers[0] = "ten"
    print(numbers)
    numbers[-1] = 1
    print(numbers)
    print(numbers[2:])
    print(9 in numbers)


main()
