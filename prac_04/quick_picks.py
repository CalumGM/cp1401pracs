import random
MIN = 1
MAX = 45
PICKS_PER_LINE = 6


def main():
    number_of_picks = int(input("How many quick picks: "))
    for i in range(number_of_picks):
        quick_picks = []
        for j in range(PICKS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_picks:
                number = random.randint(MIN, MAX)  # keeps choosing a number if that number is already in the list
            quick_picks.append(number)
        quick_picks.sort()
        print("".join("{:3}".format(number) for number in quick_picks))


main()
