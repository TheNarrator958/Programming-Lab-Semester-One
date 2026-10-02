# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : Assignment 3A

print("[Character Frequencies]")
text = input("Enter a string: ")
 
text = text.replace(" ", "").lower()
 
remaining = text  

for ch in text:
    if ch in remaining and ch != "0":
        count = 0
        for c in remaining:
            if c == ch:
                count += 1
 
        if count == 1:
            print(f"{ch} appears {count} time")
        else:
            print(f"{ch} appears {count} times")
 
        remaining = remaining.replace(ch, "0")