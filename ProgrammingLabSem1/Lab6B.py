# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : 6B

import random

randNum = random.randint(1, 100)

print("Guess the number I am thinking!")

correct = False

while not correct:
    samIn = int(input("Enter any number between 1 and 100: "))
    if samIn <= 100 and samIn >= 0:
        if samIn < randNum:
            print("Too low!")
        elif samIn > randNum:
            print("Too high!")
        elif samIn == randNum:
            correct = True
            
print(f"Correct! I was thinking of {randNum}")