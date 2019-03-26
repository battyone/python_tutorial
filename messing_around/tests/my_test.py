import unittest


class Test_1(unittest.TestCase):

    def test_say_hello(self):
        print("Hello Tests")
        print("Hello Again.")


if __name__ == '__main__':
    unittest.main()
