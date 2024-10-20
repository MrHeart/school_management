class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Course:
    def __init__(self, name, created_by):
        self.name = name
        self.created_by = created_by
        self.tutor = None
        self.students = []
        self.grades = {}

    def enroll_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, grade):
        self.grades[student] = grade

    def get_grade(self, student):
        return self.grades.get(student, None)
