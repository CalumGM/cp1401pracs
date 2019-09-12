from prac_06.guitar import Guitar

print("My Guitars")

guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print("{} ({}) : ${:,.2f} added".format(name, year, cost))
    name = input("Name: ")

print("These are my guitars")
guitar_list = [str(guitar) for guitar in guitars]
for i in guitar_list:
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
