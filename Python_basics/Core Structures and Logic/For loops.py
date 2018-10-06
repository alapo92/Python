# range(1, 11, step)  going up to but not including 11 (stops at 10)

for number in range(1, 10, 2):
    print(number)

vowels = 0
consonants = 0

print()

for letter in "Fergolicious is delicious":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
