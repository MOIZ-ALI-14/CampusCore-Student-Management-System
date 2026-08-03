# importing colors from utils/colors.py to use in the login function
from utils.colors import Green, Red, Yellow, Blue, Cyan, Magenta, Reset, White, Bold


# A simple login system for the CampusCore
def login():
    while True:
        username = input(f"\n\n\t\t\t\t\t\t{Bold}👤 Enter your username: {Reset}")
        password = input(f"\n\t\t\t\t\t\t{Bold}🔐 Enter your password: {Reset}")
        print(
            f"\n\t\t\t\t{Yellow}---------------------------------------------------------{Reset}"
        )
        if username == "Moiz" and password == "Mirza1234":
            print(f"{Green}{Bold}\t\t\t\t\t\t   ✅ Login successful!{Reset}")
            print(
                f"\t\t\t\t{Yellow}---------------------------------------------------------\n\n{Reset}"
            )
            break
        elif username != "Moiz" and password == "Mirza1234":
            print(
                f"\t\t\t\t\t{Red}{Bold} ❌ Invalid username. Please try again.{Reset}"
            )
            print(
                f"\t\t\t\t{Yellow}---------------------------------------------------------{Reset}"
            )
        elif username == "Moiz" and password != "Mirza1234":
            print(
                f"\t\t\t\t\t{Red}{Bold} ❌ Invalid password. Please try again.{Reset}"
            )
            print(
                f"\t\t\t\t{Yellow}---------------------------------------------------------{Reset}"
            )
        else:
            print(
                f"\t\t\t\t{Red}{Bold}   ❌ Invalid username and password. Please try again.{Reset}"
            )
            print(
                f"\t\t\t\t{Yellow}---------------------------------------------------------{Reset}"
            )
