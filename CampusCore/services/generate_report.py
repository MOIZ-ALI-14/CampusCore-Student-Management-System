from datetime import datetime


def generate_report():
    # local imports to avoid circular import issues 
    # without it python will throw an ImportError
    from services.statistics import (
        total_students,
        total_courses,
        students_per_semester,
        average_age,
        duplicate_names,
        duplicate_courses,
    )

    # Generate the report and save it to report.txt file
    with open("data/report.txt", "w") as file:
        file.write("============================================================\n")
        file.write("                   CampusCore Report\n")
        file.write("============================================================\n\n\n")
        file.write(
            f"             Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )
        file.write("------------------------------------------------------------\n")
        file.write("                     General Statistics\n")
        file.write("------------------------------------------------------------\n\n")
        file.write(f"Total Students: {total_students()}\n")
        file.write(f"Total Courses: {total_courses()}\n")
        file.write(f"Average Age of Students: {average_age():.2f}\n\n\n")
        file.write("------------------------------------------------------------\n")
        file.write("                     Students per Semester\n")
        file.write("------------------------------------------------------------\n\n")
        for name, count in sorted(students_per_semester().items()):
            file.write(f"semester: {name}, number of students: {count}\n")
        file.write("\n\n------------------------------------------------------------\n")
        file.write("                     Duplicate Names\n")
        file.write("------------------------------------------------------------\n\n")
        for name, count in duplicate_names().items():
            if count > 1:
                file.write(f"Duplicate Name: {name} - Students: {count}\n")
        file.write("\n\n------------------------------------------------------------\n")
        file.write("                     Duplicate Courses\n")
        file.write("------------------------------------------------------------\n\n")
        for course, count in duplicate_courses().items():
            if count > 1:
                file.write(f"Duplicate Course: {course} - Students: {count}\n")
        file.write("\n\n------------------------------------------------------------\n")
        file.write("                    End of Report\n")
        file.write("============================================================\n")
