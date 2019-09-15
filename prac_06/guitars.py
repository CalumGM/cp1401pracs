from prac_06.guitar import Guitar

print("My Guitars")

guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print("{} ({}) : ${:,.2f} added".format(new_guitar.name, new_guitar.year, new_guitar.cost))
    name = input("Name: ")

print("These are my guitars")
guitar_list = [str(guitar) for guitar in guitars]
print(guitar_list)
for i, guitar in enumerate(guitars):
    print("Guitar {}: {} ({}), worth ${:,.2f}, vintage: {}".format(i + 1, guitar.name, guitar.year, guitar.cost, guitar.__is_vintage__()))
