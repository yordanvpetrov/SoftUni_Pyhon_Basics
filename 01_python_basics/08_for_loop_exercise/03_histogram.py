numbers_qty = int(input())

group_one = 0
group_two = 0
group_three = 0
group_four = 0
group_five = 0

for _ in range(1, numbers_qty +1):
    numbers = int(input())

    if numbers < 200:
        group_one += 1
    elif 200 <= numbers <= 399:
        group_two += 1
    elif 400 <= numbers <= 599:
        group_three += 1
    elif 600 <= numbers <= 799:
        group_four += 1
    elif numbers >= 800:
        group_five += 1

print(f"{group_one / numbers_qty * 100:.2f}%")
print(f"{group_two / numbers_qty * 100:.2f}%")
print(f"{group_three / numbers_qty * 100:.2f}%")
print(f"{group_four / numbers_qty * 100:.2f}%")
print(f"{group_five / numbers_qty * 100:.2f}%")
