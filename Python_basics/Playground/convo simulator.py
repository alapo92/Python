from random import choice

import random


questions = ['Are we alone?', 'How do we survive as a species?', 'Why are people so egocentric?']

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?").strip().lower()
else:
    print("alright")
