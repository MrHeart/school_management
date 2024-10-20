import unittest
import hashlib
from secure_api import hash_value

class TestSecureAPI(unittest.TestCase):
    def test_hash_value(self):
        self.assertEqual(hash_value("password"), hashlib.sha256("password".encode()).hexdigest())

if __name__ == "__main__":
    unittest.main()
