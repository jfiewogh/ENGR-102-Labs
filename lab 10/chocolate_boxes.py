import random

chocolate_types = ["dark", "milk", "white"]
shapes = ["round", "square", "rectangle", "heart"]
fillings = ["strawberry creme", "vanilla creme", "caramel", "coconut", "toffee"]
toppings = ["sprinkles", "nuts", "white chocolate drizzle",
            "dark chocolate drizzle", "nothing"]

chocolates = {}

for i in range(1, 101):
    chocolates[i] = [
        random.choice(chocolate_types),
        random.choice(shapes),
        random.choice(fillings),
        random.choice(toppings)
    ]


def check_box(box):
    dark = 0
    fillings = []
    toppings = []
    shapes = []

    for chocolate in box:
        details = chocolates[chocolate]

        if details[0] == "dark":
            dark += 1

        fillings.append(details[2])
        toppings.append(details[3])
        shapes.append(details[1])

    if dark == 1 or dark == 4:
        return False

    if "caramel" in fillings and "vanilla creme" in fillings:
        return False

    if "nuts" in toppings and "sprinkles" in toppings:
        return False

    if "square" in shapes and "rectangle" in shapes:
        return False

    return True

def make_boxes(chocolates):
    remaining = list(chocolates.keys())
    boxes = {}

    random.shuffle(remaining)

    for i in range(1, 26):
        found = False

        for attempt in range(10000):
            box = random.sample(remaining, 4)

            if check_box(box):
                boxes[i] = [chocolates[chocolate] for chocolate in box]

                for chocolate in box:
                    remaining.remove(chocolate)

                found = True
                break

        if not found:
            return None

    return boxes


boxes = make_boxes()

while boxes == None:
    boxes = make_boxes()


print("CHOCOLATES:")
print(chocolates)

print("\nBOXES:")
for key, value in boxes.items():
    print(key, value)