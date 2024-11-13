page_number = int(input())
pages_per_hour = int(input())
days = int(input())

time_for_book = page_number // pages_per_hour
day_needed = time_for_book // days

print(day_needed)
