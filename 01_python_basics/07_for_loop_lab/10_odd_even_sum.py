iteration = int(input())

odd = 0
even = 0

for i in range(iteration):
    num = int(input())

    if i % 2 == 0:
        even += num
    else:
        odd += num

if odd != even:
    print(f"No\nDiff = {abs(even-odd)}")
else:
    print(f"Yes\nSum = {odd}")