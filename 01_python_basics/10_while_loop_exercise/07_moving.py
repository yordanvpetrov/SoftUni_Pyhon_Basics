width = int(input())
length = int(input())
height = int(input())

sum_space = width * length * height
boxes = 0

while boxes < sum_space:
    command = input()

    if command == "Done":
        print(f"{sum_space - boxes} Cubic meters left.")
        break

    boxes += int(command)
else:
    print(f"No more free space! You need {boxes - sum_space} Cubic meters more.")
