class LotteryPlayer:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Anna", (10, 15, 22, 33))
player_two = LotteryPlayer("Anna", (10, 15, 22, 33))

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def getAvergae(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("I'm going to {}.".format(self.school))
        print("I'm {}.".format(self))

    @classmethod
    def go_to_school_classmethod(cls):
        print("I'm going to school.")
        print("I'm a {}.".format(cls))

    @staticmethod
    def go_to_school_static():
        print("I'm going to school.")


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(58)

print(anna.getAvergae())
anna.go_to_school()
anna.go_to_school_classmethod()
Student.go_to_school_static()
