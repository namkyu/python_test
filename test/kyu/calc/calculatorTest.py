import unittest

from kyu.calc.calculator import Calculator


class Test(unittest.TestCase):

    def testAdd(self):
        calculator = Calculator()
        result = calculator.add(operanda=2, operandb=3)        
        self.assertEqual(result, 5, "Addition failed")