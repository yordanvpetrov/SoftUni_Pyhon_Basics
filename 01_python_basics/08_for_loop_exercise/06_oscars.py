name = input()
academy_points = float(input())
jury = int(input())

points = 0 + academy_points

for i in range(jury):
    jury_name = len(input())
    jury_points = float(input())

    points += (jury_name * jury_points) / 2
    if points >= 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        break

if points < 1250.5:
    print(f"Sorry, {name} you need {1250.5 - points:.1f} more!")
