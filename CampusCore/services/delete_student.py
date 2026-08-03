# this imports roll_no validation function from the utils folder
from utils.validation import validate_roll

# this imports the create backup function from the backup.py file in the services
# folder
from services.backup import create_backup

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold

# this function deletes a student from the system based on the roll number provided by the user
def delete_student():
    roll = input(f"{White}{Bold}\n👉 Enter Roll Number to search (1-999): {Reset}")
    # this checks if the roll number is valid and if it exists in the system
    if validate_roll(roll):
        with open("data/students.txt", "r") as file:
            for line in file:
                student_data = line.strip().split(",")
                if student_data[1] == roll:
                    print(f"\n{Blue}{Bold}We found student that you want to delete:{Reset}")
                    print(f"{Bold}----------------------------------------{Reset}")
                    print(f"{Cyan}{Bold}Roll Number: {student_data[1]}{Reset}")
                    print(f"{Cyan}{Bold}Name: {student_data[2]}{Reset}")
                    print(f"{Cyan}{Bold}Age: {student_data[3]}{Reset}")
                    print(f"{Cyan}{Bold}Semester: {student_data[4]}{Reset}")
                    print(f"{Cyan}{Bold}Course: {student_data[5]}{Reset}")
                    while True:
                        choice = input(
                            f"\n{White}{Bold}👉 Are you sure you want to delete this student? (yes/no): {Reset}"
                        )
                        if choice.lower() == "no":
                            print(f"\n\t\t\t\t\t\t{Yellow}{Bold}↩️  Deletion cancelled.{Reset}")
                            break
                        elif choice.lower() == "yes":
                            # this creates a backup of the students.txt file before
                            # deleting the student
                            create_backup()
                            # this reads the students.txt file, filters out the student with
                            # the specified roll number, and writes the remaining students
                            # back to the file(deletes the matching student)
                            with open("data/students.txt", "r") as file:
                                lines = file.readlines()

                            with open("data/students.txt", "w") as file:
                                for line in lines:
                                    if line.strip().split(",")[1] != roll:
                                        file.write(line)

                            print(f"\n\t\t\t\t\t{Green}{Bold}🗑️  Student deleted successfully!{Reset}")
                            break
                    return  # Return to main menu after deletion or cancellation
            print(f"{Red}{Bold}\n❗ No student found with Roll Number {roll}.{Reset}")
            delete_student()  # Prompt the user again if no student is found
    else:
        print(f"{Red}{Bold}\n❌ Invalid Roll Number. Please enter a number between 1 and 999.{Reset}")
        delete_student()  # Prompt the user again if the roll number is invalid
