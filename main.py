from dj_deck import dj_deck
import os
config = "config.conf"

with open(config) as f:
    content = f.readlines()
    #TODO: error handling, when file does not exist
    f.close()

deck = dj_deck(config, content)
program_running = True
while program_running:
    os.system("cls")
    print("Welcome to DJ Deck v0.1")
    print("-----------------------")
    print("1. Get outputs")
    print("2. Set output")
    print("3. Switch audio devices")
    print("[exit]")
    answer = input()

    if answer == "1":
        os.system("cls")
        deck.get_outputs()
        input("go back")
    elif answer == "2":
        os.system("cls")
        name = input("Output name: ")
        id = int(input("Output id[1-2]: "))
        deck.set_output(name, id)
        print("Successfully changed device name")
        input("go back")
    elif answer == "3":
        os.system("cls")
        deck.switch()
        print("Successfully switched output device")
        input("go back")
    elif answer == "exit":
        break