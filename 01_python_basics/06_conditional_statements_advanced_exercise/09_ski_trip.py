ONE_PERSON_ROOM = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

days = int(input())
room_type = input()
feedback = input()

discount = 0
nights = days - 1
price = 0
final_price = 0

if room_type == "room for one person":
    price = ONE_PERSON_ROOM
elif room_type == "apartment":
    price = APARTMENT
    if days < 10:
        discount = 0.3
    elif 10 <= days <= 15:
        discount = 0.35
    else:
        discount = 0.5
elif room_type == "president apartment":
    price = PRESIDENT_APARTMENT
    if days < 10:
        discount = 0.1
    elif 10 <= days <= 15:
        discount = 0.15
    else:
        discount = 0.2

sum_price = nights * price
final_price = sum_price - (sum_price * discount)

if feedback == "positive":
    final_price = final_price + (final_price * 0.25)
elif feedback == "negative":
    final_price = final_price - (final_price * 0.1)

print(f"{final_price:.2f}")
