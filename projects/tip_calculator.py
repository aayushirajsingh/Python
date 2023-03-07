# Create a Tip Calculator

print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? Rs."))
tip = int(input("What percentage tip would you like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = (bill*(tip/100)) + bill
bill_per_person = total_bill/people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: Rs.{final_amount}")