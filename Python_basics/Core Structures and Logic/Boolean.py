import random

B = True
C = False
print(2 > 3)

if True:
    print("it worked !")
print()
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

print("num1:", num1)
print("num2:", num2)
if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bugger than num1")
else:
    print("numbers are equal")
print()
print("print Not True:", not True)
print()
if num1 > 10 and num2 > 10:
    print("both numbers are greater than 10!")
else:
    print("At least one of the numbers is smaller than 10")

print()

if num1 > 10 or num2 > 10:
    print("at least one number is greater than ten")

