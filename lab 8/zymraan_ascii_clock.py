# Read input from the user
time = int(input("Enter the time in a 24 hour format "))
time = str(time)
clock_type = int(input("Enter the clock type. '24' for 24 hour format '12' for twelve hour format "))
preferred_character = input("Enter your preferred character to display the time ")
# Handle user input
if clock_type == 12:
    if time >= 13:
       time = int(time) - 12
       time = str(time) + "PM"
    else: 
        if time >= 12:
            time = str(time) + "PM"
        else: 
            time = str(time) + "AM"
else:
    time = time
accetable_characters = ["a", "b", "c", "d", "e", "g", "h", "k", "m", "n", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z", @, $, &, *, =]
n = 0
for i in acceptable_characters:
    if i == preferred_character:
        n += 1
    else:
        if i == "":
            n += 1
        else:
            continue
if n != 1:
    print("Error. Character not valid.")



    
