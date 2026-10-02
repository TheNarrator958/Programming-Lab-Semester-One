# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : Assignment 3A

size = int(input("Enter an odd number for the size of the diamond: "))
 
if size % 2 == 0:
    size += 1
    print(f"Size must be an odd number; we will increase it to {size}")
 
digit = 0  
middle = size // 2
 
for row in range(size):
    k = min(row, size - 1 - row)
    spaces = middle - k
    count = 2 * k + 1
 
    for _ in range(spaces):
        print(" ", end="")
 
    for _ in range(count):
        print(digit, end="")
        digit = (digit + 1) % 10
 
    print()