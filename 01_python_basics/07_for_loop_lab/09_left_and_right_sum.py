iteration = int(input())

left_sum = 0
right_sum = 0

for i in range(0, 2):
    for _ in range(0, iteration):
        number = int(input())

        if i == 0:
            left_sum += number
        else:
            right_sum += number

if left_sum != right_sum:
    print(f"No, diff = {abs(left_sum - right_sum)}" )
else:
    print(f"Yes, sum = {left_sum}")
