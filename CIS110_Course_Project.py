#A gnome and his hat.

import os
import sys
from tkinter import CHAR
os.system("")

#Using ANSI escape codes to make a function that clears lines (This does not work in the IDE, must be run externally in the python terminal)
def delete_last_line(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1A') #Move cursor up a line
        sys.stdout.write('\x1b[2K') #Deletes the line

#Function to print a line then wait for player to continue. Uses above "delete last line" function to delete instruction line.       
def story(line):
    print(f"{line}")
    input(f"Press Enter to continue")
    delete_last_line(1)

#Greet the user and explain how to play.
print(f"Welcome to 'A Gnome and his Hat'.")
print(f"Here you will partake in a tale of a Gnome who's lost his hat.")
print(f"Before we begin, I'll ask you a few questions.")
story(f"After typing your answer, be sure to press the enter key.\n")

#5 questions to fill variables.
character = input(f"What is the gnome's name? ").strip()
while len(character) == 0:
    character = input(f"The gnome cannot be nameless, please enter a name: ").strip()
character = character[0].upper() + character[1:] #Names should be capitalized

hair = input(f"While we all know gnome's have white beard's, what color is {character}'s hair? ").strip()
while len(hair) == 0:
    hair = input(f"Please enter a color: ").strip()

hat_color = input(f"What color is {character}'s hat?").strip()
corrected = False #whether or not player was corrected
while hat_color.lower() == "colorless" or len(hat_color) == 0:
    if hat_color.lower() == "colorless" and corrected:
        hat_color = input(f"You think you're funny, don't you? Enter a color: ").strip()
    else:
        hat_color = input(f"A gnome's hat is important, it can't be colorless! Enter a color: ").strip()
        corrected = True

hat_material = input(f"What is the material of {character}'s hat? ").strip()
corrected = False
while hat_material.lower() == "nothing" or len(hat_material) == 0:
    if hat_material.lower() == "nothing" and corrected > 0:
        hat_material = input(f"Funny guy, huh? C'mon, we don't have all day... or do we? Enter a material: ").strip()
    else:
        hat_material = input(f"You can't make a hat out of nothing! Enter a material: ").strip()
        corrected = True

favorite_thing = input(f"What is {character}'s favorite thing? What gives {character} comfort? ").strip()
while len(favorite_thing) == 0:
    favorite_thing = input(f"There must be SOMETHING {character} loves! Enter a favorite thing: ").strip()
if favorite_thing.lower() == "something":
    print(f"Okay funny guy. You know what? You're stuck with it now.")

input(f"Press Enter to begin the story")

os.system('cls') #clears screen to start the story on a fresh page, this also doesn't work from the IDE.

#Title banner
print("-"*20)
print("A Gnome and his Hat")
print("-"*20,"\n")
story(" ")

#Story Intro
story(f"Our story begins here in a lush garden as dusk begins to set. Sunlight barely peeking from the western horizon.")
story(f"{character} awakens with a yawn and a stretch. Invigorated in a way that only 'morning people' understand.")
story(f"{character} wipes the sleep from his eyes as he enjoys the slight breeze enveloping him.")
story(f"'The wind feels great blowing through my lush {hair},' {character} thinks to himself...")
story(f"Or he would if he had any hair. Instead the rush of cold air across his balding head brings him to a frightening conclusion...")
story(f"'MY HAT! MY HAT IS GONE!' {character} exclaims with great urgence!")
story(f"He searches frantically for his hat throughout the garden. But try as he might, he can't find that deep {hat_color} hat. Not even a trace of {hat_material}!")
story(f"While looking for his {hat_color} hat, he comes upon a dark black feather.")
story(f"'OF COURSE! I, {character}, would NEVER lose such a fine {hat_material} hat! I'VE BEEN ROBBED!' {character} thinks out loud.")
story(f"'Well! I can't just wait around here! I've got to track them down! Who knows how far the thief has already gotten!' He shouts as he rushes to prepare himself.\n")

#Decision 1
bring_bag = input(f"Should {character} bring his bag? It may slow him down. Type yes or no: ").lower().strip()
while bring_bag != "yes" and bring_bag != "no":
    bring_bag = input("Please type yes or no: ").lower().strip()
    
if bring_bag == "yes":
    story(f"While {character}'s movement is slowed, the clink of his coins reassures him.")
else:
    story(f"Unsure how far the thief has gotten, {character} decides to leave his belongings behind.")
    story(f"He feels invigorated by the wind in his beard.")

story(f"\nFollowing the trail of feathers takes {character} out of the garden.")
story(f"This is the first time in months, if not years, that {character} has ventured beyond the flowers he calls home.")
story(f"Sadly, he does not have time to enjoy the sights of suburbia laid before him.")
story(f"Chasing after the feathers, he comes upon a large, slumbering beast. Its black feathers raising with each breath.")
story(f"Beneath the beast, he catches a glimse of {hat_color} {hat_material}.")
story(f"'THAT'S! IT MUST BE! IT'S MY HAT!!!!!' {character} thinks with bewildered eyes.\n")

#Decision 2
approach = input(f"Does {character} dare to approach the sleeping creature? Type yes or no: ").lower().strip()
while approach != "yes" and approach != "no":
    approach = input(f"Please type yes or no: ").lower().strip()

if approach == "yes":
    story(f"Steeling his nerves, {character} creeps forward.\n")
else:
    story(f"'Of course! Such a small gnome as myself could never dare to anger a beast such as this!' {character} assures himself.")
    story(f"Certain in his thoughts, he decides his hat, while oh so precious, is not worth the danger.")
    story(f"{character} turns back; saddened, but glad to be alive\n")

#Ending 1
if bring_bag == "yes" and approach == "yes":
    story(f"Approaching the beast, {character} realizes too late the he should've left his bag.")
    story(f"As he nears the rising feathers, a resounding CLING comes from the sack on his back.")
    story(f"The beast begins to rise, alerted by the sound.")
    story(f"Upon looking at {character}, the fearsome creature caws, but it doesn't sound like a threat.")
    story(f"No...")
    story(f"Is this?...")
    story(f"Laughter?")
    story(f"The beast is laughing at {character}'s balding head!")
    story(f"Angered by the mocking of the feathered foe, {character} chucks one of his few coins at the beast.")
    story(f"Realizing the grave mistake he just made {character} steps back in fear of what's to come.")
    story(f"However, this only causes more laughter from the creature.")
    story(f"As if to humor him, the beast accepts the coin as if it were a trade. Returning to {character} his forlorn hat. Still laughing as he leaves.")
    story(f"Arriving back at the garden, {character} inspects his {hat_color} hat for any damage.")
    story(f"Wait...")
    story(f"This nametag...\n")
    print("-"*22)
    print("PROPERTY OF GNOMISLAV")
    story('-'*22)
    if character.lower() == "gnomislav":
        story(f"\n{character} sheds a single tear of joy for the reunion with his hat")
        story(f"He plops down on the cool night ground and puts his beautiful {hat_color} {hat_material} hat back in it's rightful place upon his head.")
        story(f"'I'll never let you go again,' he swears.")
        print(f"/n","-"*8)
        print(f"THE END.")
        story("-"*8)
    else:
        story(f"\n'THIS ISN'T EVEN MY HAT!!!!!'")
        print(f"/n","-"*8)
        print(f"THE END?")
        story("-"*8)
