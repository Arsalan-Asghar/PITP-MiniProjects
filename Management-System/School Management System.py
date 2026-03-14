# Week 4 - Mini Project 1 - School Management System:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Grade: {self.grade}")

people = []

def school_management():
    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            student_id = input("Enter student ID: ")
            grade = input("Enter grade: ")
            people.append(Student(name, age, student_id, grade))
        elif choice == "2":
            for person in people:
                person.display_info()
        elif choice == "3":
            print("Exiting program...")
            break

school_management()