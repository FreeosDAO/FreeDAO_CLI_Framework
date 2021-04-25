import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_uppercase(self):
        assert "loud noises".upper() == "LOUD NOISES"

    def test_reversed(self):
        assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


if __name__ == '__main__':
    unittest.main()
