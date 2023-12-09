from collections import namedtuple
import json
import random

FILE_ENCODING = "utf-8"
LEADERS_PATH = "leaders.json"
PLAYERS_PATH = "player_history.json"


DraftOutcome = namedtuple('DraftOutcome', 'name leader civ')


class Leaders:
    def __init__(self, path: str = LEADERS_PATH) -> None:
        with open(path, encoding=FILE_ENCODING) as stream:
            self.leads = json.load(stream)

    def pick_random(self, player_recent: list) -> dict:
        new_nations_for_player = [
            nation 
            for nation in self.leads 
            if nation["leader name"] not in player_recent
        ]
        choice = random.choice(new_nations_for_player)
        leftover_nations = [
            nation
            for nation in self.leads
            if choice["civ"] != nation["civ"]
        ]
        self.leads = leftover_nations
        return choice


class Draft:
    def __init__(self, todays_players: list, path: str = PLAYERS_PATH) -> None:
        with open(path, encoding=FILE_ENCODING) as stream:
            players = json.load(stream)
            self.players = []
            for player in players:
                if player["name"] in todays_players:
                    self.players.append(player)

    def draft(self, leaders: Leaders) -> list:
        output = []
        for _ in range(len(self.players)):
            player = random.choice(self.players)
            self.players.remove(player)
            nation = leaders.pick_random(player["played recently"])
            output.append(
                DraftOutcome(player["name"], nation["leader name"], nation["civ"])
            )
        return output


def main():
    players = Draft(["Алесь", "Мишаня", "Саман", "Елизавета", "Вишня"])
    leaders = Leaders()
    for result in players.draft(leaders):
        print(f"{result.name} играет за {result.leader}, {result.civ}")


if __name__ == "__main__":
    main()