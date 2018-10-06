def about(name, age, likes):
    sentence = 'Meet {}! They are {} years old and they like {}'.format(name, age, likes)
    return sentence


print(about("Jack", 23, "Python"))
print()
print(about(age=25, name="Peter", likes="C++"))
print()


def about2(name, age, likes="Python"):
    sentence = 'Meet {}! They are {} years old and they like {}'.format(name, age, likes)
    return sentence


print(about2("Peter", 25))


def about3(name="test", age="20", likes="something"):
    sentence = 'Meet {}! They are {} years old and they like {}'.format(name, age, likes)
    return sentence


print()
print(about3())
