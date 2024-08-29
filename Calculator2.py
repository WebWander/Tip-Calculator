print("Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? "))
percent_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_person = int(input("How many people to split the bill? "))

total_tip = percent_tip / 100 * total_bill
final_bill = (total_bill + total_tip) / num_person



print(f"Each person should pay: ${final_bill:.2f}")