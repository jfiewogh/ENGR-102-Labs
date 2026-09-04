# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 3
# Date: 4 September 2026
#

# Ask the user to input the quantity to be converted
conversion_number = float(input("Please enter the quantity to be converted: "))

# Convert input from pounds to newtons
pounds_to_newtons = 4.4482216153
newtons = conversion_number * pounds_to_newtons
print(f"{conversion_number:.2f} pounds force is equivalent to {newtons:.2f} newtons")

# Convert input from meters to feet
meters_to_feet = 3.280839895
feet = conversion_number * meters_to_feet
print(f"{conversion_number:.2f} meters is equivalent to {feet:.2f} feet")

# Convert input from atmospheres to kilopascals
atms_to_kilopascals = 101.325
kilopascals = conversion_number * atms_to_kilopascals
print(f"{conversion_number:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")

# Convert input from watts to BTU per hour
watts_to_btu_per_hour = 3.41214163
btu_per_hour = conversion_number * watts_to_btu_per_hour
print(f"{conversion_number:.2f} watts is equivalent to {btu_per_hour:.2f} BTU per hour")

# Convert input from liters per second to US gallons per minute
liters_per_sec_to_gallons_per_min = 0.264172052 * 60
gallons = conversion_number * liters_per_sec_to_gallons_per_min
print(f"{conversion_number:.2f} liters per second is equivalent to {gallons:.2f} US gallons per minute")
                                                                   
# Convert input from Celsius to Fahrenheit
fahrenheit = conversion_number * 9 / 5 + 32
print(f"{conversion_number:.2f} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit")