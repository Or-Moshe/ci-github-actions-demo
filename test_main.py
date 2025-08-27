import unittest
from main import upper

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(upper('foo'), 'FOO')

if __name__ == '__main__':
    unittest.main()
