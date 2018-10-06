import csv
import sqlite3

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


# integers = []
# floats = []
# mixed_negatives = []#
# numbers_no_reps
