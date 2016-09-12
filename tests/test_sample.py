import unittest
import stoc
import numpy as np
class TestStocMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

	def test_test(self):
		self.assertTrue(True)

	def test_import(self):
		self.assertEqual(stoc.__author__, 'Jacob Hwang <yz0624@gmail.com>')

	def test_bm(self):
		size = 10
		np.random.seed(1987)
		dt = 1.0 / (size - 1)
		zero = np.zeros(1)
		val = np.sqrt(dt) * np.random.randn(size-1)
		val = np.insert(zero, 1, val)
		val = np.cumsum(val)
		self.assertEqual(stoc.bm(size, seed=1987), val)

	def test_sde(self):
		self.assertEqual(stoc.sde(), "hello")

	def test_bsde(self):
		self.assertEqual(stoc.bsde(), "hello")