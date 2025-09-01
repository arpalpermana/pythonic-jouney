# basic exercise with dictionary
import datetime
import os

students_data = {}

while True:
    os.system("clear")

    student_template = {
        "id": "id",
        "name": "name",
        "points": 0,
        "dob": datetime.datetime(1000, 1, 11),
    }

    print(f"{'Welcome!':^20}")
    print(f"{'Student Data Center':^20}")
    print("-" * 20)
    new_student = dict.fromkeys(student_template.keys())

    new_student["id"] = input("Enter student ID \t\t: ")
    new_student["name"] = input("Enter student name \t\t: ")
    new_student["points"] = float(input("Enter student points \t\t: "))
    year_born = int(input("Enter student year born (YYYY)  : "))
    month_born = int(input("Enter student month born (1-12) : "))
    date_born = int(input("Enter student date born (1-31)  : "))
    new_student["dob"] = datetime.datetime(year_born, month_born, date_born)

    students_data.update({new_student["id"]: new_student})

    print(f"\n\n{'ID':<10} {'NAME':<17} {'GPA':<5} {'DATE OF BIRTH':<10}")
    for id in students_data:
        studentName = students_data[id]["name"]
        studentPoints = students_data[id]["points"]
        studentDateOfBirth = students_data[id]["dob"].strftime("%x")

        print(f"{id:<10} {studentName:<17} {studentPoints:<5} {studentDateOfBirth:<10}")

    print("\n")
    is_finish = input("Are you finish? (y/n) : ")
    if is_finish == "y":
        break

print("Thanks for your works!")
