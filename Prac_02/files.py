out_file = open("name.txt", 'w')
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", 'r')
name = in_file.readline()
print(name)

numbers = open("Numbers.txt", 'r')
number_1 = int(numbers.readline())
number_2 = int(numbers.readline())
print(number_1 + number_2)
numbers.close()

numbers = open("Numbers.txt", 'r')
total = 0
for line in numbers:
    number = int(line.strip())
    total += number
print(total)
numbers.close()
