print("Welcome to the Guess the Word game!")
word = input("Enter a word to guess (lowercase letters only): ")
 
display = ""
for i in range(len(word)):
    display += "_"
 
while display != word:
    print()
    print("The word to guess is: " + " ".join(display))
    guess = input("Guess a letter: ")
 
    if guess in word:
        new_display = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_display += guess
            else:
                new_display += display[i]
        display = new_display
        print("Good guess!")
    else:
        print("Oops! That letter is not in the word.")
 
print()
print(f"Congratulations! You've guessed the word: {word}")