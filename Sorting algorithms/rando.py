

def calculate(amount, period):
    if period == "A":
        result = int(amount) / 12
    if period == "M":
        result = int(amount) * 12
    else:
        print("Wrong input type, A - for annual, M - for monthly")

    return print(result)


income = input("Income: ").strip()
am = input("Annual/Monthly: ").strip().capitalize()

calculate(income, am)
