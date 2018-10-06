

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def averg(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def now_to_school(cls): # pass the class instead of object
        print("I'm going to school")
        print("I'm a {}".format(cls))


anna = Student("Anna", "Oxford")
rolf = Student("Rolf", "Harvard")

print(anna.now_to_school())
print(rolf.now_to_school())

###


class Student1:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average1(self):
        return sum(self.marks) / len(self.marks)

    def go_to_schoolz(self):
        return "I'm going to school"
    # may be Static because parameter self is not being used


anna = Student1("Anna", "Oxford")
rolf = Student1("Rolf", "Harvard")

print(anna.go_to_schoolz())
print(rolf.go_to_schoolz())

###


class Student2:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        return "I'm going to school"


anna = Student2("Anna", "Oxford")
rolf = Student2("Rolf", "Harvard")

print(anna.go_to_school())
print(rolf.go_to_school())

###


class Student3:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def friend(self, friend_name):
        return Student3(friend_name, self.school)


anna = Student3("Anna", "Oxford")

friend = anna.friend("Greg")
print(friend.name)
print(friend.school)
