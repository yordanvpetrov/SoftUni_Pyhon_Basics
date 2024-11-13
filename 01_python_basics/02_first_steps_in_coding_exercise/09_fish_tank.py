length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

area = (length * width * height) / 1000

water_needed = area - area * percent
print(water_needed)
