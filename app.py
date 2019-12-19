from src.Database.DatabaseHandler import DatabaseHandler
from src.Datastructures.StandupEvent import StandupEvent
from src.Standup.Standup import Standup
from src.Standup.GuiPrompt import GuiPrompt

import pyperclip
from dateutil.parser import parse
from datetime import datetime as dt

gui = GuiPrompt()
db = DatabaseHandler()
stnd = Standup()

save_file: str = "standups.txt"
read_file: str = "standups.txt"

add_task: str = "-"
add_standup_string: str = "+"
copy_current_standup_string: str = "c"
save_to_file_string: str = "s"
read_from_file_string: str = "r"
prefix = add_standup_string

current_message = "Welcome!"
options = {
    # "Add Task": add_task,
    "Add stand-up": add_standup_string,
    "Copy current stand-up": copy_current_standup_string,
    "Save to file": save_to_file_string,
    "Read from file": read_from_file_string,
}


def add_standup():

    prompt = "Date: "
    try:
        date = parse(input(prompt))
    except Exception as e:
        print(e)
        date = dt.now()
        print("Fallback = Default date.")
        pass

    prompt = "Today: "
    desc = input(prompt)
    if len(desc) < 1:
        desc = None

    prompt = "Blockers: "
    blocker = input(prompt)
    if len(blocker) < 1:
        blocker = None

    s = StandupEvent(
        date=date,
        description=desc,
        blocker=blocker,
    )

    db.add_standup_event(s)

def copy_current_standup():
    standups: [StandupEvent] = db.get_standups(count=2)
    if len(standups) < 1:
        gui.set_message("You need a standup.")
        return
    if len(standups) < 2:
        standups.append(StandupEvent())
    pyperclip.copy(stnd.generate_standup_status(standups[1],standups[0]))
    gui.set_message("Copied to clipboard!")

def save_to_file():
    with open(save_file, "w+") as out_file:
        for s in db.get_standups(count=-1):
            out_file.write(s.string())
            out_file.write("\n")

def read_from_file():
    with open(read_file, "r+") as in_file:
        count = 0
        date = ''
        yesterday = ''
        today = ''
        blocker = ''

        for line in in_file.readlines():
            cleaned_string = line.replace("ID: ", "")
            cleaned_string = cleaned_string.replace("DATE: ", "")
            cleaned_string = cleaned_string.replace("DESCRIPTION: ", "")
            cleaned_string = cleaned_string.replace("BLOCKER: ", "")
            cleaned_string = cleaned_string.replace("\n", "")


            if count == 0:
                standup_id = cleaned_string

            if count == 1:
                date = cleaned_string

            if count == 2:
                today = cleaned_string

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



while (True):
    
    gui.clear()
    gui.print_menu(options)
    ans = input("-")

    if ans == add_standup_string:
        add_standup()
        continue

    if ans == copy_current_standup_string:
        copy_current_standup()
        continue

    if ans == save_to_file_string:
        save_to_file()
        continue

    if ans == read_from_file_string:
        read_from_file()