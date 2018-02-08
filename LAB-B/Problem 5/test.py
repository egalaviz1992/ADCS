# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:46:48 2018

@author: langeles
"""
#Unit testing for problem 5 from LabB-B.1
import unittest
from reversed_string import reverse_string
class ReversedStringTest(unittest.TestCase):
    string_from_user = ""
    def setup(self):
        self.string_from_user = "Hola como estas"
    def test_string_correct_reversed_value(self):
        self.assertEqual(reverse_string("Hola como estas"),"estas como Hola")
    def test_with_only_1_word(self):
        self.assertEqual(reverse_string("Hola"),"Error, la oracion debe de tener mas de 1 palabra")
    def test_with_null_string(self):
        self.assertEqual(reverse_string(""),"Error, la oracion no debe de estar vacia")
    def test_with_only_blank_space(self):
        self.assertEqual(reverse_string(" "),"Error, la oracion debe tener por lo menos una palabra y no solo espacio")
    def test_with_long_string(self):
        self.assertEqual(reverse_string("Esta es una cadena de mas de ocho palabras"),"palabras ocho de mas de cadena una es Esta")
        
unittest.main()
