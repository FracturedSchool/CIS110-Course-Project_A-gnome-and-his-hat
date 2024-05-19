#A gnome and his hat.

import sys
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
def delete_last_line(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

#Greet the user and explain how to play.
print(f"Welcome to 'A Gnome and his Hat'.")
print(f"Here you will partake in a tale of a Gnome who's lost his hat.")
print(f"Before we begin, I'll ask you a few questions.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress enter to continue...")
delete_last_line(2)