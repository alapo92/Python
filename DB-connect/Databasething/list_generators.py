import random


def integers_append(name, limit):
    for x in range(1, limit):
        name.append((random.randrange(1, 10000)))
    return name


def floats_append(name, limit):
    for x in range(1, limit):
        name.append((random.random()))
    return name


def negatives_append(name, limit):
    for x in range(1, limit):
        name.append((random.uniform(-10, 10)))
    return name


# print(integers_append(integers, 10))
# print(floats_append(floats, 10))
# print(negatives_append(negatives, 20))


