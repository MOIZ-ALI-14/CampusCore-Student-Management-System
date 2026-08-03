# this imports the generate_report function from the
# services.generate_report module which is used to generate
# reports based on student data
from services.generate_report import generate_report

# this file contains functions to display the statistics and perform calculations related to student data
# also helps in generating reports based on the student data

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold


# this function calculates the total number of students in the system
def total_students():
    with open("data/students.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print(f"{Red}{Bold}\n❗No students found.{Reset}")
            return
        total = len(lines)
    return total


# this function displays the total number of students on the console
def show_total_students():
    total = total_students()
    print(f"\n{Yellow}{Bold}Total Students: {total}{Reset}")


# this function calculates the total number of unique courses in the system
def total_courses():
    set_courses = set()
    with open("data/students.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print(f"{Red}{Bold}\n❗No students found.{Reset}")
            return
        for line in lines:
            course = (
                line.strip().split(",")[5].lower().replace(" ", "")
            )  # assuming the course name is in the 6th column (index 5)
            if course != "":
                set_courses.add(course)
    total = len(set_courses)
    return total


# this function displays the total number of unique courses on the console
def show_total_courses():
    total = total_courses()
    print(f"\n{Yellow}{Bold}Total Courses: {total}{Reset}")


# this function calculates the number of students per semester in the system
def students_per_semester():
    semester_counts = {}
    with open("data/students.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print(f"{Red}{Bold}\n❗No students found.{Reset}")
            return
        for line in lines:
            semester = line.strip().split(",")[
                4
            ]  # assuming the semester is in the 5th column (index 4)
            if semester:
                if semester in semester_counts:
                    semester_counts[semester] += 1
                else:
                    semester_counts[semester] = 1
    return semester_counts


# this function displays the number of students per semester on the console
def show_students_per_semester():
    semester_counts = students_per_semester()
    print(f"\n{Yellow}{Bold}Students per Semester:{Reset}\n")
    for semester, count in sorted(semester_counts.items()):
        print(f"{White}{Bold}Semester: {semester}, Number of Students: {count}{Reset}")


# this function calculates the average age of students in the system
def average_age():
    with open("data/students.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print(f"{Red}{Bold}\n❗No students found.{Reset}")
            return
        total_age = sum(int(line.strip().split(",")[3]) for line in lines)
        average = total_age / len(lines)
    return average


# this function displays the average age of students on the console
def show_average_age():
    average = average_age()
    print(f"\n{Yellow}{Bold}Average Age of Students: {average:.2f}{Reset}")


# this function checks for duplicate names in the students data file
def duplicate_names():
    with open("data/students.txt", "r") as file:
        duplicate_names = {}
        lines = file.readlines()
        if len(lines) == 0:
            print(f"{Red}{Bold}\n❗No students found.{Reset}")
            return
        for line in lines:
            name = (
                line.strip().split(",")[2].lower()
            )  # assuming the name is in the 3rd column (index 2)
            if name in duplicate_names:
                duplicate_names[name] += 1
            else:
                duplicate_names[name] = 1
        return duplicate_names


# this function displays the duplicate names and their counts on the console
def show_duplicate_names():
    duplicate_name = duplicate_names()
    print(f"\n{Yellow}{Bold} Duplicate Names:{Reset}\n")
    found_duplicates = False
    for name, count in duplicate_name.items():
        if count > 1:
            print(f"{White}{Bold}{count} students have the name: {name}{Reset}")
            found_duplicates = True
    if not found_duplicates:
        print(f"{White}{Bold}❗ No duplicate names found.{Reset}")


# this function checks for duplicate courses in the students data file
def duplicate_courses():
    with open("data/students.txt", "r") as file:
        duplicate_courses = {}
        lines = file.readlines()
        if len(lines) == 0:
            print(f"{Red}{Bold}\n❗No students found.{Reset}")
            return
        for line in lines:
            course = (
                line.strip().split(",")[5].lower()
            )  # assuming the course is in the 6th column (index 5)
            if course in duplicate_courses:
                duplicate_courses[course] += 1
            else:
                duplicate_courses[course] = 1
        return duplicate_courses


# this function displays the duplicate courses and their counts on the console
def show_duplicate_courses():
    duplicate_course = duplicate_courses()
    print(f"\n{Yellow}{Bold} Duplicate Courses:{Reset}\n")
    duplicate_found = False
    for course, count in duplicate_course.items():
        if count > 1:
            print(
                f"{White}{Bold}{count} students are enrolled in the course: {course}{Reset}"
            )
            duplicate_found = True
    if not duplicate_found:
        print(f"{White}{Bold}❗ No duplicate courses found.{Reset}")


# this function checks for duplicate records in the students data file based on user input
def duplicate_records():
    print(f"\n\t\t\t\t\t{Green}{Bold}Duplicate Records Checking{Reset}")
    choice = input(
        f"\n\t\t\t\t\t{White}{Bold}1️⃣   Duplicate Names\n\t\t\t\t\t2️⃣   Duplicate Courses\n\t\t\t\t\t3️⃣   Back\n\n👉 Enter your choice(1-3):  {Reset}"
    )
    # check for duplicate names based on user input
    if choice == "1":
        show_duplicate_names()
    # check for duplicate courses based on user input
    elif choice == "2":
        show_duplicate_courses()
    # return to the main menu based on user input
    elif choice == "3":
        statistics()
        return
    else:
        print(f"{Red}{Bold}\n❌ Invalid choice. Please try again.{Reset}")


# this function displays the statistics menu and handles user input for different options
def statistics():
    print(f"\n\t\t\t\t\t{Green}{Bold}=========== Statistics Menu ==========={Reset}\n")
    print(f"\t\t\t\t\t{White}{Bold}1️⃣   Total Students{Reset}")
    print(f"\t\t\t\t\t{White}{Bold}2️⃣   Total Courses{Reset}")
    print(f"\t\t\t\t\t{White}{Bold}3️⃣   Students per Semester{Reset}")
    print(f"\t\t\t\t\t{White}{Bold}4️⃣   Average Age of Students{Reset}")
    print(f"\t\t\t\t\t{White}{Bold}5️⃣   Duplicate records check{Reset}")
    print(f"\t\t\t\t\t{White}{Bold}6️⃣   Generate Report{Reset}")
    print(f"\t\t\t\t\t{White}{Bold}7️⃣   Back to Main Menu{Reset}")
    choice = input(f"\n{White}{Bold}👉 Enter your choice (1-7): {Reset}")

    if choice == "1":
        show_total_students()
        statistics()
    elif choice == "2":
        show_total_courses()
        statistics()
    elif choice == "3":
        show_students_per_semester()
        statistics()
    elif choice == "4":
        show_average_age()
        statistics()
    elif choice == "5":
        duplicate_records()
        statistics()
    elif choice == "6":
        generate_report()
        print(
            f"\n\t\t\t\t{Yellow}{Bold}============================================================{Reset}\n"
        )
        print(
            f"\t\t\t\t{White}{Bold}         Report generated successfully(report.txt).{Reset}"
        )
        print(
            f"\n\t\t\t\t{Yellow}{Bold}============================================================{Reset}\n"
        )
        statistics()
    elif choice == "7":
        return
    else:
        print(f"{Red}{Bold}\n❌ Invalid choice. Please try again.{Reset}")
        statistics()
