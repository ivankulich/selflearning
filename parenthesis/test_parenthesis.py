import unittest
import parenthesis

class Parenthesis(unittest.TestCase):

    def test_functional_parenthesis(self):
        self.assertEqual(parenthesis.parenthesis('([](){([])})'), 'Success')
        self.assertEqual(parenthesis.parenthesis('()[]}'), 5)
        self.assertEqual(parenthesis.parenthesis('{{[()]]'), 7)
        self.assertEqual(parenthesis.parenthesis('[]([]'), 3)
        self.assertEqual(parenthesis.parenthesis('{{{[][][]'), 3)
        self.assertEqual(parenthesis.parenthesis('sdfdfsdsdf'), 'Success')
        self.assertEqual(parenthesis.parenthesis('sdfdfsdsdf('), 11)

    def test_incorrect_input_parenthesis(self):
        self.assertRaises(TypeError, parenthesis.parenthesis, -2)
