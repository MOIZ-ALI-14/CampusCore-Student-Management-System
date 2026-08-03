# this imports the validation functions from the utils.validation module
from utils.validation import validate_roll
from utils.validation import validate_name

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold


# this function searches for a student in the system based on the roll number or name provided by the user
def search_student():
    print(f"\n\t\t\t\t\t{Bold}{Green}======== Searching Students ========{Reset}")
    # this prompts the user to choose whether to search by roll number or name
    choice = input(
        f"\n\t\t\t\t\t{Bold}{White}Search by:\n\n\t\t\t\t\t1️⃣   Roll Number\n\t\t\t\t\t2️⃣   Name\n\t\t\t\t\t3️⃣   Back to Main Menu\n\n👉 Enter your choice (1-3): {Reset}"
    )
    if choice == "1":
        roll = input(f"\n{Bold}{White}👉 Enter Roll Number to search (1-999): {Reset}")
        if validate_roll(roll):
            with open("data/students.txt", "r") as file:
                for line in file:
                    student_data = line.strip().split(",")
                    if student_data[1] == roll:
                        print(f"\n{Bold}{Blue}Student found:{Reset}")
                        print(f"{Bold}---------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student_data[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student_data[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student_data[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student_data[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student_data[5]}{Reset}")
                        search_student()
                        return
            print(f"{Red}{Bold}\n❗ Student not found with roll number {roll}.{Reset}")
            search_student()
        else:
            print(f"{Red}{Bold}\n❌ Invalid roll number. Please enter a number between 1 and 999.{Reset}")
            search_student()  # Call the function again for valid input
    # this checks if the user wants to search by name and validates the input
    elif choice == "2":
        name = input(f"\n{Bold}{White}👉 Enter Name to search: {Reset}")
        if validate_name(name):
            with open("data/students.txt", "r") as file:
                # this will search for the student by name and display their details if found, otherwise it will inform the user that the student was not found
                # and shows all the students with the same name if there are multiple entries
                found = False
                for line in file:
                    student_data = line.strip().split(",")
                    if student_data[2].lower().replace(" ", "") == name.lower().replace(" ", ""):
                        print(f"\n{Bold}{Blue}Student found:{Reset}")
                        print(f"{Bold}---------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student_data[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student_data[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student_data[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student_data[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student_data[5]}{Reset}")
                        found = True
                        search_student()  # Call the function again for valid input
                if not found:
                    print(f"{Red}{Bold}\n❗ Student not found with the name {name}.{Reset}")
                    search_student()  # Call the function again for valid input
        else:
            print(f"{Red}{Bold}\n❌ Invalid name. Please enter a valid name.{Reset}")
            search_student()  # Call the function again for valid input
    elif choice == "3":
        return  # Return to main menu
    else:
        print(f"{Red}{Bold}\n❌ Invalid choice. Please try again.{Reset}")
        search_student()  # Call the function again for valid input
