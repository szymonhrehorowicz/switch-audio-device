from dj_deck import dj_deck

config = "config.conf"

with open(config) as f:
    content = f.readlines()
    #TODO: error handling, when file does not exist
    f.close()
 
deck = dj_deck(config, content)
deck.switch()