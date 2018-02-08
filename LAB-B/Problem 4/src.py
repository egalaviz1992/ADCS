# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:45:56 2018

@author: langeles
"""
#Exercise 4: Overlapping numbers between prime and happy numbers

def prime_happy_overlapping():
    prime_numbers_file = open("primenumbers.txt","r")
    happy_numbers_file = open("happynumbers.txt","r")
    prime_numbers = prime_numbers_file.readlines()
    happy_numbers = happy_numbers_file.readlines()
    output_file = open("output.txt","w")
    overlapping_numbers = []
    for prime in prime_numbers:
        if prime in happy_numbers:
            overlapping_numbers.append(prime)
            output_file.write(prime)
    output_file.close()
    return overlapping_numbers
def validate_overlapping(number):
    overlapping_numbers=prime_happy_overlapping()
    for happy_number in overlapping_numbers:
        if number == int(happy_number):
            return True
    return False
    
#prime_happy_overlapping()
#validation = validate_overlapping(200)
#print(validation)
