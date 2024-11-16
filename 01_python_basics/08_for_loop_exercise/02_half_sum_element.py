from sys import maxsize

interation = int(input())

biggest_number = -maxsize
total_numbers = 0

for num in range(1, interation +1):
    numbers = int(input())
    total_numbers += numbers

    if numbers > biggest_number:
        biggest_number = numbers

total_numbers -= biggest_number

if total_numbers == biggest_number:
    print(f"Yes\nSum = {biggest_number}")
else:
    print(f"No\nDiff = {abs(biggest_number - total_numbers)}")
