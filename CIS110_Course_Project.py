#A gnome and his hat.

import os
import sys
os.system("")

#Using ANSI escape codes to make a function that clears lines (This does not work in the IDE, must be run externally in the python terminal)
def delete_last_line(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1A') #Move cursor up a line
        sys.stdout.write('\x1b[2K') #Deletes the line

#Function to use delete_last_line to wait for player        
def wait():
    input(f"Press Enter to continue")
    delete_last_line(1)

#Greet the user and explain how to play.
print(f"Welcome to 'A Gnome and his Hat'.")
print(f"Here you will partake in a tale of a Gnome who's lost his hat.")
print(f"Before we begin, I'll ask you a few questions.")
print(f"After typing your answer, be sure to press the enter key.\n")
wait()

#5 questions to fill variables.
character = input(f"What is the gnome's name? ").strip()
while len(character) == 0:
    character = input(f"The gnome cannot be nameless, please enter a name: ").strip()

hair = input(f"While we all know gnome's have white beard's, what color is {character}'s hair? ").strip()
while len(hair) == 0:
    hair = input(f"Please enter a color: ").strip()

hatColor = input(f"What color is {character}'s hat?").strip()
corrected = False #whether or not player was corrected
while hatColor.lower() == "colorless" or len(hatColor) == 0:
    if hatColor.lower() == "colorless" and corrected:
        hatColor = input(f"You think you're funny, don't you? Enter a color: ").strip()
    else:
        hatColor = input(f"A gnome's hat is important, it can't be colorless! Enter a color: ").strip()
        corrected = True

hatMaterial = input(f"What is the material of {character}'s hat? ").strip()
corrected = False
while hatMaterial.lower() == "nothing" or len(hatMaterial) == 0:
    if hatMaterial.lower() == "nothing" and corrected > 0:
        hatMaterial = input(f"Funny guy, huh? C'mon, we don't have all day... or do we? Enter a material: ").strip()
    else:
        hatMaterial = input(f"You can't make a hat out of nothing! Enter a material: ").strip()
        corrected = True

favoriteThing = input(f"What is {character}'s favorite thing? What gives {character} comfort? ").strip()
while len(favoriteThing) == 0:
    favoriteThing = input(f"There must be SOMETHING {character} loves! Enter a favorite thing: ").strip()
if favoriteThing.lower() == "something":
    print(f"Okay funny guy. You know what? You're stuck with it now.")

input(f"Press Enter to begin the story")

os.system('cls') #clears screen to start the story on a fresh page