from datetime import datetime as dt

class StandupEvent():
    def __init__(
        self,
        __id: int=-1,
        date: dt=None,
        description: str=None,
        blocker: str="None."):

        self._id = __id

        if date is None:
            self._date = dt.now()
        else:
            self._date = date

        self._description = description
        self._blocker = blocker

