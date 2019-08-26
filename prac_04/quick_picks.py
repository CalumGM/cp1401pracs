import random


def main():
    number_of_picks = int(input("How many quick picks: "))
    for i in range(number_of_picks):
        quick_picks = [random.randint(1, 45) for i in range(6)]
        quick_picks.sort()
        print(quick_picks)


main()
