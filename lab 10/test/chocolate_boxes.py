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

import math
import random
import time
from functools import lru_cache


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


# How many white chocolate truffles may a box hold?  (Dark is always 0, 2 or 3.)
#   "every" : 2 or 3 in every box
#   "r1"    : 0, 2 or 3            (like dark; also used when white is ignored)
#   "upto3" : 0, 1, 2 or 3
WHITE_OK = {"every": (2, 3), "r1": (0, 2, 3), "upto3": (0, 1, 2, 3)}


@lru_cache(maxsize=None)
def counts_feasible(dark: int, white: int, num_boxes: int, mode: str) -> bool:
    """Can dark and white truffles be spread over num_boxes boxes, jointly?
    A box holds 4 truffles, so dark + white <= 4 in every box."""
    if mode == "every":
        # box types: (0 dark, 2-3 white) or (2 dark, 2 white)
        if dark % 2:
            return False
        both = dark // 2
        rest = num_boxes - both
        if rest < 0:
            return False
        return 2 * rest <= white - 2 * both <= 3 * rest
    if mode == "upto3":
        # a box with 2 dark holds up to 2 white, 3 dark up to 1, 0 dark up to 3
        for twos in range(num_boxes + 1):
            rem = dark - 2 * twos
            if rem < 0 or rem % 3:
                continue
            threes = rem // 3
            if twos + threes > num_boxes:
                continue
            if white <= 3 * (num_boxes - twos - threes) + 2 * twos + threes:
                return True
        return False
    for threes_d in range(num_boxes + 1):                              # "r1"
        for threes_w in range(num_boxes + 1 - threes_d):
            for both in range(num_boxes + 1 - threes_d - threes_w):
                rem_d = dark - 3 * threes_d - 2 * both
                rem_w = white - 3 * threes_w - 2 * both
                if rem_d < 0 or rem_w < 0 or rem_d % 2 or rem_w % 2:
                    continue
                if threes_d + threes_w + both + rem_d // 2 + rem_w // 2 <= num_boxes:
                    return True
    return False


def generate_boxes(seed, options, compatible, is_dark, is_white, white_ok, degree, order):
    """Yield every valid 4-truffle box containing seed.
    order: "random" shuffles the candidates; "hard" tries the candidates with
    the fewest remaining partners first; "easy" tries the most flexible first."""
    options = list(options)
    random.shuffle(options)
    if order == "hard":
        options.sort(key=lambda t: degree[t])
    elif order == "easy":
        options.sort(key=lambda t: -degree[t])

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

    # Dead-end checks, and pick the most constrained truffle as the next seed
    seed, degree = None, {}
    for truffle in remaining:
        partners = compatible[truffle] & remaining
        count = degree[truffle] = len(partners)
        if count < 3:                                      # needs 3 box-mates
            return None
        if state["need_white_partner"] and is_white[truffle] and not (partners & state["white"]):
            return None                                    # needs another white one
        if is_dark[truffle] and not (partners & state["dark"]):
            return None                                    # needs another dark one
        if seed is None or count < degree[seed] or (count == degree[seed] and random.random() < 0.3):
            seed = truffle

    tried = 0
    for box in generate_boxes(seed, compatible[seed] & remaining, compatible,
                              is_dark, is_white, white_ok, degree, state["order"]):
        tried += 1
        if tried > state["cap"]:
            break
        new_rem = remaining - set(box)
        num_dark = sum(1 for t in new_rem if is_dark[t])
        num_white = sum(1 for t in new_rem if is_white[t])
        if not counts_feasible(num_dark, num_white, num_boxes - 1, state["mode"]):
            continue
        rest = attempt(new_rem, num_boxes - 1, compatible, is_dark, is_white, white_ok, state)
        if rest is not None:
            return [box] + rest
        if state["nodes"] > state["limit"]:
            return None
    return None


