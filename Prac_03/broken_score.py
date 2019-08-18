"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    score_calculation(score)


def score_calculation(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score >= 90:
        print("Excellent")
    else:
        print("Passable")


main()


