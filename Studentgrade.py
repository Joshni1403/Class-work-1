class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# Creating 5 students
student1 = Student("Albin Anu", "A")
student2 = Student("Sia", "B+")
student3 = Student("John Paul", "A-")
student4 = Student("Maria Jose", "B")
student5 = Student("Kevin Mathew", "A+")

# Displaying all student details
student1.display()
student2.display()
student3.display()
student4.display()
student5.display()
