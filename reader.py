from src.Datastructures.StandupEvent import StandupEvent
from src.Database.DatabaseHandler import DatabaseHandler
from datetime import datetime as dt
from dateutil.parser import parse

db = DatabaseHandler()

with open("Standup", "r+") as in_file:
    count = 0
    date = ''
    yesterday = ''
    today = ''
    blocker = ''

    for line in in_file.readlines():
        cleaned_string = line.replace("*Yesterday*: ", "")
        cleaned_string = cleaned_string.replace("*Today*: ", "")
        cleaned_string = cleaned_string.replace("*Blocker*: ", "")
        cleaned_string = cleaned_string.replace("*", "")
        cleaned_string = cleaned_string.replace("\n", "")


        if count == 0:
            date = cleaned_string

        if count == 1:
            today = cleaned_string

        if count == 2:
            yesterday = cleaned_string

        if count == 3:
            blocker = cleaned_string

        if count == 4:
            s = StandupEvent(
                date = parse(date),
                description=today,
                blocker=blocker
            )
            db.add_standup_event(s)
            count = 0
            continue
        
        count = count + 1

