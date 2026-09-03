class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display_detials(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student1 = student("Arun",21,"Python")
student2 = student("Rahul",22,"Django")

student1.display_detials()
print()
student2.display_detials()

