import os
class dj_deck(object):
    def __init__(self, config):
        """Initialize object dj_deck. Expects name of file containing config as [config] of STR type"""
        assert type(config) == str, "ERROR! Expected STRING type parameter"

        self.config = config
        self.content = self.load_config()
        self.outputs = []
        self.current_output = None
        
        for line in self.content:
            if line[:8] == "CURR_OUT":
                self.current_output = int(line[9:-1])
            else:
                self.outputs.append(line[9:-1])

    def set_output(self, name, id):
        """Sets an output name. Expects to get new name(STRING) and ID from {1, 2}"""
        assert type(name) == str and type(id) == int and id in [0, 1], "ERROR! Expected two parameters: [name] of STR type and [id] of INT type and from {0, 1}"

        self.outputs[id] = name
        self.content[id] = self.content[id][:9] + name + "\n"
        try:
            with open(self.config, "w") as f:
                f.write("".join(self.content))
        except:
            print("ERROR! There was a problem while saving changed settings")


    def set_current(self, id):
        """Sets current audio output device. Expects to get [id] of INT type"""
        assert type(id) == int and id in [0, 1], "ERROR! Expected parameter [id] of INT type and from {0, 1}"

        self.current_output = id
        os.system(f"nircmd setdefaultsounddevice \"{self.outputs[id]}\" 1")
        self.content[2] = f"CURR_OUT={self.current_output}"
        try:
            with open(self.config, "w") as f:
                f.write("".join(self.content) + "\n")
        except:
            print("ERROR! There was a problem while saving changed settings")

    def switch(self):
        """Switches to other audio output device"""

        if self.current_output == 0:
            self.set_current(1)
        else:
            self.set_current(0)

    def get_outputs(self):
        """Prints names and ID's of currently set audio output devices"""

        print("List of outputs: \n"\
              f"ID 1: {self.outputs[0]}\n"\
              f"ID 2: {self.outputs[1]}\n")

    def load_config(self):
        """Loads data from config file"""
        
        try:
            with open(self.config) as f:
                return f.readlines()
        except:
            print("ERROR! There was a problem while working with loading configuration data")