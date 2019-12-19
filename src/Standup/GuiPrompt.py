from os import system, name

class GuiPrompt():

    def __init__(self):
        super().__init__()

    def clear(self) -> None:

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def print_options(self, options: {}) -> None:


        for k, v in options.items():
            print("{} :: {}".format(k, v))