import unittest

from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(11, set_membership.in_set({25, 7, 9, 0, 3, 66, 33, }))

    def test_something2(self):
        self.assertTrue(1, set_membership.in_set({1, 25, 7, 9, 0, 3, 66, 33, 11}))




if __name__ == '__main__':
    unittest.main()
