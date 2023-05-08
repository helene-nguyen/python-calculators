print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? \n$"))

percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill?"))

total_bill_tip = total_bill * (percent_tip/100) + total_bill

total_for_each = total_bill_tip / people

# total_rounded = round(total_for_each, 2)
total_rounded = "{:.2f}".format(total_for_each)

print(f"The amount for each people is ${total_rounded}")