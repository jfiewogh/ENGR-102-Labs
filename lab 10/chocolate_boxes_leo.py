# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 10
# Date: 3 November 2026
#

import random

def valid_box(box, chocolates):
    # Check that no two truffles are identical
    for i in range(len(box)):
        for j in range(i + 1, len(box)):
            if chocolates[box[i]] == chocolates[box[j]]:
                return False

    caramel = False
    vanilla = False
    nuts = False
    sprinkles = False
    square = False
    rectangle = False
    toffee = False
    coconut = False
    white_drizzle = False
    dark_drizzle = False
    round_shape = False
    heart_shape = False
    dark_count = 0
    white_count = 0

    # Check the characteristics of each truffle
    for number in box:
        truffle = chocolates[number]

        if truffle[2] == "caramel":
            caramel = True

        if truffle[2] == "vanilla":
            vanilla = True

        if truffle[2] == "toffee":
            toffee = True

        if truffle[2] == "coconut":
            coconut = True

        if truffle[3] == "nuts":
            nuts = True

        if truffle[3] == "sprinkles":
            sprinkles = True

        if truffle[3] == "white chocolate drizzle":
            white_drizzle = True

        if truffle[3] == "dark chocolate drizzle":
            dark_drizzle = True

        if truffle[1] == "round":
            round_shape = True

        if truffle[1] == "heart":
            heart_shape = True

        if truffle[0] == "dark":
            dark_count += 1

        if truffle[0] == "white":
            white_count += 1

    # Check all the restrictions
    if caramel and vanilla:
        return False

    if nuts and sprinkles:
        return False

    if square and rectangle:
        return False

    if toffee and coconut:
        return False

    if white_drizzle and dark_drizzle:
        return False
    
    if round_shape and heart_shape:
        return False

    if dark_count == 1:
        return False

    if dark_count > 3:
        return False
   
    if white_count < 2 or white_count > 3:
        return False

    if truffle[1] == "square":
        square = True

    if truffle[1] == "rectangle":
        rectangle = True
        return True


def make_boxes(chocolates):
    # Check that there are groups of four
    if len(chocolates) % 4 != 0:
        return []

    # Get all the truffle numbers
    truffles = list(chocolates.keys())

    # Try different random arrangements
    for attempt in range(500):
        remaining = truffles.copy()
        random.shuffle(remaining)

        boxes = []
        possible = True

        # Continue until all truffles are used
        while len(remaining) > 0:

            found_box = False

            # Try combinations of four truffles
            for i in range(len(remaining)):
                if found_box:
                    break

                for j in range(i + 1, len(remaining)):
                    if found_box:
                        break

                    for k in range(j + 1, len(remaining)):
                        if found_box:
                            break

                        for m in range(k + 1, len(remaining)):

                            box = [
                                remaining[i],
                                remaining[j],
                                remaining[k],
                                remaining[m]
                            ]

                            # Check if the box follows all the rules
                            if valid_box(box, chocolates):

                                boxes.append(box)

                                # Remove the selected truffles
                                new_remaining = []

                                for number in remaining:
                                    if number not in box:
                                        new_remaining.append(number)

                                remaining = new_remaining
                                found_box = True
                                break

            # Start over if no valid box can be made
            if not found_box:
                possible = False
                break

        # Return the boxes if all truffles were used
        if possible:
            return boxes

    return []

cocoa = ["dark", "milk", "white"]
filling = ["strawberry", "vanilla", "caramel", "coconut", "toffee"]
shape = ["round", "square", "rectangle", "heart"]
topping = ["sprinkles", "nuts", "white chocolate drizzle", "dark chocolate drizzle", "none"]

chocolates = {i: [random.choice(cocoa), random.choice(shape), random.choice(filling), random.choice(topping)] for i in range(1, 101)}
print(make_boxes(chocolates))
