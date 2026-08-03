from utils.validation import validate_roll
from datetime import datetime

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold

# this marks the attendance of students for a today's date
def mark_attendance():
    # check if attendance for today has already been marked
    heading = f"Attendance for {datetime.now().strftime('%Y-%m-%d')}"
    with open("data/attendance.txt", "r") as attendance_file:
        lines = attendance_file.readlines()
        if heading in "".join(lines):
            print(f"\n\t\t\t\t{Yellow}{Bold}✅ {heading} has already been marked.{Reset}")
            attendance()
            return

    # if attendance for today has not been marked, create a new entry in the attendance.txt file
    with open("data/attendance.txt", "a") as attendance_file:
        attendance_file.write("\n\n============================\n")
        attendance_file.write(f"  {heading}\n")
        attendance_file.write("============================\n\n")
        attendance_file.write("Roll No\t\tName\t\t\tStatus\n")

    # read the students.txt file and mark attendance for each student
    with open("data/students.txt", "r") as student_file:
        print(f"\n{Green}{Bold}====== {heading} ======{Reset}")
        # loop through each student and prompt the user to mark their attendance
        for line in student_file:
            student_data = line.strip().split(",")
            roll_number = student_data[1]
            name = student_data[2]
            while True:
                user_input = input(f"\n{White}{Bold}{name} ({roll_number}) [P/A]: {Reset}")
                if user_input.upper() == "P":
                    status = "Present"
                    break
                elif user_input.upper() == "A":
                    status = "Absent"
                    break
                else:
                    print(
                        f"\n{Red}{Bold}❌ Invalid input. Please enter 'P' for Present or 'A' for Absent.{Reset}"
                    )
            with open("data/attendance.txt", "a") as attendance_file:
                attendance_file.write(f"{roll_number}\t\t\t\t{name}\t\t\t{status}\n")
        print(f"\n\t\t\t\t{Yellow}{Bold}✅  Attendance marking completed for all students.{Reset}")
        attendance()


# this function displays the attendance of students for a specific date
def view_attendance_by_date():
    choice = input(f"{White}{Bold}\n👉 Enter the date (YYYY-MM-DD) to view attendance: {Reset}")
    heading = f"Attendance for {choice}"
    with open("data/attendance.txt", "r") as attendance_file:
        found = False
        for line in attendance_file:
            if heading == line.strip():
                found = True
                print(f"\n\n\t\t\t\t{White}{Bold}====== {heading} ======{Reset}\n")
                for line in attendance_file:
                    if line.strip().startswith("Attendance for"):
                        break
                    print(f"{Cyan}{Bold}{line.strip()}{Reset}")
                attendance()
        if not found:
            print(
                f"{Red}{Bold}\n❗ Either your format is incorrect or no attendance records found for {choice}.{Reset}"
            )
            attendance()


# this function calculates the attendance percentage of a student based on their roll number
def attendance_percentage():
    roll_number = input(f"{White}{Bold}\n👉 Enter the roll number of the student: {Reset}")
    if validate_roll(roll_number):
        total_classes = 0
        attended_classes = 0
        # read the attendance.txt file and calculate the attendance percentage for the given roll number
        with open("data/attendance.txt", "r") as attendance_file:
            for line in attendance_file:
                student_data = line.strip().split("\t")
                if student_data[0] == roll_number:
                    total_classes += 1
                    if "Present" in line:
                        attended_classes += 1
        # calculate the attendance percentage and display it to the user
        if total_classes == 0:
            print(f"{Red}{Bold}\n❗ No attendance records found for roll number {roll_number}.{Reset}")
            attendance()
        else:
            percentage = (attended_classes / total_classes) * 100
            print(
                f"\n{Magenta}{Bold}Attendance percentage for roll number {roll_number}: {percentage:.2f}%{Reset} "
            )
            attendance()
    else:
        print(f"{Red}{Bold}\n❌ Invalid roll number. Please enter a valid roll number.{Reset}")
        attendance()


def attendance():
    while True:
        print(f"\n\t\t\t\t\t{Green}{Bold}======== Attendance Menu ========{Reset}")
        try:
            choices = int(
                input(
                    f"\n\t\t\t\t\t{White}{Bold}1️⃣   Mark Attendance\n\t\t\t\t\t2️⃣   View Attendance by Date\n\t\t\t\t\t3️⃣   Attendance Percentage\n\t\t\t\t\t4️⃣   Back to Main Menu\n\n👉 Enter your choice (1-4): {Reset}"
                )
            )
            break
        except ValueError:
            print(f"\n{Red}{Bold}❌ Invalid choice. Please enter a valid choice (1-4).{Reset}")
            continue

    if choices == 1:
        mark_attendance()
    elif choices == 2:
        view_attendance_by_date()
    elif choices == 3:
        attendance_percentage()
    elif choices == 4:
        return 
    else:
        print(f"\n{Red}{Bold}❌ Invalid choice. Going back to the main menu.{Reset}")
