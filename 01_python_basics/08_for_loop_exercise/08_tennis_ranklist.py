from math import floor

iteration = int(input())
starting_points = int(input())

W = 2000
F = 1200
SF = 720

points = 0

wins = 0

for _ in range(iteration):
    stage = input()
    if stage == "W":
        points += W
        wins += 1
    elif stage == "F":
        points += F
    elif stage == "SF":
        points += SF

sum_points = points + starting_points
print(f"Final points: {floor(sum_points)}")
print(f"Average points: {floor(points / iteration)}")
print(f"{(wins / iteration) * 100:.2f}%")
