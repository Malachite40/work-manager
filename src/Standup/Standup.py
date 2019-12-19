
from src.Datastructures.StandupEvent import StandupEvent
class Standup():

    def __init__(self):
        return

    def generate_standup_status(self, yesterday: StandupEvent, today: StandupEvent):

        string: str = (
            "*{}* ".format(today._date) + "\n" +
            "*Yesterday*: {}".format(yesterday._description) + "\n" +
            "*Today*: {}".format(today._description) + "\n" +
            "*Blockers*: {}".format(today._blocker)+  "\n"
        )

        return string