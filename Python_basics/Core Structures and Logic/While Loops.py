i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

print()

L = []
while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)
print("Sorry list is full")
print(L)