class Student():
    def __init__(self, name, roll_no, age, sex, class_1):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.sex = sex
        self.class_1 = class_1


s1 = Student(input("Name is:"))
print(s1.name)
