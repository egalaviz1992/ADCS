import unittest
from isPalindrome import *

class UnitIsPalindrome(unittest.TestCase):
    def test_split_string1(self):
        self.assertEqual(split_string("hola"),("ho","la"))
    def test_split_string2(self):
        self.assertEqual(split_string("ho la"),("ho","la"))
    def test_split_string3(self):
        self.assertEqual(split_string(""),("",""))
    def test_split_string4(self):
        self.assertEqual(split_string("anitalavalatina"),("anitala","alatina"))
    def test_split_string5(self):
        self.assertEqual(split_string("ani"),("a","i"))

        
    def test_is_palindrome1(self):
        self.assertEqual(is_palindrome("hola"),False)
    def test_is_palindrome2(self):
        self.assertEqual(is_palindrome("hola aloh"),True)
    def test_is_palindrome3(self):
        self.assertEqual(is_palindrome("anitalavalatina"),True)
    def test_is_palindrome4(self):
        self.assertEqual(is_palindrome("Janitalavalatina"),False)
    def test_is_palindrome5(self):
        self.assertEqual(is_palindrome(""),True)
    def test_is_palindrome6(self):
        self.assertEqual(is_palindrome(" "),True)


if __name__ == '__main__':
    unittest.main
