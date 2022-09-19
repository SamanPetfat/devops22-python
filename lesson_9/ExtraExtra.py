import random

class Person:

    def __init__(self, name, year):
        self.name = name
        self.year = year

class Player(Person):

    def __init__(self, name, year, stats):
        self.stats = stats
        super().__init__(name, year)

    def __str__(self):
        return f"{self.name} [{self.year}] -Stats: {self.stats}"


class Coach(Person):
    def __init__(self, name, year, voice):
        self.voice = voice
        super().__init__(name, year)

    def __str__(self):
        return f"{self.name} [{self.year}] - Voice: {self.voice}"

class Team:
    def __init__(self, players, coach):
        self.players = players
        self.coach =   coach

    def summarize_team(self):
        team = """
-----------------------------------
-------------- My Team ------------
-----------------------------------
"""        
        team += f"coach {self.coach}\n"
        team += "-------------- Players ------------\n"
        team += "\n".join(map(str,self.players))
        return team


def get_random_stats():
    return (
        f"Speed: [{random.randint(1, 10)}]",
        f"Agility: [{random.randint(1, 10)}]",
        f"Strenght: [{random.randint(1, 10)}]")


def main():
    coach = Coach("pelle", 1959, 5)

    players = []
    for name in ["lisa", "eva", "petra","anna","hanna","malin","johanna","alena","nina","lina"]:
        year = random.randint(1987,2004)
        players.append(Player(name, year, get_random_stats()))

    team = Team(players, coach)
    print(team.summarize_team())


if __name__== "__main__":
    main()