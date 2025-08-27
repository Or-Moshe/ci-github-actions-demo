import unittest
from main import to_upper

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(to_upper('foo'), 'FOO')

if __name__ == '__main__':
    unittest.main()
