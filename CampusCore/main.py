# CampusCore
# Created by: Moiz Ali
# Date: 2026-07-23
# Description: A modern CampusCore

# importing colors from utils/colors.py to use in the menu function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold


# creating menu function to display the menu options
def menu():
    print(
        f"\n\t\t\t\t{Bold}{Blue}=========== Welcome to the CampusCore ===========\n{Reset}"
    )
    print(
        f"\t\t\t\t {Bold}{White}🎓 1. Add Student \t\t📋 2. Display Students\n{Reset}"
    )
    print(
        f"\t\t\t\t {Bold}{White}🔍 3. Search Student\t\t✏️  4. Update Student\n{Reset}"
    )
    print(f"\t\t\t\t {Bold}{White}🗑️  5. Delete Student\t\t📅 6. Attendance\n{Reset}")
    print(f"\t\t\t\t {Bold}{White}📊 7. GPA Calculator\t\t📈 8. Statistics\n{Reset}")
    print(f"\t\t\t\t\t\t {Bold}{White} 🚪 9. Exit\n{Reset}")


# importing the required functions from services folder
from services.add_student import add_student
from services.search_student import search_student
from services.display_students import display_students
from services.update_student import update_student
from services.delete_student import delete_student
from services.statistics import statistics
from services.login import login
from services.attendance import attendance
from services.GPA_calc import gpa_calculator

# running the login function to authenticate the user
login()

# running the main loop to display the menu and handle user input
while True:
    menu()
    choice = input(f"{Bold}{White}👉 Enter your choice (1-9): {Reset}")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        attendance()
    elif choice == "7":
        gpa_calculator()
    elif choice == "8":
        statistics()
    elif choice == "9":
        print(f"{Bold}{Green}\n\n\t\t\t\t\t👋 Exiting the program...🙏 Goodbye!{Reset}")
        break
    else:
        print(f"{Bold}{Red}\n❌ Invalid choice. Please try again.{Reset}")
