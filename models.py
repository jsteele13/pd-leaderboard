class Responder:
    user_id: str = "" # id of User in Pagerduty
    name: str = ""
    hours_covered: float = 0.0 # total number of overridden hours completed

    def __init__(self, id_input: str, name_input: str):
        self.user_id = id_input
        self.name = name_input

    def add_covered_shift(self, duration: float):
        self.hours_covered += duration


class Team:
    responders_roster: dict[str, Responder] = {}

    def __init__(self):
        pass

    # create Team object from stored json database
    def __init__(self, database: str):
        pass

    # order by hours_covered, then post to leaderboard.txt
    def update_leaderboard(self):
        pass