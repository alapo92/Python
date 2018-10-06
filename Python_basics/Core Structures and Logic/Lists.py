my_list = [13, 23, 43, 54, 22]

print(my_list)

print(type(my_list))

Whatevz = ["A", "B", "C", 1, 2, 3, "wow", "such", "python", True, False]
print(Whatevz[4])
print(Whatevz[-2])

x = Whatevz[1]
print(x)

print(Whatevz[0:3])

listception = [11, 54, "A",[13, 23, 43, 54, 22], 0]

print(listception)
print(listception[3])

print(listception[3][1])


my_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_table)
print(my_table[0])
print(my_table[1])
print(my_table[2])
print(my_table[2][1])
print(my_table[1][1:])

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del L[0]
print(L)

print()

A = [5, 12, 65, 78, 23, 54]
A = A + ["BCD"]
print("A + [BCD]: ", A)
print()
A = A + list("BCD")
print("A + list(BCD): ", A)
print()
A = A + [1, 2, 3]
print("A + [1, 2, 3]: ", A)
print()
A = A + list(str(123))
print("A + list(str(123)): ", A)
print()
B = [5, 12, 65, 78, 23, 54]
print("B: ", B)
B = B + [[5, 6, 7, 8]]
print()
print("B + [[5, 6, 7, 8]]: ", B)
print()
print("B[-1]: ", B[-1])
print()
B.append([10, 11, 12, 13])
print("appended: ", B)
print()

B.insert(2, 100)
print("B.insert(2,100): ", B)
print()

C = [1, 2, 3]
C[0] = 5
print(C)
