"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    grade = score_calculation(score)
    print(grade)


def score_calculation(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score < 50:
        return "Bad"
    elif score >= 90:
        return "Excellent"
    else:
        return "Passable"


main()


