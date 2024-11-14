RESISTANCE = 12.5

record = float(input())
distance = float(input())
seconds_per_meter = float(input())

time = distance * seconds_per_meter
extra_time = (distance // 15) * RESISTANCE

sum_time = time + extra_time

if sum_time < record:
    print(f"Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {sum_time - record:.2f} seconds slower.")
