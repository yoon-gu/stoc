import unittest
import stoc
class TestStringMethods(unittest.TestCase):

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
		import stoc
		self.assertEqual(stoc.__author__, 'Jacob Hwang <yz0624@gmail.com>')
	def test_bm(self):
		self.assertEqual(stoc.bm(), "hello")