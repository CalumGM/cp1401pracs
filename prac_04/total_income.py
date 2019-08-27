"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_moths."""
    incomes = []
    number_of_moths = int(input("How many months?: "))

    for month in range(1, number_of_moths + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):  # enumerate function loops through element and index
        total += income
        print("Month {:2} - Income: ${:5.2f}      Total: ${:5.2f}".format(month, income, total))


main()
