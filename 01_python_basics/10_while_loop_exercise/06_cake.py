cake_width = int(input())
cake_length = int(input())

total_pieces = cake_width * cake_length
eaten_pieces = 0

while eaten_pieces < total_pieces:
    command = input()

    if command == "STOP":
        print(f"{total_pieces - eaten_pieces} pieces are left.")
        break

    eaten_pieces += int(command)
else:
    print(f"No more cake left! You need {abs(eaten_pieces - total_pieces)} pieces more.")
