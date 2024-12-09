GOAL = 10000

steps = 0

while steps < GOAL:
    command = input()

    if command == "Going home":
        steps += int(input())

        if steps < GOAL:
            print(f"{GOAL - steps} more steps to reach goal.")
            break
        else:
            print(f"Goal reached! Good job!\n{steps - GOAL} steps over the goal!")
            break

    steps += int(command)
else:
    print(f"Goal reached! Good job!\n{steps - GOAL} steps over the goal!")
