# this imports the student class from the models folder
from models.student import Student

# this imports the validation functions from the utils folder
from utils.validation import (
    validate_name,
    validate_roll,
    validate_age,
    validate_semester,
    validate_course,
)

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold

# this function adds a new student to the system after validating the input data
def add_student():
    # roll number validation loop to ensure the roll number is unique and valid
    while True:
        roll = input(f"\n{Bold}{White}🆔 Enter Roll Number (1-999): {Reset}")
        # this checks if the roll number is valid and if it already exists in the system
        if validate_roll(roll) == True:
            with open("data/students.txt", "r") as file:
                for line in file:
                    student_data = line.strip().split(",")
                    if student_data[1] == roll:
                        print(f"\n{Red}{Bold}⚠️  Student with this roll number already exists.{Reset}")
                        add_student()
                        return
                break
        else:
            print(f"\n{Red}{Bold}❌ Invalid roll number. Please enter a valid roll number.{Reset}")
    # name validation loop to ensure the name is valid
    while True:
        name = input(f"\n{Bold}{White}👤 Enter Name (A-Z): {Reset}")
        if validate_name(name) == True:
            break
        else:
            print(f"\n{Red}{Bold}❌ Invalid name. Please enter a valid name.{Reset}")
    # age validation loop to ensure the age is valid
    while True:
        age = input(f"\n{Bold}{White}🎂 Enter Age (0-35): {Reset}")
        if validate_age(age) == True:
            break
        else:
            print(f"\n{Red}{Bold}❌ Invalid age. Please enter a valid age.{Reset}")
    # semester validation loop to ensure the semester is valid
    while True:
        semester = input(f"\n{Bold}{White}📚 Enter Semester (1-8): {Reset}")
        if validate_semester(semester) == True:
            break
        else:
            print(f"\n{Red}{Bold}❌ Invalid semester. Please enter a valid semester.{Reset}")
    # course validation loop to ensure the course is valid
    while True:
        course = input(f"\n{Bold}{White}📖 Enter Course (A-Z): {Reset}")
        if validate_course(course) == True:
            break
        else:
            print(f"\n{Red}{Bold}❌ Invalid course. Please enter a valid course.{Reset}")

    # this creates a new student object using the validated input data
    new_student = Student(roll, name, age, semester, course)

    print(f"\n\t\t\t\t\t{Green}{Bold} ✅ Student added successfully!{Reset}")
    print(new_student)
    # this writes the new student data to the students.txt file
    with open("data/students.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            file_id = 1
        else:
            last_line = lines[-1]
            last_id = int(last_line.split("==")[0].strip())
            file_id = last_id + 1
    with open("data/students.txt", "a") as file:
        file.write(f"{file_id} == ,{roll},{name},{age},{semester},{course}\n")
