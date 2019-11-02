import unittest
import rpn

class TestBasics(unittest.TestCase):
	def rest_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)