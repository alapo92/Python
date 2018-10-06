a = [1, 2, 3]

print(a)


def f1():
    # if a variable is declared within a function, it can only be seen by that function
    a[0] = 3
    print(a)


def f2():
    a = 50    # local
    print(a)


f1()
f2()
print(a)
