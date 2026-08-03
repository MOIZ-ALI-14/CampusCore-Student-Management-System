# Validation functions for the CampusCore

# this checks if the name contains only alphabets
def validate_name(name):
    name = name.replace(" ", "")  # Remove spaces from the name
    if name.isalpha():
        return True
    else:
        return False

# this checks if the roll number is a valid integer between 1 and 999
def validate_roll(roll):
    if roll.isdigit() and 1 <= int(roll) <= 999:
        return True
    else:
        return False

# this checks if the age is a valid integer between 1 and 35
def validate_age(age):
    if age.isdigit() and 0 < int(age) < 36:
        return True
    else:
        return False

# this checks if the semester is a valid integer between 1 and 8
def validate_semester(semester):
    if semester.isdigit() and 1 <= int(semester) <= 8:
        return True
    else:
        return False

# this checks if the course name contains only alphabets
def validate_course(course):
    course = course.replace(" ", "")  # Remove spaces from the course name
    if course.isalpha():
        return True
    else:
        return False
