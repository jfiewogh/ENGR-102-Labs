# Read input from the user
time_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ":"]
x = 0
time = input("Enter the time in a 24 hour format ")
time_parts = time.split(":")
hours, minutes = str(time_parts[0]), str(time_parts[1])
while x != 1:
    time_parts = time.split(":")
    hours, minutes = str(time_parts[0]), str(time_parts[1])

    for i in time:
        if i not in time_list:
            x = 0
        else:
            continue
    if not(int(hours) >= 0 and int(hours) < 24 and int(minutes) >= 0 and int(minutes) < 60):
        x = 0
    else:
        x = 1
    if x != 1:
        time = input("Error. Not a valid time. Try again ")
    else:
        break
clock_type = int(input("Enter the clock type. '24' for 24 hour format '12' for twelve hour format "))
preferred_character = input("Enter your preferred character to display the time ")
# Handle user input
if clock_type == 12:
    if int(hours) >= 13:
       time = str(int(hours) - 12) + ":" + str(minutes)
       time = str(time) + "PM"
    else: 
        if int(hours) >= 12:
            time = str(time) + "PM"
        elif int(hours) == 0:
            hours = int(hours) + 12
            time = f"{hours}:{minutes}" + "AM"

        else: 
            time = str(time) + "AM"
else:
    time = time

accetable_characters = ["a", "b", "c", "d", "e", "g", "h", "k", "m", "n", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z", "@", "$", "&", "*", "="]
if not(preferred_character in accetable_characters or preferred_character == ''):
    print("Error. Character not valid.")
    input("Try again. Enter another preferred character ")



print(time)
print(preferred_character)

    
