# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:12:08 2018

@author: langeles
"""
#Exercise 5: Ask the user for a string and print it backwards
def reverse_string(string_from_user):
    if not string_from_user:
        return "Error, la oracion no debe de estar vacia"
    if string_from_user == " ":
        return "Error, la oracion debe tener por lo menos una palabra y no solo espacio"
    lista_string = string_from_user.split(" ")
    if len(lista_string) > 1:
        result = reversed(lista_string)
        result_string = ""
        for i in result:
            result_string = result_string + i + " "
        result_string = result_string.strip()
        return result_string
    else:
        return "Error, la oracion debe de tener mas de 1 palabra"

#string_from_user = input("Please enter a string of length higher than 1")
#resultado = reverse_string(string_from_user)
#print(resultado)


