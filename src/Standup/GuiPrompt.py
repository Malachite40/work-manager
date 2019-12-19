from os import system, name

class GuiPrompt():

    def __init__(self):
        self._message = "Welcome!"
        self._continue_prompt = "[Enter] to continue."
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
            print("{} | {}".format(v, k))

    def print_top(self):
        self.print_bottom()
        print("  {}".format(self._message))
        print("_________________________")

    def print_bottom(self):
        print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")

    def print_menu(self, options: {}):
        self.print_top()
        self.print_options(options)
        self.print_bottom()
    
    def set_message(self, message):
        self._message = message