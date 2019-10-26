from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    print(MENU)
    current_taxi = None
    menu_choice = input(">>> ")
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxi's Available:")
            [print("{} - {}".format(index, taxi)) for index, taxi in enumerate(taxis)]
            taxi_choice = int(input("Chose Taxi: "))
            while taxi_choice > len(taxis) - 1:
                taxi_choice = int(input("Chose Taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_bill))
        if menu_choice == 'd':
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("How far would you like to drive: "))
                current_taxi.drive(distance)
                print("Your {} trip cost you {:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                total_bill += current_taxi.get_fare()
                print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ")
    print("Taxi's are now")
    [print("{} - {}".format(index, taxi)) for index, taxi in enumerate(taxis)]
    print("Bill to date: ${:.2f}".format(total_bill))

main()
