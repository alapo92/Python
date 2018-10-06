import random
import csv
import list_generators

integers = []
floats = []
mixed_negatives = []

list_generators.integers_append(integers, 10000)
list_generators.negatives_append(mixed_negatives, 10000)
list_generators.floats_append(floats, 10000)


def create_csv(name, length):
    with open('{}.csv'.format(name), mode='w') as numbers:
        row_writer = csv.writer(numbers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row_writer.writerow(('integers', 'floats', 'mixed_negatives'))

        for i in range(length):

            row_writer.writerow([random.choice(integers), random.choice(floats), random.choice(mixed_negatives)])


create_csv('numbers_no_reps', 10000)
