import random


def main():
    quick_picks = []
    number_of_picks = int(input("How many quick picks: "))
    for i in range(number_of_picks):
        quick_picks = [random.randint(1, 45) for i in number_of_picks]
        quick_picks.sort()
    print(quick_picks)


main()
