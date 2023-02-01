import unittest
import tree_height

class TestTreeHeight(unittest.TestCase):
    def test_positive_scenarios(self):
        self.assertEqual(3, tree_height.tree_height([4, -1, 4, 1, 1]))
        self.assertEqual(4, tree_height.tree_height([-1, 0, 4, 0, 3]))

    def test_posistive_scanrios_more_than_2_children(self):
        self.assertEqual(4, tree_height.tree_height([-1, 0, 4, 0, 3, 0, 0, 0]))
        self.assertEqual(9, tree_height.tree_height([-1, 0, 4, 0, 3, 0, 0, 0, 4, 8, 9, 10, 11, 12]))

    def test_boundary_values(self):
        self.assertEqual(0, tree_height.tree_height([]))
        self.assertEqual(1, tree_height.tree_height([-1]))
        self.assertEqual(False, tree_height.tree_height([4]))

    def test_negative_scenarios(self):
        self.assertEqual(False, tree_height.tree_height([-1, -1]))
        self.assertEqual(False, tree_height.tree_height([4, 4, 4, 7, 2, 8]))
        self.assertEqual(False, tree_height.tree_height([-1, 4, 4, 4, 7, 2, 8]))

