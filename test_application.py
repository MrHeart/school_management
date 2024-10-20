import unittest
from controllers import SchoolManagementSystem

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.system = SchoolManagementSystem()
        self.system.add_user("admin", "adminpass", "administrator")
        self.system.add_user("user", "userpass", "non-administrator")

    def test_authentication(self):
        self.assertTrue(self.system.authenticate("admin", "adminpass"))
        self.assertFalse(self.system.authenticate("user", "wrongpassword"))

    def test_course_enrollment(self):
        self.system.authenticate("admin", "adminpass")
        self.system.add_course("Math 101", "admin")
        self.system.enroll_in_course("user", "Math 101")
        self.system.view_courses("user")

if __name__ == "__main__":
    unittest.main()
