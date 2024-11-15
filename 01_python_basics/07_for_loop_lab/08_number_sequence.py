from sys import maxsize

repeat = int(input())

min_num = maxsize
max_num = -maxsize

for _ in range(0, repeat):
    number = int(input())

    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
