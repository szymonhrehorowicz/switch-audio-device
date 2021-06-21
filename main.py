from dj_deck import dj_deck


from dj_deck import dj_deck
import os
config = "config.config"

with open(config) as f:
    content = f.readlines()

deck = dj_deck(config, content)
program_running = True
while program_running:
    os.system("cls")