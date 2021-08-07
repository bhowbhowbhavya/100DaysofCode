print("Welcome to the tip calculator.")
bill = float(input(("What was the bill?")))
tip = int(input("What percentage tip would you like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))
final_bill = bill + ((tip/100)*bill)
value = final_bill/people
final_amount = round(value,2)
print(f"Each person should pay: {final_amount}")


