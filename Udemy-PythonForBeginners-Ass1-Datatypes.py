"""Udemy - Pyhon for beginners - Assignment 1: Datatypes
Define driver license info., store them in correct datatypes and print them
"""

firstName = str("Ivan")
lastName = str("Tomic")
age = int(24)
ssn = str(1234567890) #SSN is a number, but is string because we won't be doing any math operations, since this number is ID
height = int(190)
weight = int(83)

print("First Name: " + firstName)
print("Last Name: " + lastName)
print("Age: " + str(age) + " years")
print("SSN: " + ssn)
print("Height: " + str(height) + " cm")
print("Weight: " + str(weight) + " kg")