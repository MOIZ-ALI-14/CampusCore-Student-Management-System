from utils.validation import validate_roll
from utils.validation import validate_semester
from utils.validation import validate_course

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold


# this function calculates the GPA of a student based on their grades and credit hours
def gpa_calculator():
    print(f"\n\t\t\t\t\t{Magenta}{Bold}======== GPA Calculator ========{Reset}")
    choice = input(
        f"{White}{Bold}\n\t\t\t\t\t1️⃣   Calculate GPA\n\t\t\t\t\t2️⃣   Calculate CGPA\n\t\t\t\t\t3️⃣   Main Menu\n\n👉 Enter your choice(1-3): {Reset}"
    )
    if choice == "1":
        grading_chart = {
            "A+": 4.00,
            "A": 3.70,
            "B+": 3.40,
            "B": 3.00,
            "B-": 2.50,
            "C+": 2.00,
            "C": 1.50,
            "D": 1.00,
            "F": 0.00,
        }

        roll_number = input(
            f"{White}{Bold}\n👉 Enter your roll number (1-999): {Reset}"
        )
        # validate the roll number using the validate_roll function from utils/validation.py
        if validate_roll(roll_number):
            student_found = False
            # open the students.txt file and read the student data
            with open("data/students.txt", "r") as file:
                # iterate through each line in the file and split the data by comma
                for line in file:
                    student_data = line.strip().split(",")
                    # check if the roll number matches the input roll number
                    if student_data[1] == roll_number:
                        student_found = True
                        print(
                            f"\n\t\t\t\t\t{Magenta}{Bold}lets calculate your GPA {student_data[2]}!"
                        )
                        print(f"\t\t\t\t\t{Bold}---------------------------------------{Reset}")

                        total_quality_points = 0
                        total_credit_hours = 0

                        # get the number of courses from the user and validate the input
                        while True:
                            try:
                                total_courses = int(
                                    input(
                                        f"\n{White}{Bold}👉 Enter number of courses (1-10): {Reset}"
                                    )
                                )
                                if total_courses <= 10 and total_courses > 0:
                                    break
                                else:
                                    print(
                                        f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of courses.\n{Reset}"
                                    )
                            except ValueError:
                                print(
                                    f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of courses.\n{Reset}"
                                )

                        # iterate through the number of courses and get the course name,
                        # credit hours, and grade from the user
                        for i in range(total_courses):
                            print(
                                f"{Magenta}{Bold}---------------------------------------{Reset}"
                            )
                            # get the course name from the user and validate the input
                            while True:
                                try:
                                    course_name = input(
                                        f"{White}{Bold} Course {i+1} name (A-Z): {Reset}"
                                    )
                                    if validate_course(course_name):
                                        break
                                    else:
                                        print(
                                            f"\n{Red}{Bold}❌ Invalid input. Please enter a valid course name.\n{Reset}"
                                        )
                                except ValueError:
                                    print(
                                        f"\n{Red}{Bold}❌ Invalid input. Please enter a valid course name.\n{Reset}"
                                    )

                            # get the credit hours from the user and validate the input
                            while True:
                                try:
                                    credit_hours = int(
                                        input(
                                            f"{White}{Bold} Credit hours (1-10): {Reset}"
                                        )
                                    )
                                    if credit_hours <= 10 and credit_hours > 0:
                                        break
                                    else:
                                        print(
                                            f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of credit hours.\n{Reset}"
                                        )
                                except ValueError:
                                    print(
                                        f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of credit hours.\n{Reset}"
                                    )

                            # get the grade from the user and validate the input
                            while True:
                                try:
                                    grade = input(
                                        f"{White}{Bold} Grade (A+, A, B+, B, B-, C+, C, D, F): {Reset}"
                                    )
                                    if grade.upper() in grading_chart:
                                        break
                                    else:
                                        print(
                                            f"\n{Red}{Bold}❌ Invalid input. Please enter a valid grade.\n{Reset}"
                                        )
                                except ValueError:
                                    print(
                                        f"\n{Red}{Bold}❌ Invalid input. Please enter a valid grade.\n{Reset}"
                                    )
                            print(
                                f"{Magenta}{Bold}---------------------------------------{Reset}"
                            )
                            # check if the grade is valid and calculate the total quality
                            # points and credit hours
                            if grade.upper() in grading_chart:
                                total_quality_points += (
                                    grading_chart[grade.upper()] * credit_hours
                                )
                                total_credit_hours += credit_hours
                        # calculate the GPA by dividing the total quality points by the total credit hours
                        if total_credit_hours != 0:
                            gpa = total_quality_points / total_credit_hours
                            print(
                                f"\n\t\t\t\t\t{Magenta}{Bold}---------------------------------------{Reset}"
                            )
                            print(f"\t\t\t\t\t\t{Bold}GPA: {gpa:.2f} for {student_data[2]}{Reset}")
                            print(
                                f"\t\t\t\t\t{Magenta}{Bold}---------------------------------------{Reset}"
                            )

            # if the student is not found, display a message
            if not student_found:
                print(
                    f"\n{Red}{Bold}❌ Student with roll number {roll_number} not found.{Reset}"
                )
                print(f"{Red}{Bold}-----------------------------------------{Reset}")
                gpa_calculator()  # recursively call the function to allow the user to try again

        else:
            print(
                f"\n{Red}{Bold}❌ Invalid roll number. Please enter a number between 1 and 999.{Reset}"
            )
            gpa_calculator()  # recursively call the function to allow the user to try again
    elif choice == "2":
        roll_number = input(
            f"\n{White}{Bold}👉 Enter your roll number (1-999): {Reset}"
        )
        # validate the roll number using the validate_roll function from utils/validation.py
        if validate_roll(roll_number):
            student_found = False
            # open the students.txt file and read the student data
            with open("data/students.txt", "r") as file:
                # iterate through each line in the file and split the data by comma
                for line in file:
                    student_data = line.strip().split(",")
                    # check if the roll number matches the input roll number
                    if student_data[1] == roll_number:
                        student_found = True
                        print(
                            f"\n\t\t\t\t\t{Magenta}{Bold} Let's calculate your CGPA {student_data[2]}!"
                        )
                        print(f"\t\t\t\t\t{Magenta}{Bold}---------------------------------------{Reset}")

                        total_quality_points = 0
                        total_credit_hours = 0

                        # get the number of semesters from the user and validate the input
                        while True:
                            try:
                                total_semesters = int(
                                    input(
                                        f"\n{White}{Bold}👉 Enter number of semesters (1-8): {Reset}"
                                    )
                                )
                                if total_semesters <= 8 and total_semesters > 0:
                                    break
                                else:
                                    print(
                                        f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of semesters.\n{Reset}"
                                    )
                            except ValueError:
                                print(
                                    f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of semesters.\n{Reset}"
                                )

                        # iterate through the number of semesters and get the GPA and credit hours from the user
                        # for that semester and calculate the total quality points and credit hours
                        for i in range(total_semesters):
                            print(
                                f"{Magenta}{Bold}---------------------------------------{Reset}"
                            )
                            # get the semester GPA from the user and validate the input
                            while True:
                                try:
                                    semester_gpa = float(
                                        input(
                                            f"{White}{Bold} Semester {i+1} GPA (0.0-4.0): {Reset}"
                                        )
                                    )
                                    if semester_gpa <= 4 and semester_gpa >= 0:
                                        break
                                    else:
                                        print(
                                            f"\n{Red}{Bold}❌ Invalid input. Please enter a valid GPA between 0 and 4.\n{Reset}"
                                        )
                                except ValueError:
                                    print(
                                        f"\n{Red}{Bold}❌ Invalid input. Please enter a valid GPA.\n{Reset}"
                                    )

                            # get the semester credit hours from the user and validate the input
                            while True:
                                try:
                                    semester_credit_hours = int(
                                        input(
                                            f"{White}{Bold} Semester {i+1} Credit hours (1-20): {Reset}"
                                        )
                                    )
                                    if (
                                        semester_credit_hours <= 20
                                        and semester_credit_hours > 0
                                    ):
                                        break
                                    else:
                                        print(
                                            f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of credit hours.\n{Reset}"
                                        )
                                except ValueError:
                                    print(
                                        f"\n{Red}{Bold}❌ Invalid input. Please enter a valid number of credit hours.{Reset}\n"
                                    )

                            print(
                                f"{Magenta}{Bold}---------------------------------------{Reset}"
                            )
                            # calculate the total quality points and credit hours
                            total_quality_points += semester_gpa * semester_credit_hours
                            total_credit_hours += semester_credit_hours
                        # calculate the CGPA by dividing the total quality points by the total credit hours
                        if total_credit_hours != 0:
                            cgpa = total_quality_points / total_credit_hours
                            print(
                                f"\n\t\t\t\t\t{Magenta}{Bold}---------------------------------------{Reset}"
                            )
                            print(f"\t\t\t\t\t\t{Bold}CGPA: {cgpa:.2f} for {student_data[2]}{Reset}")
                            print(
                                f"\t\t\t\t\t{Magenta}{Bold}---------------------------------------{Reset}"
                            )

            # if the student is not found, display a message
            if not student_found:
                print(
                    f"\n{Red}{Bold}❌ Student with roll number {roll_number} not found."
                )
                print(f"{Red}{Bold}-----------------------------------------{Reset}")
                gpa_calculator()  # recursively call the function to allow the user to try again
        else:
            print(
                f"\n{Red}{Bold}❌ Invalid roll number. Please enter a number between 1 and 999."
            )
            gpa_calculator()  # recursively call the function to allow the user to try again
    elif choice == "3":
        return
    else:
        print(f"\n{Red}{Bold}❌ Invalid choice. Enter valid choice.")
        gpa_calculator()  # recursively call the function to allow the user to try again
