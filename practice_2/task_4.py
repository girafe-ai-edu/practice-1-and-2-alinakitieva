# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
number = input("Please enter a 4-digit number: ")
def sum_digits(number):
    if len(number) != 4:
        print("Please enter a 4-digit number")
    print("The sum of the digits in the number is:", sum([int(digit) for digit in number]))

sum_digits(number)