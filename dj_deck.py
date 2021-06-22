import os
class dj_deck(object):
    def __init__(self, filename, content):
        """Expects an array with two STRING type names of audio output devices and config as STRING of a config file name/path"""
        assert type(filename) == str, "ERROR! Expected STRING type parameter"
        self.outputs = []
        self.current_output = None
        i = 0
        for line in content:
            if i == 2:
                self.current_output = int(line[9:-1])
            else:
                self.outputs.append(line[9:-1])
            i += 1
        self.config = filename
        self.content = content

    def set_output(self, name, id):
        """Sets an output name. Expects to get new name(STRING) and ID from range of <1-2>"""
        assert type(name) == str and type(id) == int and id in range(1,3), "ERROR! Expected two parameters: [name] of STRING type and [id] of INT type and in range <1-2>"
        self.outputs[id - 1] = name
        #TODO: save in config file

    def set_current(self, id):
        """Sets current audio output device. Expects to get id(INT)"""
        assert type(id) == int and id in range(1,3), "ERROR! Expected parameter [id] of INT type and from range 1-2"
        self.current_output = id
        os.system(f"nircmd setdefaultsounddevice \"{self.outputs[id]}\" 1")
        self.content[2] = f"CURR_OUT={self.current_output}"
        with open(self.config, "w") as f:
            new_content = ""
            for line in self.content:
                new_content += line
            new_content += "\n"
            f.write(new_content)

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