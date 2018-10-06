students = {
    "male": ["Peter", "Roman", "Wojciech", "Mitch"],
    "female": ["Jessica", "Waltraut", "Griselde", "Gesa", "Jenny"]
}

for key in students.keys():
    print(students[key])

print()

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
