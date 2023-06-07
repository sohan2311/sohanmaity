class Football:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score_team1 = 0
        self.score_team2 = 0

    def goal(self, team):
        if team == self.team1:
            self.score_team1 += 1
        elif team == self.team2:
            self.score_team2 += 1
        else:
            print("Invalid team!")

    def get_score(self):
        return f"{self.team1}: {self.score_team1} - {self.team2}: {self.score_team2}"


# Usage example
match = Football("Real Madrid", "Barcelona")

match.goal("Real Madrid")
match.goal("Barcelona")
match.goal("Barcelona")
match.goal("Real Madrid")
match.goal("Barcelona")
match.goal("Real Madrid")
match.goal("Real Madrid")
print(match.get_score())  # Output: "Real Madrid: 1 - Barcelona: 2"

