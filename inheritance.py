class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

class WorkingStudent(Student):
    def __init__(self, name, school, salery, job_title):
        super().__init__(name, school)
        self.salery = salery
        self.job_title = job_title

    #

anna = Student("Anna", "Oxford")
greg = WorkingStudent.friend(anna, "Greg", 17.50, "Software Developer")

print(anna.name)
print(anna.school)

print(greg.name)
print(greg.school)
print(greg.salery)
print(greg.job_title)

##
