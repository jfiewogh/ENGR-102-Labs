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

import random

def is_compatible(first_truffle: dict[int, list[str]], second_truffle: dict[int, list[str]]) -> bool:
    # Check if equal
    if first_truffle == second_truffle:
        return False
    # Check shape
    if {first_truffle[1], second_truffle[1]} in ({"square", "rectangle"}, {"round", "heart"}):
        return False
    # Check filling
    if {first_truffle[2], second_truffle[2]} in ({"caramel", "vanilla"}, {"toffee", "coconut"}):
        return False
    # Check topping
    if {first_truffle[3], second_truffle[3]} in ({"nuts", "sprinkles"}, {"white chocolate drizzle", "dark chocolate drizzle"}): 
        return False
    return True

def dark_or_white_feasible(num_dark_or_white: int, num_boxes: int) -> bool:
    """Can num_dark_or_white truffles be spread over num_boxes boxes with 0, 2, or 3 per box?"""
    for threes in range(num_boxes + 1):
        rem = num_dark_or_white - 3 * threes
        if rem >= 0 and rem % 2 == 0 and rem // 2 + threes <= num_boxes:
            return True
    return False 

def generate_boxes(seed_truffle: int, options: set[int], compatible: dict[int, set[int]], is_dark: dict[int, bool], is_white: dict[int, bool]):
    """Yield every valid 4-truffle box containing seed (random order)."""
    options = list(options)
    random.shuffle(options)

    def extend(box, options, num_dark, num_white):
        if len(box) == 4:
            if num_dark in (0, 2, 3) and num_white in (0, 2, 3):
                yield list(box)
            return
        for i, truffle in enumerate(options):
            next_num_dark = num_dark + (1 if is_dark[truffle] else 0)
            if next_num_dark > 3:
                continue
            next_num_white = num_white + (1 if is_white[truffle] else 0)
            if next_num_white > 3:
                continue
            next_options = [x for x in options[i + 1:] if x in compatible[truffle]]
            if len(next_options) < 3 - len(box):
                continue
            box.append(truffle)
            yield from extend(box, next_options, next_num_dark, next_num_white)
            box.pop()

    yield from extend([seed_truffle], options, 1 if is_dark[seed_truffle] else 0, 1 if is_white[seed_truffle] else 0)

def attempt(remaining: set[int], num_boxes: int, compatible: dict[int, set[int]], is_dark: dict[int, bool], is_white: dict[int, bool], state: dict[str, int]):
    """Randomized depth-first search; returns list of boxes or None."""
    if not remaining:
        return []
    state["nodes"] += 1
    if state["nodes"] > state["limit"]:
        return None

    # Pick the most constrained truffle as the seed of the next box
    min_truffle, min_count = None, None
    for truffle in remaining:
        count = len(compatible[truffle] & remaining)
        if count == 0:
            return None
        if min_truffle is None or count < min_count or (count == min_count and random.random() < 0.3):
            min_truffle, min_count = truffle, count

    # tried = 0
    for box in generate_boxes(min_truffle, compatible[min_truffle] & remaining, compatible, is_dark, is_white):
        # tried += 1
        # if tried > 50:
        #     break
        new_rem = remaining - set(box)
        num_dark = sum(1 for truffle in new_rem if is_dark[truffle])
        if not dark_or_white_feasible(num_dark, num_boxes - 1):
            continue
        num_white = sum(1 for truffle in new_rem if is_white[truffle])
        if not dark_or_white_feasible(num_white, num_boxes - 1):
            continue
        rest = attempt(new_rem, num_boxes - 1, compatible, is_dark, is_white, state)
        if rest is not None:
            return [box] + rest
        if state["nodes"] > state["limit"]:
            return None
    return None

def make_boxes(truffles: dict[int, list[str]]) -> list[list[int]]:
    keys = list(truffles.keys())
    num_boxes = len(keys) // 4
    is_white = {k: truffles[k][0] == "white" for k in keys}
    is_dark = {k: truffles[k][0] == "dark" for k in keys}

    # Precompute which pairs of truffles can share a box
    compatible = {k: set() for k in keys}
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if is_compatible(truffles[a], truffles[b]):
                compatible[a].add(b)
                compatible[b].add(a)

    total_dark = sum(is_dark.values())
    if not dark_or_white_feasible(total_dark, num_boxes):
        print("No valid arrangement exists: dark chocolate count can't be split into 0/2/3 per box.")
        return None
    total_white = sum(is_white.values())
    if not dark_or_white_feasible(total_white, num_boxes):
        print("No valid arrangement exists: white chocolate count can't be split into 0/2/3 per box.")
        return None

    remaining = set(keys)

    for _ in range(5000): # random restarts
        state = {"nodes": 0, "limit": 3000}
        result = attempt(remaining, num_boxes, compatible, is_dark, is_white, state)
        if result is not None:
            return result

    print("No solution found.")
    return None

cocoa = ["dark", "milk", "white"]
filling = ["strawberry", "vanilla", "caramel", "coconut", "toffee"]
shape = ["round", "square", "rectangle", "heart"]
topping = ["sprinkles", "nuts", "white chocolate drizzle", "dark chocolate drizzle", "none"]

chocolates = {i: [random.choice(cocoa), random.choice(shape), random.choice(filling), random.choice(topping)] for i in range(1, 101)}

boxes = make_boxes(chocolates)
print("Boxes:", boxes)
