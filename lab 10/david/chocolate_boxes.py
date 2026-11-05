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

def counts_feasible(dark: int, white: int, num_boxes: int, white_required: bool = False) -> bool:
    """Can dark and white truffles be spread over num_boxes boxes, jointly?
    Dark per box is 0, 2 or 3.
    white_required=False: white per box is 0, 2 or 3.
    white_required=True : white per box is 2 or 3 (every box needs white)."""
    if white_required:
        # Only box types: (0 dark, 2 white), (0 dark, 3 white), (2 dark, 2 white)
        if dark % 2:
            return False
        both = dark // 2                       # boxes with 2 dark + 2 white
        rest = num_boxes - both                # boxes with white only: 2 or 3 each
        if rest < 0:
            return False
        return 2 * rest <= white - 2 * both <= 3 * rest
    for threes_d in range(num_boxes + 1):                              # boxes with 3 dark
        for threes_w in range(num_boxes + 1 - threes_d):               # boxes with 3 white
            for both in range(num_boxes + 1 - threes_d - threes_w):    # boxes with 2 dark + 2 white
                rem_d = dark - 3 * threes_d - 2 * both
                rem_w = white - 3 * threes_w - 2 * both
                if rem_d < 0 or rem_w < 0 or rem_d % 2 or rem_w % 2:
                    continue
                if threes_d + threes_w + both + rem_d // 2 + rem_w // 2 <= num_boxes:
                    return True
    return False

# def counts_feasible(dark: int, white: int, num_boxes: int) -> bool:
#     """Can dark and white truffles be spread over num_boxes boxes, jointly?
#     Each box is one of (dark, white, milk): (0,0,4) (2,0,2) (3,0,1) (0,2,2) (0,3,1) (2,2,0)."""
#     for threes_dark in range(num_boxes + 1): # boxes with 3 dark
#         for threes_white in range(num_boxes + 1 - threes_dark): # boxes with 3 white
#             for both in range(num_boxes + 1 - threes_dark - threes_white): # boxes with 2 dark and 2 white
#                 rem_dark = dark - 3 * threes_dark - 2 * both
#                 rem_white = white - 3 * threes_white - 2 * both
#                 if rem_dark < 0 or rem_white < 0 or rem_dark % 2 or rem_white % 2:
#                     continue
#                 # leftover dark go 2 per box, leftover white go 2 per box
#                 boxes_used = threes_dark + threes_white + both + rem_dark // 2 + rem_white // 2
#                 if boxes_used <= num_boxes:
#                     return True
#     return False

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
            next_num_white = num_white + (1 if is_white[truffle] else 0)

            if next_num_dark > 3 or next_num_white > 3:
                continue

            next_options = [x for x in options[i + 1:] if x in compatible[truffle]]
            if len(next_options) < 3 - len(box):
                continue
            box.append(truffle)
            yield from extend(box, next_options, next_num_dark, next_num_white)
            box.pop()

    seed_dark = 1 if is_dark[seed_truffle] else 0
    seed_white = 1 if is_white[seed_truffle] else 0 
    yield from extend([seed_truffle], options, seed_dark, seed_white)

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
        if count < 3:
            return None
        if min_truffle is None or count < min_count or (count == min_count and random.random() < 0.3):
            min_truffle, min_count = truffle, count

    for box in generate_boxes(min_truffle, compatible[min_truffle] & remaining, compatible, is_dark, is_white):
        new_rem = remaining - set(box)
        num_dark = sum(1 for truffle in new_rem if is_dark[truffle])
        num_white = sum(1 for truffle in new_rem if is_white[truffle])
        
        if not counts_feasible(num_dark, num_white, num_boxes - 1):
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
    total_white = sum(is_white.values())
    if not counts_feasible(total_dark, total_white, num_boxes):
        return None

    remaining = set(keys)

    for _ in range(10000): # random restarts
        state = {"nodes": 0, "limit": 10000}
        result = attempt(remaining, num_boxes, compatible, is_dark, is_white, state)
        if result is not None:
            return result

    return None

cocoa = ["dark", "milk", "white"]
filling = ["strawberry", "vanilla", "caramel", "coconut", "toffee"]
shape = ["round", "square", "rectangle", "heart"]
topping = ["sprinkles", "nuts", "white chocolate drizzle", "dark chocolate drizzle", "none"]

for _ in range(1):
    chocolates = {i: [random.choice(cocoa), random.choice(shape), random.choice(filling), random.choice(topping)] for i in range(1, 101)}

    boxes = make_boxes(chocolates)
    print(boxes)