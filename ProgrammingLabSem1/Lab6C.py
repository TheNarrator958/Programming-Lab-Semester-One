# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : 6C

rows = int(input("Enter Number for Rows or 0 to quit: "))
 
while rows != 0:
    for row in range(1, rows + 1):
        line = " " * (rows - row)
 
        for num in range(row, 0, -1):
            line += str(num)
        for num in range(2, row + 1):
            line += str(num)
 
        print(line)
 
    rows = int(input("Enter Number for Rows or 0 to quit: "))