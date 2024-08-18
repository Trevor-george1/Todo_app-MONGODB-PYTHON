#!/usr/bin/env python3
"""main program"""

import time
from services.creat_note_service import fetch_data_to_create_note
from services.display_note import display_notes
import mongo_setup as mongo_setup

mongo_setup.global_init()

print("Launching GNZ To-do app:")
print("==========================")
print("Loading....")
time.sleep(3)
print()
print("Welcome user to GNZ To-do app")
print("-----------------------")

while 1:
    print("1. [C]reate a note")
    print("2. [D]isplay Todo List")
    print("-----------------------")
    choice = input("Choose option to continue(C or D)... ")

    if choice == 'create' or choice == 'c' or choice == 'C':
        note = fetch_data_to_create_note()
        break
        #create_todo()
    elif choice == 'display' or choice == 'd' or choice == 'D':
        display_notes()
        break
    else:
        print("Invalid choice. Try again")