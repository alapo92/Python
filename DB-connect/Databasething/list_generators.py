import random


def generate_list(limit):
    name = []
    for x in range(limit):
        name.append(random.randrange(1, 10000))
    return name


print(generate_list(10))

#
#
#
# def floats_append(limit):
#     name = []
#     for x in range(limit):
#         name.append((random.random()))
#     return name
#
#
# def negatives_append(limit):
#     name = []
#     for x in range(limit):
#         name.append((random.uniform(-10, 10)))
#     return name


# print(integers_append(integers, 10))
# print(floats_append(floats, 10))
# print(negatives_append(negatives, 20))



