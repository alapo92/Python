students = {}
# {ITEM=Key:value, Key:value...}
students = {"Alice": 28, "Bob": 27, "Claire": 18, "Peter": 26, "Sammie": 27}
print(students["Alice"])
students["Fred"] = 25
print()
print(students["Fred"])
print()
del students["Fred"]
print()
# print(students["Fred"]) will return an error
print(students.keys())
print()
a = list(students.keys())
print(a[0])
print()
print(students.values())
# a dict doesnt have an order - no indices, work with keys
print()
print(students.items())
print()

# dictionary with values as a list
students2 = {"Alice": ["ID0001", 26, "A"],
             "Bob": ["ID0002", 27, "B"],
             "Claire": ["ID0003", 21, "C"],
             "Peter": ["ID0004", 26, "A"],
             "Sammie": ["ID0005", 27, "A"]
             }

print("Claire's stats: ", students2["Claire"])
print()
print("Bob's ID: ", students2["Bob"][0])
print("Bob's ID and age: ", students2["Bob"][0:2])
print()

# dictionary with values as another dictionary
studdict = {"Alice": {"ID": "ID001", "age": 26, "grade": "A"},
            "Bob": {"ID": "ID002", "age": 27, "grade": "B"},
            "Claire": {"ID": "ID003", "age": 21, "grade": "C"},
            "Peter": {"ID": "ID004", "age": 26, "grade": "A"},
            "Sammie": {"ID": "ID005", "age": 27, "grade": "A"}
            }

print("Peter's age: ", studdict["Peter"]["age"])
print()
print("Claire's id and grade: ", studdict["Claire"]["ID"], studdict["Claire"]["grade"])
