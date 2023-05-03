import unittest

from tree import Tree


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(1)
        self.tree.add(10)
        self.tree.add(11)

    def test_something(self):
        self.assertEqual(self.tree.find(12), None)  # add assertion here
        self.assertEqual(self.tree.find(5).data, 5)


if __name__ == '__main__':
    unittest.main()
