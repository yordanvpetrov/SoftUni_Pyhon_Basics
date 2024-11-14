from math import ceil

LUNCH_TIME_PERCENT = 1 / 8
CHILL_TIME_PERCENT = 1 / 4

movie_name = input()
movie_duration = int(input())
break_time = int(input())

lunch_time = break_time * LUNCH_TIME_PERCENT
chill_time = break_time * CHILL_TIME_PERCENT

time_needed = lunch_time + chill_time + movie_duration

if time_needed <= break_time:
    print(f"You have enough time to watch {movie_name} and left with {ceil(break_time - time_needed)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(time_needed - break_time)} more minutes.")
