even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print("even numbers: ", even_numbers)
print()
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
print("odd numbers: ", odd_numbers)
print()

words = ["the", "big", "fat", "drag", "queen", "ate", "miz", "cracker"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
print()
