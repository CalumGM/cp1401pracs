from prac_08.taxi import Taxi


new_taxi = Taxi("Prius 1", 100)
print(new_taxi)
new_taxi.start_fare()
new_taxi.drive(40)
print("{}. Current fare: ${}".format(new_taxi, new_taxi.get_fare()))

