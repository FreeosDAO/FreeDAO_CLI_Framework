import unittest

import src.configs.config as conf



class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("Test case Hello")
        self.assertEqual(True, False)


if __name__ == '__main__':
    print("Hello World", conf.x)
    unittest.main()

