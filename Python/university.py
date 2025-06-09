# Assignment
# University system to display information about students, courses, and lecturers.
# Classes: Person(Parent), 
# Subclasses: Student, Lecturer, Staff etc

# Superclass
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}") 
        
# Subclass for Student
class Student(Person):
    def __init__(self, name, id_number, courses):
        super().__init__(name, id_number)
        self.courses = courses                      # list of courses a student offers

    def display_info(self):
        super().display_info()
        print("Enrolled courses:")
        for course in self.courses:
            print(f" - {course}")  
            
# Subclass for Lecturer
class Lecturer(Person):
    def __init__(self, name, id_number, courses_teaching, department):
        super().__init__(name, id_number)
        self.courses_teaching = courses_teaching    # list of courses a lecturer teaches
        self.department = department                # list of departments

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("Courses teaching:")
        for course in self.courses_teaching:
            print(f" - {course}")
            
# Subclass for Staff
class Staff(Person):
    def __init__(self, name, id_number, role, office):
        super().__init__(name, id_number)
        self.role = role
        self.office = office

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")
        print(f"Office: {self.office}")
        
student = Student("Abisha Baingana", "ST12345", ["BSE2206", "BSE3101", "BSE2205"])
lecturer = Lecturer("Dr. Nasser Kimbugwe", "LT87654", ["BSE2206", "Emerging Web Technologies"], "Networks")
staff = Staff("Joshua Aryampa", "ST555333", " School Registrar", "Block B, Room 303")

print("Student Info:")
student.display_info()

print("\nLecturer Info:")
lecturer.display_info()

print("\nStaff Info:")
staff.display_info()