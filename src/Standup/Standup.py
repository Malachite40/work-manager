import pyperclip

from src.Datastructures.StandupEvent import StandupEvent
class Standup():

    def __init__(self):
        return

    def copy_status_to_clipboard(self, yesterday: StandupEvent, today: StandupEvent):

        string: str = (
            "*{}* ".format(today._date) + "\n" +
            "*Yesterday*: {}".format(yesterday._description) + "\n" +
            "*Today*: {}".format(today._description) + "\n" +
            "*Blockers*: {}".format(today._blocker)+  "\n"
        )

        pyperclip.copy(string)
