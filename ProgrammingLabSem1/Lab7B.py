# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : 7B

import MyMath


num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

minValue = MyMath.my_min(num1, num2)
maxValue = MyMath.my_max(num1, num2)
avgValue = MyMath.my_avg(num1, num2)

print(f"Min is: {minValue}")
print(f"Max is: {maxValue}")
print(f"Average is: {avgValue}")