# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : 6A

choice = 0

while choice != 3:
    print("Multiplication and Exponent Calculator")
    print("Choose option 1 for Multiplication")
    print("Choose option 2 for Exponentiation")
    print("Choose option 3 to Exit")
    choice = int(input())
 
    if choice == 1:
        print()
        a = int(input("Enter an operand: "))
        b = int(input("Enter the other operand: "))
 
        product = 0
        for _ in range(abs(b)):
            product += a
        if b < 0:
            product = -product
 
        print(f"{a} x {b} = {product}")
        print()
 
    elif choice == 2:
        print()
        base = int(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
        result = 1
        for _ in range(exponent):
            new_result = 0
            for _ in range(abs(base)):
                new_result += result
            if base < 0:
                new_result = -new_result
            result = new_result
 
        print(f"{base}^({exponent}) = {result}")
        print()
 
    elif choice == 3:
        print()
        print("Closing the Calculator...")
 
    else:
        print()
        print("Invalid Choice")
        print()