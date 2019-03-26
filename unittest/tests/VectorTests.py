import unittest

from Vector import Vector


class TestVector(unittest.TestCase):
    def test_creation(self):
        v = Vector(1, 2)


if __name__ == '__main__':
    unittest.main()
