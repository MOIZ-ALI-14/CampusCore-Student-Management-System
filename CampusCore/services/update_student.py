# this imports the validation functions from the utils.validation module
from utils.validation import (
    validate_name,
    validate_roll,
    validate_age,
    validate_semester,
    validate_course,
)

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold

# this imports the create backup function from the backup.py file in the services
# folder
from services.backup import create_backup


# this function updates a student's information in the system based on the roll number provided by the user
def update_student():
    roll = input(f"\n{White}{Bold}👉 Enter Roll Number to search (1-999): {Reset}")
    if validate_roll(roll):
        with open("data/students.txt", "r") as file:
            # this reads the students.txt file and searches for the student with the specified roll number
            for line in file:
                student_data = line.strip().split(",")
                if student_data[1] == roll:
                    print(
                        f"\n{Blue}{Bold}We found student that you want to update:{Reset}"
                    )
                    print(f"{Bold}----------------------------------------{Reset}")
                    print(f"{Cyan}{Bold}Roll Number: {student_data[1]}{Reset}")
                    print(f"{Cyan}{Bold}Name: {student_data[2]}{Reset}")
                    print(f"{Cyan}{Bold}Age: {student_data[3]}{Reset}")
                    print(f"{Cyan}{Bold}Semester: {student_data[4]}{Reset}")
                    print(f"{Cyan}{Bold}Course: {student_data[5]}{Reset}")

                    print(
                        f"\n\t\t\t\t\t{Green}{Bold}Let's Update Roll No {roll}{Reset}\n"
                    )
                    # same roll number would be given even after updation
                    student_data[1] = roll
                    # this loop validates the new name for the student
                    while True:
                        new_name = input(
                            f"\n{White}{Bold}👉 Enter New Name (A-Z): {Reset}"
                        )
                        if validate_name(new_name):
                            student_data[2] = new_name
                            break
                        else:
                            print(
                                f"\n{Red}{Bold}❌ Invalid Name. Please enter a name containing only letters (A-Z).{Reset}"
                            )
                    # this loop validates the new age for the student
                    while True:
                        new_age = input(
                            f"\n{White}{Bold}👉 Enter New Age (0-35): {Reset}"
                        )
                        if validate_age(new_age):
                            student_data[3] = new_age
                            break
                        else:
                            print(
                                f"\n{Red}{Bold}❌ Invalid Age. Please enter an age between 0 and 35.{Reset}"
                            )
                    # this loop validates the new semester for the student
                    while True:
                        new_semester = input(
                            f"\n{White}{Bold}👉 Enter New Semester (1-8): {Reset}"
                        )
                        if validate_semester(new_semester):
                            student_data[4] = new_semester
                            break
                        else:
                            print(
                                f"\n{Red}{Bold}❌ Invalid Semester. Please enter a semester between 1 and 8.{Reset}"
                            )
                    # this loop validates the new course for the student
                    while True:
                        new_course = input(
                            f"\n{White}{Bold}👉 Enter New Course (A-Z): {Reset}"
                        )
                        if validate_course(new_course):
                            student_data[5] = new_course
                            break
                        else:
                            print(
                                f"\n{Red}{Bold}❌ Invalid Course. Please enter a course containing only letters (A-Z).{Reset}"
                            )

                    # this creates a backup of the students.txt file before
                    # updating the student
                    create_backup()
                    with open("data/students.txt", "r") as file:
                        lines = file.readlines()

                    with open("data/students.txt", "w") as file:
                        # this writes the updated student data back to the students.txt file, replacing the old data for the student with the specified roll number
                        for line in lines:
                            if line.strip().split(",")[1] == roll:
                                file.write(",".join(student_data) + "\n")
                            else:
                                file.write(line)

                        print(
                            f"\n\t\t\t\t\t{Green}{Bold}✅ Student updated successfully!{Reset}"
                        )
                    return
            print(f"{Red}{Bold}\n❗ No student found with Roll Number {roll}.{Reset}")
            update_student()  # recursively call the function to allow the user to try again
    else:
        print(
            f"{Red}{Bold}\n❌ Invalid Roll Number. Please enter a number between 1 and 999.{Reset}"
        )
        update_student()  # recursively call the function to allow the user to try again
