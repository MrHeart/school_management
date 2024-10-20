from models import User, Course

class SchoolManagementSystem:
    def __init__(self):
        self.users = {}
        self.courses = {}
        self.current_user = None

    def add_user(self, username, password, role):
        if username in self.users:
            print(f"User {username} already exists.")
        else:
            self.users[username] = User(username, password, role)
            print(f"User {username} added as {role}.")

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            return True
        return False

    def view_user_list(self):
        for username, user in self.users.items():
            print(f"Username: {username}, Role: {user.role}")

    def edit_user_details(self, username, new_password, new_role):
        user = self.users.get(username)
        if user:
            user.password = new_password
            user.role = new_role
            print(f"User {username} details updated.")
        else:
            print(f"User {username} not found.")

    def deactivate_delete_user(self, username):
        if username in self.users:
            del self.users[username]
            print(f"User {username} deactivated/deleted.")
        else:
            print(f"User {username} not found.")

    def add_course(self, name, created_by):
        if name in self.courses:
            print(f"Course {name} already exists.")
        else:
            self.courses[name] = Course(name, created_by)
            print(f"Course {name} created by {created_by}.")

    def view_course_list(self):
        for name, course in self.courses.items():
            print(f"Course: {name}, Created by: {course.created_by}, Tutor: {course.tutor}")

    def edit_course_details(self, name, new_details):
        course = self.courses.get(name)
        if course:
            course.details = new_details
            print(f"Course {name} details updated.")
        else:
            print(f"Course {name} not found.")

    def assign_tutor_to_course(self, course_name, tutor_name):
        course = self.courses.get(course_name)
        tutor = self.users.get(tutor_name)
        if course and tutor and tutor.role == 'tutor':
            course.tutor = tutor_name
            print(f"Tutor {tutor_name} assigned to course {course_name}.")
        else:
            print(f"Error assigning tutor {tutor_name} to course {course_name}.")

    def enroll_in_course(self, student_name, course_name):
        course = self.courses.get(course_name)
        student = self.users.get(student_name)
        if course and student and student.role == 'student':
            course.students.append(student_name)
            print(f"Student {student_name} enrolled in course {course_name}.")
        else:
            print(f"Error enrolling student {student_name} in course {course_name}.")

    def deactivate_delete_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]
            print(f"Course {course_name} deactivated/deleted.")
        else:
            print(f"Course {course_name} not found.")

    def view_grades_overview(self):
        for course_name, course in self.courses.items():
            print(f"Course: {course_name}, Grades: {course.grades}")

    def edit_grades(self, student_name, course_name, new_grade):
        course = self.courses.get(course_name)
        if course and student_name in course.students:
            course.grades[student_name] = new_grade
            print(f"Grade for {student_name} in course {course_name} updated to {new_grade}.")
        else:
            print(f"Error updating grade for {student_name} in course {course_name}.")

    def finalize_grades(self, course_name):
        course = self.courses.get(course_name)
        if course:
            course.finalized = True
            print(f"Grades for course {course_name} finalized.")
        else:
            print(f"Course {course_name} not found.")

    def handle_grade_review_request(self, review_request):
        print(f"Handling grade review request: {review_request}")

    def generate_student_performance_report(self):
        print("Generating student performance report...")

    def generate_course_enrollment_report(self):
        print("Generating course enrollment report...")

    def generate_financial_report(self):
        print("Generating financial report...")

    def export_print_report(self, report_type):
        print(f"Exporting/Printing report: {report_type}")

    def view_activity_logs(self):
        print("Viewing activity logs...")

    def analyze_suspicious_activity(self):
        print("Analyzing suspicious activity...")

    def generate_security_reports(self):
        print("Generating security reports...")

    def change_system_configuration(self):
        print("Changing system configuration...")

    def manage_security_settings(self):
        print("Managing security settings...")

    def update_user_roles_permissions(self):
        print("Updating user roles/permissions...")

    def backup_system_data(self):
        print("Backing up system data...")       

    def view_courses(self, username):
        user_courses = [course.name for course in self.courses.values() if username in course.students]
        print(f"Courses for {username}: {user_courses}")

    def assign_grade(self, course_name, student, grade):
        course = self.courses.get(course_name)
        if course and self.current_user.username == course.tutor:
            course.assign_grade(student, grade)

    def view_grades(self, username):
        student_courses = [course for course in self.courses.values() if username in course.students]
        for course in student_courses:
            grade = course.get_grade(username)
            print(f"Course: {course.name}, Grade: {grade}")
