from datetime import datetime as dt

class StandupEvent():
    def __init__(
        self,
        standup_id: int=-1,
        date: dt=None,
        description: str=None,
        blocker: str=None):

        self._id = standup_id

        self._date = date
        if date is None:
            self._date = dt.now()

        self._description = description
        if description is None:
            self._description = "Nothing."

        self._blocker = blocker
        if blocker is None:
            self._blocker = "None."

    def print(self):
        print(self.string())

    def string(self):
        return (
           "ID: {}".format(self._id) + "\n" +
           "DATE: {}".format(self._date) + "\n" +
           "DESCRIPTION: {}".format(self._description) + "\n" +
           "BLOCKER: {}".format(self._blocker) + "\n"
        )