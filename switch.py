from dj_deck import dj_deck

config = "config.config"

with open(config) as f:
    content = f.readlines()
 
deck = dj_deck(config, content)
deck.switch()