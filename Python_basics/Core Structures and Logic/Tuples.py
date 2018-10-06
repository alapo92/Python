my_tuple = 1, 2, 3, "A", "B", "C"

print(type(my_tuple))
print()
print(my_tuple)
print()
print(my_tuple[0:3])
print()

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(A)
A = tuple(A)
print("A as tuple: ", A)
print()

(A, B, C) = 1, 2, 3
print(A, B)
print(C)
print()
(D, E, F) = "ABC"
print(D, F)
print()