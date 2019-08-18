#read price per kWh in cents
# daily use in kWh
# number of days in the billing period
#calculate the electricity bill

price = float(input("Input price per kWh in cents: "))
daily = float(input("Input daily usage in kWh: "))
days = float(input("Input number of days in the billing period: "))

e_bill = price * daily * days
print("Total electricity bill is " + str(e_bill))
