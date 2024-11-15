month = input()
days = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 0
apartment_discount = 0
studio_total = 0
apartment_total = 0

if  month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if days > 14:
        studio_discount = 0.30
    elif days > 7:
        studio_discount = 0.05
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if days > 14:
        studio_discount = 0.20
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if days > 14:
    apartment_discount = 0.10
    apartment_total = apartment_price * days
    apartment_total = apartment_total - apartment_total * apartment_discount
    studio_total = studio_price * days
else:
    apartment_total = apartment_price * days
    studio_total = studio_price * days

if studio_discount != 0:
    print(f"Apartment: {apartment_total:.2f} lv.")
    print(f"Studio: {studio_total - (studio_total * studio_discount):.2f} lv.")
else:
    print(f"Apartment: {apartment_total:.2f} lv.")
    print(f"Studio: {studio_price * days:.2f} lv.")
