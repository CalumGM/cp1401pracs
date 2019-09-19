from prac_06.guitar import Guitar

my_guitar = Guitar("test", 1930, 1230.23)
print("{} get_age() - Expected 89 got {}".format(my_guitar.name, my_guitar.get_age()))
print("{} is_vintage() - Expected True got {}".format(my_guitar.name, my_guitar.is_vintage()))


