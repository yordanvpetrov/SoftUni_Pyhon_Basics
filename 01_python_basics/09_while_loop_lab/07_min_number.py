from sys import maxsize

min_number = maxsize

while True:
    number = input()

    if number == "Stop":
        print(min_number)
        break

    check_number = int(number)

    if check_number < min_number:
        min_number = check_number
