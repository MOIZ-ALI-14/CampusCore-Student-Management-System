from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold


# This is the student model class that defines the attributes and methods for a student object
class Student:
    def __init__(self, roll_number, name, age, semester, course):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.semester = semester
        self.course = course

    # This method returns a string representation of the student object
    def __str__(self):
        return f"\n{Bold}📋 Student Details:\n\n🔹 Roll Number: {self.roll_number}\n🔹 Name: {self.name}\n🔹 Age: {self.age}\n🔹 Semester: {self.semester}\n🔹 Course: {self.course}{Reset}\n"
