def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77


# print(methodception(add_two_numbers))
print(methodception(lambda: 35 + 77))  # lambda functions always in one line (function that doesnt need naming)

# useful when working with data

my_list = [13, 56, 77, 484]
# filter python built in method allows u to keep only some values | takes a function and an iterable
print(list(filter(lambda x: x != 13, my_list)))


# same as
def not_thirteen(x):
    return x != 13


print(list(filter(not_thirteen, my_list)))

print((lambda x: x * 3)(5))
# is equal to


def f(x):
    return x * 3


print(f(5))
