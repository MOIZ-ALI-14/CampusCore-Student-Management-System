# This function creates a backup of the students.txt file by reading its contents
# and writing them to a new file called students_backup.txt.
def create_backup():
    with open("data/students.txt","r") as file:
        data = file.read()
    with open("data/students_backup.txt","w") as backup:
        backup.write("============================================================\n")
        backup.write("                   Students Backup\n")
        backup.write("============================================================\n\n")
        backup.write("This is a backup of the students.txt file.\n")
        backup.write(data)