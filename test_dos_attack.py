import unittest
import time
from dos_attack import dos_attack

class TestDoSAttack(unittest.TestCase):
    def test_dos_attack(self):
        self.assertRaises(KeyboardInterrupt, dos_attack, "http://localhost:8000")

if __name__ == "__main__":
    unittest.main()
