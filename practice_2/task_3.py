# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = input("Please enter your weight in kilograms: ")
height = input("Please enter your height in meters: ")


#code here
weight = float(weight)
height = float(height)

def bmi(weight, height):
    return weight / height**2

print("Your BMI is: ", bmi(weight, height))

