from sys import maxsize

max_number = -maxsize

while True:
    number = input()

    if number == "Stop":
        print(max_number)
        break

    check_number = int(number)

    if check_number > max_number:
        max_number = check_number
