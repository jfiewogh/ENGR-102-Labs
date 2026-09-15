# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 4
# Date: 15 September 2026

# Prompt the user for the amount paid and change.
payment = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

# Calculate and print the change
change = payment - cost
print(f"You received ${change:.2f} in change. That is...")

# Determine and print amount of quarters
quarters = int(f"{change * 100:.0f}") // 25
if quarters != 0:
    if quarters == 1:
        print(f"{quarters} quarter")
    else:
        print(f"{quarters} quarters")
# Subtract the value of quarters from the change
change = float(f"{change - quarters * 0.25:.2f}")

# Determine and print amount of dimes
dimes = int(f"{change * 100:.0f}") // 10
if dimes != 0:
    if dimes == 1:
        print(f"{dimes} dime")
    else:
        print(f"{dimes} dimes")
# Subtract the value of dimes from the change
change = float(f"{change - dimes * 0.1:.2f}")

# Determine and print amount of nickels
nickels = int(f"{change * 100:.0f}") // 5
if nickels != 0:
    if nickels == 1:
        print(f"{nickels} nickel")
    else:
        print(f"{nickels} nickels")
# Subtract the value of nickels from the change
change = float(f"{change - nickels * 0.05:.2f}")

# Determine and print amount of pennies
pennies = int(f"{change * 100:.0f}")
if pennies != 0:
    if pennies == 1:
        print(f"{pennies} penny")
    else:
        print(f"{pennies} pennies")