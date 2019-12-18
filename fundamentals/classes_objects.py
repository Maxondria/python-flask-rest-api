class LotterPlayer:
    def __init__(self, name):
        self.numbers = (33, 45, 66, 11, 9, 89)
        self.name = name

    def total(self):
        return sum(self.numbers)


# player = LotterPlayer('Rolf')
# print(player.name)
# print(player.total())

##


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print(f'I am going to {self.school}')

    @classmethod
    def i_am_a_class_method(cls):
        print(
            f'I will instead receive the current class as {cls} instead of this object (self)')

    @staticmethod
    def i_am_static_method():
        print('Hello from static and I didn\'t need any \'self\' argument')


anna = Student('Anna', 'MIT')
anna.marks.append(56)

print(anna.marks)
print(anna.average())
anna.go_to_school()
# static method
Student.i_am_static_method()
Student.i_am_a_class_method()
