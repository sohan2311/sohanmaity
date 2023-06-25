import itertools
from datetime import datetime,timedelta

print("IPL Schedule 2023")


def schedule_matches(teams, start_date):
    num_teams = len(teams)
    num_rounds = (num_teams - 1)

    fixtures = []
    match_date = start_date.replace(hour=14, minute=30)
  
    for round_num in range(num_rounds):
        round_fixtures = []
        for i in range(num_teams // 2):
            home = teams[i]
            away = teams[num_teams - 1 -i]
            round_fixtures.append((home, away , match_date))
            match_date += timedelta(hours = 5) # Increase time by 5 hours 
            match_date += timedelta(days = 1)
           # Move to the next day
          
            
            
            
        fixtures.append(round_fixtures)
        teams.insert(1, teams.pop())

  
 
    return fixtures

# Fix the code to play one match at 2:30 PM and the next match at 7:30 PM on each day
def fix_schedule(fixtures):
    for round_num, round_fixtures in enumerate(fixtures):
        day_counter = 0
        for i in range(0, len(round_fixtures), 2):
            first_match = round_fixtures[i]
            second_match = round_fixtures[i + 1]

            # Play the first match at 2:30 PM
            first_match_date = first_match[2] + timedelta(days=day_counter, hours=2, minutes=30)

            # Play the second match at 7:30 PM
            second_match_date = first_match[2] + timedelta(days=day_counter, hours=7, minutes=30)

            round_fixtures[i] = (first_match[0], first_match[1], first_match_date)
            round_fixtures[i + 1] = (second_match[0], second_match[1], second_match_date)

            day_counter += 1

    return fixtures

# Example usage
team_names = ['Royal Challengers Bangalore' , 'Chennai Super Kings' , 'Kolkata Knight Riders' , 'Delhi Capitals' , 'Mumbai Indians' , 'Gujarat Titans' , 'Lucknow Super Giants','Punjab Kings','Rajasthan Royals','Sunrisers Hyderabad']
start_date = datetime(2023, 6, 20) #Specify the start date
fixtures = schedule_matches(team_names, start_date)

# Fix the Schedule
fixtures = fix_schedule(fixtures)

#Display the fixtures
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

print()
print ("--- Knockout Stage ---")
print()










