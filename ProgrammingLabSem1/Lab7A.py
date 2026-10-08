# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : 7A

running = True

while running:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    def isValid(w, h):
        totalValue = w + h

        if totalValue < 30:
            return False
        else:
            return True

    if isValid(width, height) == False:
        print("This is an invalid rectangle.")

    if isValid(width, height) == True:
        print("This is a valid rectangle.")

    def area(w, h):
        return w * h

    def perimeter(w, h):
        return 2 * (w + h)

    aV = area(width, height)
    pV = perimeter(width, height)

    if isValid(width, height) == True:
        print(f"The area is: {aV}")
        print(f"The perimeter is: {pV}")

    inA = input("Do you want to enter another width and height (Y/N)?: ")

    if inA == "Y" or inA == "y":
        running = True
    elif inA == "N" or inA == "n":
        running = False

print("Program Ends")