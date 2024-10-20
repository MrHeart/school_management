import unittest
from brute_force import brute_force_attack

class TestBruteForce(unittest.TestCase):
    def test_brute_force_attack(self):
        passwords = ["1234", "password", "adminpass", "qwerty"]
        self.assertTrue(brute_force_attack("admin", passwords))
        self.assertFalse(brute_force_attack("admin", ["1234", "password", "qwerty"]))

if __name__ == "__main__":
    unittest.main()
