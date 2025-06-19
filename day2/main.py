print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10 12 15.3 "))
people = int(input("How many people to split the bill? "))

total_bill_with_tip = bill + (bill * tip / 100)
payment_per_person = total_bill_with_tip / people
payment_rounded = round(payment_per_person, 2)

print(f"Each person has to pay ${payment_rounded}.")
