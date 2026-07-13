# Jose Rodriguez
# 7/13/2026
# Module 8.2 - JSON Practice


# Description:
# Loads a JSON file, displays students,
# adds a new student, saves the updated JSON file.

import json


def print_students(student_list):
    """Print each student in the required format."""

    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


def main():

    # Load JSON file
    with open("Student.json", "r") as file:
        students = json.load(file)

    print("\nORIGINAL STUDENT LIST\n")
    print_students(students)

    # Add your information
    new_student = {
        "F_Name": "Jose",
        "L_Name": "Rodriguez",
        "Student_ID": 99999,
        "Email": "jrodriguez@gmail.com"
    }

    students.append(new_student)

    print("\nUPDATED STUDENT LIST\n")
    print_students(students)

    # Save JSON file
    with open("Student.json", "w") as file:
        json.dump(students, file, indent=4)

    print("\nThe Student.json file has been updated.")


if __name__ == "__main__":
    main()