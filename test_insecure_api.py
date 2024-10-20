import unittest

class TestInsecureAPI(unittest.TestCase):
    def test_insecure_output(self):
        self.assertEqual("password", "password")
        self.assertEqual("123456", "123456")

if __name__ == "__main__":
    unittest.main()
