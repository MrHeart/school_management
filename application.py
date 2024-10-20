from controllers import SchoolManagementSystem

def run_application():
    system = SchoolManagementSystem()
    
    # Sample data for demonstration purposes
    system.add_user("admin", "adminpass", "admin")
    system.add_user("student", "studentpass", "student")
    system.add_course("Math 101", "admin")
    
    def admin_menu():
        while True:
            print("\nAdmin Actions:")
            print("1. Manage User Accounts")
            print("2. Manage Courses")
            print("3. Manage Grades")
            print("4. Generate Reports")
            print("5. Monitor System Activities")
            print("6. Update System Settings")
            print("7. Logout")
            action = input("Select an action: ")

            if action == '1':
                manage_user_accounts()
            elif action == '2':
                manage_courses()
            elif action == '3':
                manage_grades()
            elif action == '4':
                generate_reports()
            elif action == '5':
                monitor_system_activities()
            elif action == '6':
                update_system_settings()
            elif action == '7':
                print("Logging out...")
                break
            else:
                print("Invalid action. Please try again.")

    def manage_user_accounts():
        print("\nManage User Accounts")
        print("1. View User List")
        print("2. Add New User")
        print("3. Edit User Details")
        print("4. Deactivate/Delete User")
        action = input("Select an action: ")

        if action == '1':
            system.view_user_list()
        elif action == '2':
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            role = input("Enter role (student/tutor/administrator): ")
            system.add_user(username, password, role)
        elif action == '3':
            username = input("Enter username to edit: ")
            new_password = input("Enter new password: ")
            new_role = input("Enter new role (student/tutor/administrator): ")
            system.edit_user_details(username, new_password, new_role)
        elif action == '4':
            username = input("Enter username to deactivate/delete: ")
            system.deactivate_delete_user(username)
        else:
            print("Invalid action. Please try again.")

    def manage_courses():
        print("\nManage Courses")
        print("1. View Course List")
        print("2. Create New Course")
        print("3. Edit Course Details")
        print("4. Assign Tutor to Course")
        print("5. Enroll Students in Course")
        print("6. Deactivate/Delete Course")
        action = input("Select an action: ")

        if action == '1':
            system.view_course_list()
        elif action == '2':
            course_name = input("Enter new course name: ")
            created_by = system.current_user.username
            system.add_course(course_name, created_by)
        elif action == '3':
            course_name = input("Enter course name to edit: ")
            new_details = input("Enter new course details: ")
            system.edit_course_details(course_name, new_details)
        elif action == '4':
            course_name = input("Enter course name to assign tutor: ")
            tutor_name = input("Enter tutor username: ")
            system.assign_tutor_to_course(course_name, tutor_name)
        elif action == '5':
            course_name = input("Enter course name to enroll students: ")
            student_name = input("Enter student username: ")
            system.enroll_in_course(student_name, course_name)
        elif action == '6':
            course_name = input("Enter course name to deactivate/delete: ")
            system.deactivate_delete_course(course_name)
        else:
            print("Invalid action. Please try again.")

    def manage_grades():
        print("\nManage Grades")
        print("1. View Grades Overview")
        print("2. Edit Grades")
        print("3. Finalize Grades")
        print("4. Handle Grade Review Requests")
        action = input("Select an action: ")

        if action == '1':
            system.view_grades_overview()
        elif action == '2':
            student_name = input("Enter student username: ")
            course_name = input("Enter course name: ")
            new_grade = input("Enter new grade: ")
            system.edit_grades(student_name, course_name, new_grade)
        elif action == '3':
            course_name = input("Enter course name to finalize grades: ")
            system.finalize_grades(course_name)
        elif action == '4':
            review_request = input("Enter grade review request details: ")
            system.handle_grade_review_request(review_request)
        else:
            print("Invalid action. Please try again.")

    def generate_reports():
        print("\nGenerate Reports")
        print("1. Generate Student Performance Report")
        print("2. Generate Course Enrollment Report")
        print("3. Generate Financial Report")
        print("4. Export/Print Report")
        action = input("Select an action: ")

        if action == '1':
            system.generate_student_performance_report()
        elif action == '2':
            system.generate_course_enrollment_report()
        elif action == '3':
            system.generate_financial_report()
        elif action == '4':
            report_type = input("Enter report type to export/print: ")
            system.export_print_report(report_type)
        else:
            print("Invalid action. Please try again.")

    def monitor_system_activities():
        print("\nMonitor System Activities")
        print("1. View Activity Logs")
        print("2. Analyze Suspicious Activity")
        print("3. Generate Security Reports")
        action = input("Select an action: ")

        if action == '1':
            system.view_activity_logs()
        elif action == '2':
            system.analyze_suspicious_activity()
        elif action == '3':
            system.generate_security_reports()
        else:
            print("Invalid action. Please try again.")

    def update_system_settings():
        print("\nUpdate System Settings")
        print("1. Change System Configuration")
        print("2. Manage Security Settings")
        print("3. Update User Roles/Permissions")
        print("4. Backup System Data")
        action = input("Select an action: ")

        if action == '1':
            system.change_system_configuration()
        elif action == '2':
            system.manage_security_settings()
        elif action == '3':
            system.update_user_roles_permissions()
        elif action == '4':
            system.backup_system_data()
        else:
            print("Invalid action. Please try again.")
    def student_actions(sms):
        while True:
            print("\nStudent Actions: ")
            print("1. View Courses")
            print("2. View Grades")
            print("3. Communicate with Tutor")
            print("4. Update Profile")
            print("5. Logout")
            action = input("Select an action: ").strip()

            if action == "1":
                print("\nView Courses: ")
                sms.view_courses(system.current_user.username)
                course_name = input("Enter course name to view materials: ").strip()
                sms.view_course_materials(course_name)
                download = input("Do you want to download materials? (yes/no): ").strip().lower()
                if download == "yes":
                    sms.download_course_materials(course_name)
                
                if input("Check for assignments? (yes/no): ").strip().lower() == "yes":
                    sms.view_assignment_details(course_name)
                    if input("Submit assignment? (yes/no): ").strip().lower() == "yes":
                        assignment = input("Enter assignment details: ").strip()
                        sms.submit_assignment(course_name, assignment)
                        print("Assignment submitted successfully.")
                    else:
                        print("No assignments available.")
            
            elif action == "2":
                print("\nView Grades: ")
                course_name = input("Enter course name to view grades: ").strip()
                sms.view_grades(course_name)
                if input("Request grade review? (yes/no): ").strip().lower() == "yes":
                    sms.request_grade_review(course_name)
            
            elif action == "3":
                print("\nCommunicate with Tutor: ")
                tutor_name = input("Enter tutor name: ").strip()
                message = input("Enter your message: ").strip()
                sms.communicate_with_tutor(tutor_name, message)
                sms.receive_reply()
            
            elif action == "4":
                print("\nUpdate Profile: ")
                print("a. View Profile Information")
                print("b. Update Profile Details")
                profile_action = input("Select an action: ").strip().lower()

                if profile_action == "a":
                    print(f"Profile Information: {sms.current_user.profile}")
                elif profile_action == "b":
                    profile_updates = {}
                    while True:
                        field = input("Enter field to update (or 'done' to finish): ").strip()
                        if field == "done":
                            break
                        value = input(f"Enter new value for {field}: ").strip()
                        profile_updates[field] = value
                    sms.update_profile(profile_updates)
                else:
                    print("Invalid action.")
            
            elif action == "5":
                print("Logging out...")
                sms.current_user = None
                break
            
            else:
                print("Invalid action.")

    
    while True:
        print("\nLogin:")
        username = input("Username: ")
        password = input("Password: ")

        if system.authenticate(username, password):
                if system.current_user.role == "admin":
                    print("Authenticated as Administrator.")
                    admin_menu()
                elif system.current_user.role == "student":
                    print("Authenticated as a Student.")
                    student_actions(system)
                else:
                    print("Invalid role for the user.")
        else:
                print("Authentication failed. Please try again.")

if __name__ == "__main__":
    run_application()
