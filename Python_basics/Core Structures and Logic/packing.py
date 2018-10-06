numbers1 = [1, 2, 3, 4, 5]
print()
print(numbers1)
print()
print(*numbers1)
print()
print("abc")
print()
print(*"abc")


def add(x, y):
    return x + y


print(add(10, 10))
print()


def add2(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


print(add2(1, 2, 3, 4, 5))
print()
print(add2(10, 15, 20, 30))
print()


def about(name, age, likes):
    sentence = "Meet {}, they are {} years old and they like {}".format(name, age, likes)
    return sentence


dictionary = {"name": "Peter", "age": 25, "likes": "Python"}
# one star for normal arguments, two stars for keyword arguments
print(about(**dictionary))
print()


def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


foo(sammie="Female", peter="male")

