from prac_08.silver_service_taxi import SilverServiceTaxi

test_SStaxi = SilverServiceTaxi("test", 100, 2)
test_SStaxi.start_fare()
test_SStaxi.drive(18)
test_SStaxi.get_fare()
print("{} {}".format(test_SStaxi, test_SStaxi.get_fare()))
