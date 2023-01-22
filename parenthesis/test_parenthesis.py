import unittest
import parenthesis
import random
import re

class Parenthesis(unittest.TestCase):

    def test_parenthesis_functional(self):
        self.assertEqual(parenthesis.parenthesis('([](){([])})'), 'Success')
        self.assertEqual(parenthesis.parenthesis('()[]}'), 5)
        self.assertEqual(parenthesis.parenthesis('{{[()]]'), 7)
        self.assertEqual(parenthesis.parenthesis('[]([]'), 3)
        self.assertEqual(parenthesis.parenthesis('{{{[][][]'), 3)
        self.assertEqual(parenthesis.parenthesis('sdfdfsdsdf'), 'Success')
        self.assertEqual(parenthesis.parenthesis('sdfdfsdsdf('), 11)

    def test_parenthesis_incorrect_input(self):
        self.assertRaises(TypeError, parenthesis.parenthesis, -2)

    #
    def test_parenthesis_stress(self):
        for _ in range(1000):
            n = random.randint(0, 1000)
            s = (random.choice(['[', '(', '{', ']', ')', '}', '*', 'a', '-']) for _ in range(n))
            s = ''.join(list(s))
            self.assertRegex(str(parenthesis.parenthesis(s)), '[0-9]+|Success')
