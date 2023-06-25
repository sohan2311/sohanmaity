import itertools
from datetime import datetime,timedelta

print()
print("IPL Schedule 2023")


def schedule_matches(teams, start_date):
    num_teams = len(teams)
    num_rounds = (num_teams - 1)

    fixtures = []
    match_date = start_date
    for round_num in range(num_rounds):
        round_fixtures = []
        for i in range(num_teams // 2):
            home = teams[i]
            away = teams[num_teams - 1 -i]
            if (i + round_num) % 2 == 0:
                match_time = match_date.replace(hour = 19 , minute = 30)
            else:
                match_time = match_date.replace(hour = 14 , minute = 30)
            round_fixtures.append((home, away , match_date))
            match_date += timedelta(days=1)
        fixtures.append(round_fixtures)
        teams.insert(1, teams.pop())

    return fixtures

# Example usage
team_names = ['Royal Challengers Bangalore' , 'Chennai Super Kings' , 'Kolkata Knight Riders' , 'Delhi Capitals' , 'Mumbai Indians' , 'Gujarat Titans' , 'Lucknow Super Giants','Punjab Kings','Rajasthan Royals','Sunrisers Hyderabad']
start_date = datetime(2023, 6, 20) #Specify the start date
fixtures = schedule_matches(team_names, start_date)

# Display the fixtures

match_num = 0
for round_num, round_fixtures in enumerate(fixtures):
    print()
    print(f"Round {round_num + 1} Fixtures:")
    print()
    
    for match in round_fixtures:
    
        home, away , match_date  = match
        
        print(f"Match { match_num + 1}: -- Date : {match_date} -- {home} (Home) vs {away} (Away) ")
        match_num +=1
        
match_num = 45
for round_num, round_fixtures in enumerate(fixtures):
    print()
    print(f"Round {round_num + 10} Fixtures:")
    print()
    
    for match in round_fixtures:
    
        away, home , match_date  = match
        
        print(f"Match { match_num + 1}: -- Date : {match_date} -- {home} (Home) vs {away} (Away)  ")
        match_num +=1












