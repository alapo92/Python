word = "whateverermagherd"
print(word)
# [start:end:step]
print("first four letters:", word[0:4:1])

print("reverse: ", word[::-1])

new_word = word[word.index("ever"):word.index("erm")]
print()
print(new_word)