def anneal(keys, bad, is_dark, is_white, white_ok, seconds, temp=0.25):
    """Local search: start from a random arrangement and swap truffles between
    boxes, mostly in boxes that currently break a rule, until no rule is broken.
    Returns a list of boxes, or None if time runs out."""
    n = len(keys)
    num_boxes = n // 4
    dk = [1 if is_dark[k] else 0 for k in keys]
    wh = [1 if is_white[k] else 0 for k in keys]
    dark_pen = [0 if c in (0, 2, 3) else 1 for c in range(5)]
    white_pen = [0 if c in white_ok else 1 for c in range(5)]
    slots = list(range(n))
    random.shuffle(slots)

    def box_cost(b):
        if b >= num_boxes:                   # leftover truffles (when n % 4 != 0)
            return 0
        a, c, d, e = slots[4 * b: 4 * b + 4]
        pairs = bad[a][c] + bad[a][d] + bad[a][e] + bad[c][d] + bad[c][e] + bad[d][e]
        return (pairs + dark_pen[dk[a] + dk[c] + dk[d] + dk[e]]
                + white_pen[wh[a] + wh[c] + wh[d] + wh[e]])

    costs = [box_cost(b) for b in range(num_boxes)]
    total = sum(costs)
    deadline = time.time() + seconds
    steps = 0
    while total > 0:
        steps += 1
        if steps % 1024 == 0 and time.time() > deadline:
            return None
        if random.random() < 0.7:            # focus on a box that is currently broken
            broken = [b for b in range(num_boxes) if costs[b] > 0]
            i = 4 * random.choice(broken) + random.randrange(4)
        else:
            i = random.randrange(n)
        j = random.randrange(n)
        bi, bj = i >> 2, j >> 2
        if bi == bj:
            continue
        slots[i], slots[j] = slots[j], slots[i]
        ci = box_cost(bi)
        cj = box_cost(bj)
        old = (costs[bi] if bi < num_boxes else 0) + (costs[bj] if bj < num_boxes else 0)
        delta = ci + cj - old
        if delta <= 0 or random.random() < math.exp(-delta / temp):
            if bi < num_boxes:
                costs[bi] = ci
            if bj < num_boxes:
                costs[bj] = cj
            total += delta
        else:
            slots[i], slots[j] = slots[j], slots[i]
    return [[keys[slots[4 * b + k]] for k in range(4)] for b in range(num_boxes)]


def solve(truffles, extras, white_mode, max_seconds, dark_rule=True):
    """Try to build all the boxes under one rule set. Returns the boxes or None.
    white_mode: "every", "r1", "upto3", or None (white chocolate not restricted).
    dark_rule : True = a box has 0, 2 or 3 dark truffles; False = dark not restricted."""
    deadline = time.time() + max_seconds
    keys = list(truffles.keys())
    num_boxes = len(keys) // 4
    is_dark = {k: dark_rule and truffles[k][0] == "dark" for k in keys}
    is_white = {k: white_mode is not None and truffles[k][0] == "white" for k in keys}
    mode = white_mode or "r1"                  # with no white truffles tracked, "r1" = dark only
    white_ok = WHITE_OK[mode]

    # Precompute which pairs of truffles can share a box
    compatible = {k: set() for k in keys}
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if is_compatible(truffles[a], truffles[b], extras):
                compatible[a].add(b)
                compatible[b].add(a)

    # Quick impossibility check on the dark / white counts
    if not counts_feasible(sum(is_dark.values()), sum(is_white.values()), num_boxes, mode):
        return None

    # bad[i][j] = 1 when truffles i and j may not share a box
    bad = [[0 if keys[j] in compatible[keys[i]] else 1 for j in range(len(keys))]
           for i in range(len(keys))]

    dark_set = {k for k in keys if is_dark[k]}
    white_set = {k for k in keys if is_white[k]}
    while time.time() < deadline:
        # Round 1: local search (swap truffles between boxes)
        result = anneal(keys, bad, is_dark, is_white, white_ok,
                        min(0.7, max(0.0, deadline - time.time())))
        if result is not None:
            return result
        # Round 2: build the boxes one at a time (random restarts, mixed styles)
        round_end = min(deadline, time.time() + 0.3)
        while time.time() < round_end:
            state = {"nodes": 0, "dark": dark_set, "white": white_set, "mode": mode,
                     "need_white_partner": mode in ("every", "r1"),
                     "limit": random.choice([100, 300, 1500]),
                     "cap": random.choice([5, 25]),
                     "order": random.choice(["hard", "hard", "random", "easy"])}
            result = attempt(set(keys), num_boxes, compatible, is_dark, is_white, white_ok, state)
            if result is not None:
                return result
    return None


def make_boxes(truffles: dict[int, list[str]]) -> list[list[int]]:
    # Try the strictest reading of the rules first. An answer found under a
    # stricter rule set also satisfies every looser one, so falling back never hurts.
    # In every tier the three extra pair rules apply and a box with white
    # chocolate truffles has 2 or 3 of them. The tiers differ in:
    #   - whether EVERY box needs white truffles (2 or 3), or only boxes that have any
    #   - whether the dark rule (0, 2 or 3 dark per box) still applies
    for white_mode, dark_rule, max_seconds in (("every", True, 1.0),
                                               ("r1", True, 4),
                                               ("every", False, 1.0),
                                               ("r1", False, 4)):
        result = solve(truffles, True, white_mode, max_seconds, dark_rule)
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