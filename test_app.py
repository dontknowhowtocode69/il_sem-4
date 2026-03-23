import unittest
from app import add
class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4,5),9)
if __name__ == "__main__":
    unittest.main()