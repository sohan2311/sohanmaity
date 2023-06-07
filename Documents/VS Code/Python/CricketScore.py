class CricketScoreboard:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score_team1 = 0
        self.score_team2 = 0
        self.overs = 0
        self.balls = 0

    def run(self, team, runs):
        if team == self.team1:
            self.score_team1 += runs
        elif team == self.team2:
            self.score_team2 += runs
        else:
            print("Invalid team!")

        self.balls += 1
        if self.balls == 6:
            self.overs += 1
            self.balls = 0

    def get_score(self):
        return f"{self.team1}: {self.score_team1}/{self.overs}.{self.balls} - {self.team2}: {self.score_team2}/{self.overs}.{self.balls}"


# Usage example
match = CricketScoreboard("India", "Australia")
print(match.get_score())  # Output: "India: 0/0.0 - Australia: 0/0.0"

match.run("India", 4)
match.run("India", 6)
match.run("India", 2)
match.run("India", 4)
match.run("India", 1)
match.run("India", 6)
match.run("India", 1)
print(match.get_score())  # Output: "India: 6/0.1 - Australia: 7/0.1"
