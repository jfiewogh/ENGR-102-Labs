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

from random import choice
import math

def check_box(box: list[int], truffles) -> bool:
    dark = 0
    box_fillings = []
    box_toppings = []
    box_shapes = []

    for key in box:
        details = truffles[key]
        if details[0] == "dark":
            dark += 1
        box_fillings.append(details[2])
        box_toppings.append(details[3])
        box_shapes.append(details[1])

    if dark == 1 or dark == 4:
        return False
    if "toffee" in box_fillings and "coconut" in box_fillings:
        return False
    if "caramel" in box_fillings and "vanilla creme" in box_fillings:
        return False
    if "nuts" in box_toppings and "sprinkles" in box_toppings:
        return False
    if "square" in box_shapes and "rectangle" in box_shapes:
        return False
    if "white chocolate drizzle" in box_toppings and "dark chocolate drizzle" in box_toppings:
        return False

    return True

def has_repeating_truffle(box, truffles):
        for i in range(len(box)):
            for j in range(i + 1, len(box)):
                if truffles[box[i]] == truffles[box[j]]:
                    # print(truffles[box[i]], truffles[box[j]])
                    return False
        return True

def make_boxes(truffles: dict[int, list[str]]) -> list[list[int]]:
    # each box has 4 truffles
    # each box contains a nice mix of truffles with no two truffles exactly the same
    # My friends that like caramel don't like vanilla creme, so make sure no box contains both fillings. 
    # My friends that like nuts don't like sprinkles, so make sure no box contains both toppings. 
    # My boxes are designed to fit either rectangles or squares, but not both so make sure no box contains both shapes. 
    # I have some friends that prefer truffles made from dark chocolate, so make sure boxes with dark chocolate truffles contain at least two, but no more than three, dark chocolate truffles.

    def get_random_truffle():
        truffle = choice(possible_keys)
        possible_keys.remove(truffle)
        return truffle

    while True:
        boxes = [] 
        possible_keys = list(truffles.keys())

        num_errors = 0

        while True:
            box = [get_random_truffle() for _ in range(4)]

            if not has_repeating_truffle(box, truffles) and check_box(box, truffles):
                boxes.append(box)
                num_errors = 0
            else:
                for key in box:
                    possible_keys.append(key)
                num_errors += 1

            print(len(boxes), possible_keys, num_errors)

            if len(boxes) == 25 or num_errors >= math.factorial(len(possible_keys)) / (math.factorial(len(possible_keys) - 4) * math.factorial(4)):
                num_errors += 1
                break
            
        if len(boxes) == 25:
            break

    return boxes
    # return [<type of chocolate>, <shape>, <filling>, <topping>].

cocoa = ["dark", "milk", "white"]
filling = ["strawberry", "vanilla", "caramel", "coconut", "toffee"]
shape = ["round", "square", "rectangle", "heart"]
topping = ["sprinkles", "nuts", "white chocolate drizzle", "dark chocolate drizzle", "none"]

chocolates = {i: [choice(cocoa), choice(shape), choice(filling), choice(topping)] for i in range(1, 101)}

boxes = make_boxes(chocolates)
print("Boxes:", boxes)
