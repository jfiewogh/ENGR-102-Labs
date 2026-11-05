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
import time


def is_compatible(a: list[str], b: list[str], extras: bool) -> bool:
    """Can truffles a and b share a box?
    extras=False: the five basic rules.
    extras=True : also toffee/coconut, white/dark drizzle and round/heart."""
    if a == b:                                              # no identical truffles
        return False
    shapes, fillings, toppings = {a[1], b[1]}, {a[2], b[2]}, {a[3], b[3]}
    if shapes == {"square", "rectangle"}:
        return False
    if fillings == {"caramel", "vanilla"}:
        return False
    if toppings == {"nuts", "sprinkles"}:
        return False
    if extras:
        if shapes == {"round", "heart"}:
            return False
        if fillings == {"toffee", "coconut"}:
            return False
        if toppings == {"white chocolate drizzle", "dark chocolate drizzle"}:
            return False
    return True


def counts_feasible(dark: int, white: int, num_boxes: int, white_required: bool) -> bool:
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


def generate_boxes(seed, options, compatible, is_dark, is_white, white_ok):
    """Yield every valid 4-truffle box containing seed (random order)."""
    options = list(options)
    random.shuffle(options)

    def extend(box, options, num_dark, num_white):
        if len(box) == 4:
            if num_dark in (0, 2, 3) and num_white in white_ok:
                yield list(box)
            return
        for i, truffle in enumerate(options):
            nd = num_dark + (1 if is_dark[truffle] else 0)
            nw = num_white + (1 if is_white[truffle] else 0)
            if nd > 3 or nw > 3:
                continue
            next_options = [x for x in options[i + 1:] if x in compatible[truffle]]
            if len(next_options) < 3 - len(box):
                continue
            box.append(truffle)
            yield from extend(box, next_options, nd, nw)
            box.pop()

    yield from extend([seed], options,
                      1 if is_dark[seed] else 0, 1 if is_white[seed] else 0)


def attempt(remaining, num_boxes, compatible, is_dark, is_white, white_ok, state):
    """Randomized depth-first search; returns a list of boxes or None."""
    if not remaining:
        return []
    state["nodes"] += 1
    if state["nodes"] > state["limit"]:
        return None

    # Seed the next box with the most constrained truffle
    seed, seed_count = None, None
    for truffle in remaining:
        count = len(compatible[truffle] & remaining)
        if count < 3:
            return None
        if seed is None or count < seed_count or (count == seed_count and random.random() < 0.3):
            seed, seed_count = truffle, count

    white_required = 0 not in white_ok
    tried = 0
    for box in generate_boxes(seed, compatible[seed] & remaining, compatible, is_dark, is_white, white_ok):
        tried += 1
        if tried > 25:
            break
        new_rem = remaining - set(box)
        num_dark = sum(1 for t in new_rem if is_dark[t])
        num_white = sum(1 for t in new_rem if is_white[t])
        if not counts_feasible(num_dark, num_white, num_boxes - 1, white_required):
            continue
        rest = attempt(new_rem, num_boxes - 1, compatible, is_dark, is_white, white_ok, state)
        if rest is not None:
            return [box] + rest
        if state["nodes"] > state["limit"]:
            return None
    return None


def solve(truffles, extras, white_required, max_seconds):
    """Try to build all the boxes under one rule set. Returns the boxes or None."""
    deadline = time.time() + max_seconds
    keys = list(truffles.keys())
    num_boxes = len(keys) // 4
    is_dark = {k: truffles[k][0] == "dark" for k in keys}
    # The white-chocolate count rule belongs to the extra rules
    is_white = {k: extras and truffles[k][0] == "white" for k in keys}
    white_ok = (2, 3) if white_required else (0, 2, 3)

    # Precompute which pairs of truffles can share a box
    compatible = {k: set() for k in keys}
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if is_compatible(truffles[a], truffles[b], extras):
                compatible[a].add(b)
                compatible[b].add(a)

    if not counts_feasible(sum(is_dark.values()), sum(is_white.values()),
                           num_boxes, white_required):
        return None

    while time.time() < deadline:              # random restarts
        state = {"nodes": 0, "limit": 300}
        result = attempt(set(keys), num_boxes, compatible, is_dark, is_white, white_ok, state)
        if result is not None:
            return result
    return None


def make_boxes(truffles: dict[int, list[str]]) -> list[list[int]]:
    # Try the strictest rules first. An answer found under stricter rules also
    # satisfies every looser set, so falling back can never hurt:
    #   1. all rules, and every box has 2 or 3 white truffles
    #   2. all rules, boxes with white truffles have 2 or 3 of them
    #   3. only the five basic rules
    for extras, white_required, max_seconds in ((True, True, 5),
                                                (True, False, 5)):
        result = solve(truffles, extras, white_required, max_seconds)
        if result is not None:
            return result
    return []


if __name__ == "__main__":
    cocoa = ["dark", "milk", "white"]
    filling = ["strawberry", "vanilla", "caramel", "coconut", "toffee"]
    shape = ["round", "square", "rectangle", "heart"]
    topping = ["sprinkles", "nuts", "white chocolate drizzle", "dark chocolate drizzle", "none"]
    chocolates = {i: [random.choice(cocoa), random.choice(shape),
                      random.choice(filling), random.choice(topping)] for i in range(1, 101)}
    print(make_boxes(chocolates))