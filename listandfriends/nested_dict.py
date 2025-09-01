# nested dictionary
import datetime

student_1 = {
    "name": "John Doe",
    "sid": "26024847172",
    "gdp_points": 180,
    "scholarship": False,
    "date_born": datetime.datetime(2001, 10, 12),
}

student_2 = {
    "name": "Lily Potter",
    "sid": "22054847172",
    "gdp_points": 200,
    "scholarship": True,
    "date_born": datetime.datetime(2000, 7, 29),
}

student_3 = {
    "name": "Maddog",
    "sid": "25054847172",
    "gdp_points": 200,
    "scholarship": False,
    "date_born": datetime.datetime(2000, 2, 29),
}

students = {"student01": student_1, "student02": student_2, "student03": student_3}

print(f"{'ID':<10} {'NAME':<17} {'GPA':<3} {'SCHOLARSHIP':<12} {'DATE OF BIRTH':<10}")
print(f"{"="*55}")

for id in students:
    studentName = students[id]["name"]
    studentID = students[id]["sid"]
    studentPoints = students[id]["gdp_points"]
    studentScholarship = students[id]["scholarship"]
    studentDateOfBirth = students[id]["date_born"].strftime("%x")

    print(
        f"{id:<10} {studentName:<17} {studentPoints:<3} {studentScholarship:<12} {studentDateOfBirth:<10}"
    )
