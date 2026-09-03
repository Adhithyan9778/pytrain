students = [
    {"id": 1, "name": "Arun", "age": 21},
    {"id": 2, "name": "Rahul", "age": 22}
]

students.append({
    "id": 3,
    "name": "Adhithyan",
    "age": 22
})


for student in students:
    if student["id"] == 1:
        student["age"] = 22
        
students = [student for student in students if student["id"] != 2]

for student in students:
    print(student["id"], student["name"], student["age"])