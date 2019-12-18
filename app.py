from src.Database.DatabaseHandler import DatabaseHandler
from src.Datastructures.StandupEvent import StandupEvent
from src.Standup.Standup import Standup
db = DatabaseHandler()
stnd = Standup()

# s = StandupEvent(
#     description="test data",
#     blocker="None",
# )


add_standup: str = "+"
prefix = add_standup

while (False):
    
    ans = input(prefix)

    if ans == add_standup:

        prompt = "Today: "
        desc = input(prompt)

        prompt = "Blockers: "
        blocker = input(prompt)
        
        s = StandupEvent(
            description=desc,
            blocker=blocker,
        )

        db.add_standup_event(s)

        stnd.copy_status_to_clipboard(s,s)
        print("Copied to your clip-board")
        continue

db.print_tables()