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
    areaValue = 0
    perimeterValue = 0

    def isValid(w, h):
        totalValue = w + h

        if totalValue < 30:
            return False
        else:
            return True

    if isValid(width, height) == False:
        print("This is an invalid rectangle.")

    def area(w, h):
        float(areaValue) = w * h

    def perimeter(w, h):
        float(perimeterValue) = 2 * (w + h)

    if isValid(width, height) == True:
        print(f"The area is: {float(areaValue)}")
        print(f"The perimeter is: {float(perimeterValue)}")

    inA = input("Do you want to enter another width and height (Y/N)?: ")

    if inA == "Y" or inA == "y":
        running = True
    elif inA == "N" or inA == "n":
        running = False