#read choice of tariff
# daily use in kWh
# number of days in the billing period
#calculate the electricity bill

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which tariff? 31 or 11: "))

daily = float(input("Input daily usage in kWh: "))
days = float(input("Input number of days in the billing period: "))
if tariff == 11:
    e_bill = TARIFF_11 * daily * days
    print("Total electricity bill is " + str(e_bill))
else:
    e_bill = TARIFF_31 * daily * days
    print("Total electricity bill is " + str(e_bill))
