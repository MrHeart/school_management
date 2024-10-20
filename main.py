from controllers import SchoolManagementSystem

def main():
    system = SchoolManagementSystem()
    
    # Sample data for demonstration purposes
    system.add_user("student1", "password1", "student")
    system.add_user("tutor1", "password2", "tutor")
    system.add_course("Math 101", "tutor1")
    
    # Login as student
    if system.authenticate("student1", "password1"):
        print("Logged in as student1")
        system.enroll_in_course("student1", "Math 101")
        system.view_courses("student1")
    
    # Login as tutor
    if system.authenticate("tutor1", "password2"):
        print("Logged in as tutor1")
        system.assign_grade("Math 101", "student1", 95)
        system.view_grades("student1")

if __name__ == "__main__":
    main()
