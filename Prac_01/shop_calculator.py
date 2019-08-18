# enter the number of items
# enter the price of each item
# tally up the price
# if price > 100, 10% discount

number_of_items = int(input("Enter the number of items: "))

while number_of_items < 0:
    print("Invalid Number of Items")
    number_of_items = int(input("Enter the number of items: "))

total = 0
for i in range(number_of_items):
    price = float(input("Enter the price of item " + str(i) + ": "))
    total += price
print("Total price is: " + str(total))
