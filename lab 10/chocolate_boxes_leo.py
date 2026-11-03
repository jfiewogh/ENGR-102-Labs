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
chocolates = {1: ["milk", "round", "toffee", "sprinkles"],
2: ["milk", "square", "coconut", "none"],
3: ["dark", "heart", "strawberry", "white chocolate drizzle"],
4: ["dark", "round", "toffee", "white chocolate drizzle"],
5: ["milk", "square", "caramel", "nuts"],
6: ["milk", "heart", "toffee", "dark chocolate drizzle"],
7: ["dark", "rectangle", "caramel", "none"],
8: ["dark", "heart", "strawberry", "white chocolate drizzle"],
9: ["dark", "heart", "coconut", "white chocolate drizzle"],
10: ["milk", "square", "coconut", "none"],
11: ["milk", "round", "vanilla", "dark chocolate drizzle"],
12: ["milk", "round", "strawberry", "nuts"],
13: ["milk", "rectangle", "caramel", "sprinkles"],
14: ["dark", "rectangle", "toffee", "none"],
15: ["dark", "heart", "toffee", "none"],
16: ["dark", "heart", "coconut", "white chocolate drizzle"],
17: ["dark", "round", "vanilla", "none"],
18: ["dark", "rectangle", "toffee", "dark chocolate drizzle"],
19: ["milk", "round", "toffee", "none"],
20: ["milk", "square", "caramel", "dark chocolate drizzle"],
21: ["milk", "square", "vanilla", "none"],
22: ["dark", "heart", "caramel", "sprinkles"],
23: ["milk", "square", "caramel", "nuts"],
24: ["milk", "round", "caramel", "dark chocolate drizzle"],
25: ["milk", "round", "coconut", "dark chocolate drizzle"],
26: ["dark", "round", "coconut", "dark chocolate drizzle"],
27: ["milk", "rectangle", "strawberry", "sprinkles"],
28: ["white", "heart", "vanilla", "none"],
29: ["dark", "heart", "strawberry", "none"],
30: ["dark", "rectangle", "caramel", "none"],
31: ["white", "round", "caramel", "none"],
32: ["milk", "heart", "vanilla", "none"],
33: ["white", "round", "strawberry", "nuts"],
34: ["milk", "round", "coconut", "none"],
35: ["dark", "rectangle", "coconut", "dark chocolate drizzle"],
36: ["milk", "round", "vanilla", "dark chocolate drizzle"],
37: ["dark", "round", "coconut", "white chocolate drizzle"],
38: ["dark", "round", "coconut", "white chocolate drizzle"],
39: ["dark", "round", "coconut", "dark chocolate drizzle"],
40: ["dark", "round", "strawberry", "dark chocolate drizzle"],
41: ["milk", "rectangle", "toffee", "none"],
42: ["milk", "round", "strawberry", "white chocolate drizzle"],
43: ["milk", "heart", "coconut", "none"],
44: ["white", "round", "strawberry", "white chocolate drizzle"],
45: ["milk", "heart", "toffee", "sprinkles"],
46: ["milk", "rectangle", "strawberry", "none"],
47: ["white", "round", "caramel", "dark chocolate drizzle"],
48: ["white", "square", "toffee", "none"],
49: ["milk", "rectangle", "toffee", "none"],
50: ["dark", "rectangle", "caramel", "none"],
51: ["milk", "square", "vanilla", "none"],
52: ["dark", "round", "toffee", "dark chocolate drizzle"],
53: ["milk", "round", "toffee", "white chocolate drizzle"],
54: ["dark", "square", "strawberry", "none"],
55: ["milk", "heart", "caramel", "dark chocolate drizzle"],
56: ["milk", "heart", "vanilla", "none"],
57: ["milk", "heart", "caramel", "none"],
58: ["milk", "heart", "coconut", "sprinkles"],
59: ["milk", "heart", "vanilla", "sprinkles"],
60: ["dark", "square", "caramel", "none"],
61: ["milk", "rectangle", "vanilla", "none"],
62: ["milk", "heart", "toffee", "none"],
63: ["milk", "heart", "vanilla", "dark chocolate drizzle"],
64: ["white", "round", "coconut", "white chocolate drizzle"],
65: ["milk", "round", "coconut", "nuts"],
66: ["milk", "round", "coconut", "white chocolate drizzle"],
67: ["dark", "heart", "coconut", "none"],
68: ["dark", "square", "toffee", "none"],
69: ["dark", "round", "strawberry", "dark chocolate drizzle"],
70: ["milk", "heart", "caramel", "none"],
71: ["milk", "square", "caramel", "sprinkles"],
72: ["milk", "rectangle", "strawberry", "sprinkles"],
73: ["dark", "heart", "strawberry", "none"],
74: ["dark", "heart", "strawberry", "none"],
75: ["dark", "square", "coconut", "none"],
76: ["dark", "heart", "caramel", "none"],
77: ["dark", "heart", "coconut", "nuts"],
78: ["white", "rectangle", "caramel", "dark chocolate drizzle"],
79: ["milk", "heart", "vanilla", "sprinkles"],
80: ["white", "heart", "strawberry", "none"],
81: ["dark", "round", "toffee", "white chocolate drizzle"],
82: ["dark", "round", "vanilla", "none"],
83: ["white", "square", "coconut", "none"],
84: ["milk", "rectangle", "caramel", "dark chocolate drizzle"],
85: ["white", "heart", "toffee", "none"],
86: ["white", "round", "caramel", "nuts"],
87: ["white", "round", "caramel", "none"],
88: ["dark", "round", "caramel", "none"],
89: ["dark", "square", "coconut", "nuts"],
90: ["milk", "heart", "vanilla", "none"],
91: ["dark", "round", "coconut", "none"],
92: ["dark", "round", "caramel", "none"],
93: ["white", "round", "toffee", "none"],
94: ["milk", "round", "vanilla", "sprinkles"],
95: ["white", "round", "strawberry", "white chocolate drizzle"],
96: ["dark", "square", "strawberry", "nuts"],
97: ["milk", "round", "vanilla", "none"],
98: ["milk", "rectangle", "caramel", "sprinkles"],
99: ["milk", "heart", "vanilla", "none"],
100: ["dark", "rectangle", "strawberry", "white chocolate drizzle"],
}

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

# print(make_boxes(chocolates))
