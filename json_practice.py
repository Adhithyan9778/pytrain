import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(student["name"], student["age"])