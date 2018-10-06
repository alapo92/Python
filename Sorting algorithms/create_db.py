import random
import csv
import sqlite3


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


integers = []
floats = []
mixed_negatives = []

integers_append(integers, 10000)
negatives_append(mixed_negatives, 10000)
floats_append(floats, 10000)


def create_csv(name, length):
    with open('{}.csv'.format(name), mode='w') as numbers:
        row_writer = csv.writer(numbers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row_writer.writerow(('integers', 'floats', 'mixed_negatives'))

        for i in range(length):

            row_writer.writerow([random.choice(integers), random.choice(floats), random.choice(mixed_negatives)])


create_csv('numbers_no_reps', 10000)

con = sqlite3.connect("numbers.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS numbers (id INTEGER PRIMARY KEY, integers int, floats date, mixed_negatives int);")
# use your column names here

with open('numbers_no_reps.csv', 'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['integers'], i['floats'], i['mixed_negatives']) for i in dr]

cur.executemany("INSERT INTO numbers (integers, floats, mixed_negatives) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()
