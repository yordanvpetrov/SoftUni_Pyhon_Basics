SPRING_RENT = 3000
SUMMER_RENT = 4200
AUTUMN_RENT = 4200
WINTER_RENT = 2600
MAX_SIX_PPL_DISCOUNT = 10 / 100
SEVEN_ELEVEN_DISCOUNT = 15 / 100
OVER_TWELVE_DISCOUNT = 25 / 100

EXTRA_DISCOUNT = 5 / 100

budget = int(input())
season = input()
people = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = SPRING_RENT
    if people <= 6:
        boat_rent = boat_rent - (boat_rent * MAX_SIX_PPL_DISCOUNT)
    elif 7 <= people <= 11:
        boat_rent = boat_rent - (boat_rent * SEVEN_ELEVEN_DISCOUNT)
    else:
        boat_rent = boat_rent - (boat_rent * OVER_TWELVE_DISCOUNT)
elif season == "Summer":
    boat_rent = SUMMER_RENT
    if people <= 6:
        boat_rent = boat_rent - (boat_rent * MAX_SIX_PPL_DISCOUNT)
    elif 7 <= people <= 11:
        boat_rent = boat_rent - (boat_rent * SEVEN_ELEVEN_DISCOUNT)
    else:
        boat_rent = boat_rent - (boat_rent * OVER_TWELVE_DISCOUNT)
elif season == "Autumn":
    boat_rent = AUTUMN_RENT
    if people <= 6:
        boat_rent = boat_rent - (boat_rent * MAX_SIX_PPL_DISCOUNT)
    elif 7 <= people <= 11:
        boat_rent = boat_rent - (boat_rent * SEVEN_ELEVEN_DISCOUNT)
    else:
        boat_rent = boat_rent - (boat_rent * OVER_TWELVE_DISCOUNT)
elif season == "Winter":
    boat_rent = WINTER_RENT
    if people <= 6:
        boat_rent = boat_rent - (boat_rent * MAX_SIX_PPL_DISCOUNT)
    elif 7 <= people <= 11:
        boat_rent = boat_rent - (boat_rent * SEVEN_ELEVEN_DISCOUNT)
    else:
        boat_rent = boat_rent - (boat_rent * OVER_TWELVE_DISCOUNT)

if season == "Spring" or season == "Summer" or season == "Winter":
    if people % 2 == 0:
        boat_rent = boat_rent - (boat_rent * EXTRA_DISCOUNT)

if boat_rent <= budget:
    sum_total = budget - boat_rent
    print(f"Yes! You have {sum_total:.2f} leva left.")
elif boat_rent > budget:
    sum_total = boat_rent - budget
    print(f"Not enough money! You need {sum_total:.2f} leva.")
