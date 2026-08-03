from utils.validation import validate_semester
from utils.validation import validate_course

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold


# this function displays all the students in the system
def display_students():
    print(f"\n\t\t\t\t\t{Green}{Bold}======== Displaying Students ========{Reset}\n")
    try:
        choice = input(
            f"\t\t\t\t\t{White}{Bold}1️⃣   Display All Students\n\t\t\t\t\t2️⃣   Display Sorted Students\n\t\t\t\t\t3️⃣   Filter Students\n\t\t\t\t\t4️⃣   Back to Main Menu\n\n👉 Enter your choice (1-4){Reset}: "
        )
        if choice == "1":
            with open("data/students.txt", "r") as file:
                students = file.readlines()
                # this checks if there are any students in the system and displays their details
                if students == []:
                    print(f"{Red}{Bold}\n❗No students added to the system yet.{Reset}")
                    display_students()
                    return
                for student in students:
                    print(f"\n\n{Blue}{Bold}Student No: {student.split(',')[0]}{Reset}")
                    print(f"{Bold}---------------------------------------------{Reset}")
                    print(f"{Cyan}{Bold}Roll Number: {student.split(',')[1]}{Reset}")
                    print(f"{Cyan}{Bold}Name: {student.split(',')[2]}{Reset}")
                    print(f"{Cyan}{Bold}Age: {student.split(',')[3]}{Reset}")
                    print(f"{Cyan}{Bold}Semester: {student.split(',')[4]}{Reset}")
                    print(f"{Cyan}{Bold}Course: {student.split(',')[5]}{Reset}")
                display_students()
        elif choice == "2":
            print(f"\n\t\t\t\t\t{Bold}{Green}======== Sorting Students ========{Reset}")
            choice = input(
                f"\n\t\t\t\t\t{White}{Bold}1️⃣   Sort by Roll Number\n\t\t\t\t\t2️⃣   Sort by Name\n\t\t\t\t\t3️⃣   Sort by Age\n\t\t\t\t\t4️⃣   Sort by Semester\n\t\t\t\t\t5️⃣   Back\n\n👉 Enter your choice (1-5): {Reset}"
            )
            if choice == "1":
                # this sorts the students by roll number and displays their details
                with open("data/students.txt", "r") as file:
                    students = file.readlines()
                    # this checks if there are any students in the system and displays their details sorted by roll number
                    if students == []:
                        print(
                            f"{Red}{Bold}\n❗No students added to the system yet.{Reset}"
                        )
                        display_students()
                        return
                    # this sorts the students by roll number using a lambda function and displays their details
                    students.sort(key=lambda x: int(x.split(",")[1]))
                    for student in students:
                        print(f"\n\n{Blue}{Bold}Student No: {student.split(',')[0]}{Reset}")
                        print(f"{Bold}---------------------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student.split(',')[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student.split(',')[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student.split(',')[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student.split(',')[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student.split(',')[5]}{Reset}")
                    display_students()
            elif choice == "2":
                # this sorts the students by name and displays their details
                with open("data/students.txt", "r") as file:
                    students = file.readlines()
                    # this checks if there are any students in the system and displays their details sorted by name
                    if students == []:
                        print(
                            f"{Red}{Bold}\n❗No students added to the system yet.{Reset}"
                        )
                        display_students()
                        return
                    # this sorts the students by name using a lambda function and displays their details
                    students.sort(key=lambda x: x.split(",")[2].lower())
                    for student in students:
                        print(f"\n\n{Blue}{Bold}Student No: {student.split(',')[0]}{Reset}")
                        print(f"{Bold}---------------------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student.split(',')[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student.split(',')[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student.split(',')[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student.split(',')[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student.split(',')[5]}{Reset}")
                    display_students()
            elif choice == "3":
                # this sorts the students by age and displays their details
                with open("data/students.txt", "r") as file:
                    students = file.readlines()
                    # this checks if there are any students in the system and displays their details sorted by age
                    if students == []:
                        print(
                            f"{Red}{Bold}\n❗No students added to the system yet.{Reset}"
                        )
                        display_students()
                        return
                    # this sorts the students by age using a lambda function and displays their details
                    students.sort(key=lambda x: int(x.split(",")[3]))
                    for student in students:
                        print(f"\n\n{Blue}{Bold}Student No: {student.split(',')[0]}{Reset}")
                        print(f"{Bold}---------------------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student.split(',')[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student.split(',')[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student.split(',')[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student.split(',')[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student.split(',')[5]}{Reset}")
                    display_students()
            elif choice == "4":
                # this sorts the students by semester and displays their details
                with open("data/students.txt", "r") as file:
                    students = file.readlines()
                    # this checks if there are any students in the system and displays their details sorted by semester
                    if students == []:
                        print(
                            f"{Red}{Bold}\n❗No students added to the system yet.{Reset}"
                        )
                        display_students()
                        return
                    # this sorts the students by semester using a lambda function and displays their details
                    students.sort(key=lambda x: int(x.split(",")[4]))
                    for student in students:
                        print(f"\n\n{Blue}{Bold}Student No: {student.split(',')[0]}{Reset}")
                        print(f"{Bold}---------------------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student.split(',')[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student.split(',')[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student.split(',')[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student.split(',')[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student.split(',')[5]}{Reset}")
                    display_students()
            elif choice == "5":
                display_students()
            else:
                print(f"\n{Red}{Bold}❌ Invalid choice. Please try again.{Reset}")
                display_students()
        elif choice == "3":
            print(f"\n\t\t\t\t\t{Bold}{Green}======== Filtering Students ========{Reset}\n")
            # this filters the students based on user input and displays their details
            filter_choice = input(
                f"\t\t\t\t\t{White}{Bold}1️⃣   Filter by Semester\n\t\t\t\t\t2️⃣   Filter by Course\n\t\t\t\t\t3️⃣   Back\n\n👉 Enter your choice (1-3): {Reset}"
            )
            if filter_choice == "1":
                # this loops until the user enters a valid semester and then filters the students based
                # on that semester
                while True:
                    semester = input(f"\n{Bold}{White}👉 Enter the semester to filter by: {Reset}")
                    if validate_semester(semester) == True:
                        break
                    else:
                        print(
                            f"{Red}{Bold}\n❌ Invalid semester. Please enter a number between 1 and 8.{Reset}"
                        )
                with open("data/students.txt", "r") as file:
                    students = file.readlines()
                    filtered_students = [
                        student
                        for student in students
                        if student.split(",")[4].lower() == semester.lower()
                    ]
                    # this checks if there are any students in the system and displays their details filtered by semester
                    if filtered_students == []:
                        print(
                            f"{Red}{Bold}\n❗No students added to the system for semester {semester}.{Reset}"
                        )
                        display_students()
                        return
                    for student in filtered_students:
                        print(f"\n\n{Blue}{Bold}Student No: {student.split(',')[0]}{Reset}")
                        print(f"{Bold}---------------------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student.split(',')[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student.split(',')[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student.split(',')[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student.split(',')[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student.split(',')[5]}{Reset}")
                    display_students()
            elif filter_choice == "2":
                while True:
                    course = input(f"\n{Bold}{White}👉 Enter the course to filter by: {Reset}").lower()
                    if validate_course(course) == True:
                        break
                    else:
                        print(f"\n{Red}{Bold}❌ Invalid course. Please enter a valid course.{Reset}")
                with open("data/students.txt", "r") as file:
                    students = file.readlines()
                    filtered_students = [
                        student
                        for student in students
                        if student.split(",")[5].strip().lower() == course.lower()
                    ]
                    # this checks if there are any students in the system and displays their details filtered by course
                    if filtered_students == []:
                        print(
                            f"{Red}{Bold}\n❗No students added to the system for course {course}.{Reset}"
                        )
                        display_students()
                        return
                    for student in filtered_students:
                        print(f"\n\n{Blue}{Bold}Student No: {student.split(',')[0]}{Reset}")
                        print(f"{Bold}---------------------------------------------{Reset}")
                        print(f"{Cyan}{Bold}Roll Number: {student.split(',')[1]}{Reset}")
                        print(f"{Cyan}{Bold}Name: {student.split(',')[2]}{Reset}")
                        print(f"{Cyan}{Bold}Age: {student.split(',')[3]}{Reset}")
                        print(f"{Cyan}{Bold}Semester: {student.split(',')[4]}{Reset}")
                        print(f"{Cyan}{Bold}Course: {student.split(',')[5]}{Reset}")
                    display_students()
            elif filter_choice == "3":
                display_students()
            else:
                print(f"\n{Red}{Bold}❌ Invalid choice. Please try again.{Reset}")
                display_students()
        elif choice == "4":
            return
        else:
            print(f"\n{Red}{Bold}❌ Invalid choice. Please try again.{Reset}")
            display_students()
    # this handles the case where the students.txt file does not exist and displays an appropriate message
    except FileNotFoundError:
        print(
            f"{Red}{Bold}\n❗No students added to the system. The file does not exist.{Reset}"
        )
        display_students()
