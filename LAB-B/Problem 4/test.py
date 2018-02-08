# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:42:50 2018

@author: langeles
"""
#Testing file for problem 4 Lab 1, Overlapping Numbers
import unittest
import overlapping_numbers
class OverlappingNumbersTest(unittest.TestCase):
    string_from_user = ""
    def setup(self):
        self.prime_only = 2
        self.happy_only = 10
        self.prime_and_happy = 13
        self.not_prime_not_happy = 4
    def test_prime_number_not_happy(self):
        self.assertEqual(validate_overlapping(2),False)
    def test_happy_number_only(self):
        self.assertEqual(validate_overlapping(10),False)
    def test_happy_and_prime(self):
        self.assertEqual(validate_overlapping(13),True)
    def test_not_happy_not_prime(self):
       self.assertEqual(validate_overlapping(4),False)
unittest.main()
