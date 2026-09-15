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
import math
payment = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = (f"{payment-cost:.2f}")
print("You received $",change, " in change. That is...", sep="")
quarters = int(float(change)//0.25)


if(quarters != 0):
    if(quarters > 1):
        print(quarters, "quarters", sep=" ")
        remaining = (f"{float(change)-quarters*0.25:.2f}")
    else:
        print(quarters, "quarter", sep=" ")
        remaining = (f"{float(change) - quarters*0.25:.2f}")
else:
    remaining = float(change)
remaining = float(remaining)

if(remaining >= 0.20):
    dimes = 2
    print("2 dimes")
    remaining2 = float((f"{remaining - dimes*.10:.2f}"))
    if(remaining2 >= 0.05):
        nickels = remaining2//0.05
        print(int(nickels))
        remaining3 = float((f"{remaining2 - nickels*0.05:.2f}"))
        pennies = remaining3//0.01
        if(pennies > 0):
            if(pennies > 1):
                print(int(pennies), "pennies", sep = " ")
            else:
                print(int(pennies), "penny", sep = " ")
        else:
            print()
    else:
        pennies = int(f"{remaining2/0.01:.0f}")
        if(pennies > 0):
            if(pennies > 1):
                print(int(pennies), "pennies", sep = " ")
            else:
                print(int(pennies), "penny", sep = " ")
        else:
            print()

elif(remaining >= 0.10):
    dimes = 1
    print("1 dime")
    remaining2 = float((f"{remaining - dimes*.10:.2f}"))
    if(remaining2 >= 0.05):
        nickels = remaining2//0.05
        print(int(nickels), "nickel", sep=" ")
        remaining3 = remaining2 - nickels*0.05
        pennies = remaining3//0.01
        if(pennies > 0):
            if(pennies > 1):
                print(int(pennies), "pennies", sep = " ")
            else:
                print(int(pennies), "penny", sep = " ")
        else:
            print()
    else:
        pennies = remaining2//0.01
        if(pennies > 0):
            if(pennies > 1):
                print(int(pennies), "pennies", sep = " ")
            else:
                print(int(pennies), "penny", sep = " ")


else:
    if(remaining >= 0.05):
        nickels = remaining//0.05
        print(int(nickels), "nickel", sep=" ")
        remaining3 = remaining - nickels*0.05
        pennies = remaining3//0.01
        if(pennies > 0):
            if(pennies > 1):
                print(int(pennies), "pennies", sep = " ")
            else:
                print(int(pennies), "penny", sep = " ")
        else:
            print()
    else:

        pennies = remaining//0.01
        if(pennies > 0):
            if(pennies > 1):
                print(int(pennies), "pennies", sep = " ")
            else:
                print(int(pennies), "penny", sep = " ")
        else:
            print()
            #change is made