# # ask user for input
# # name = input("what is your name?: ")
#
# # print(name)
#
# a = "live slow"
# b = 1
#
# # concat
# print(a + ' ' + str(b))
# print("{} -{}".format(a, b))
# print("{1} -{0}".format(a, b))

#
# # Create output text
# name = input("what is your name? : ")
# species = input("what is the name of your species? : ")
# planet = input("What planet do you come from? : ")
# string = "Your name is {} and you are a {}. You come from {}"
# output = string.format(name, species, planet)

# print(output)

print("hello".count("l"))
text = "whatever"
print(text.count("What"))

print(text.upper())

print("istitle ", text.istitle())
print("isalpha", text.isalpha())
print("isupper", text.isupper())
text.capitalize()
print(text)

print()

x = "Little Bits and Gazorpazorpfield"
index = x.index("Bits")
print(x)
print("Index for Bits: ", index)
find = x.find("Gazorpazorpfield")
print("Find gazorpazorpfield: ", find)

print()

y = "0000Intergalatic TV0000000000"
print(y)
print("Strip 0: ", y.strip("0"))
print("Rstrip 0: ", y.rstrip("0"))

print()

word = input("What is your word? (add some spaces at the end of the word): ").strip()
print(word)
print(len(word))

