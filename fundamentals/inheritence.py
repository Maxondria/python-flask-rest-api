class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)


class WorkingStudent(Student):
    def __init__(self, school, name, *args):
        super().__init__(name, school)
        self.salary = args


maxon = WorkingStudent('Oxford', 'Maxon', 20.00)
# print(maxon.salary)

maxon_friend = WorkingStudent.friend(maxon, "Timothy", 45.0)

print(maxon_friend.school)
print(maxon_friend.salary)
