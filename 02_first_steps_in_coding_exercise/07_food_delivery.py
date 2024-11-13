CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGAN_MENU_PRICE = 8.15
DESERT_PERCENT = 0.20
DELIVERY_PRICE = 2.50

chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

sum_menu = (chicken_menu * CHICKEN_MENU_PRICE) \
            + (fish_menu * FISH_MENU_PRICE) \
            + (vegan_menu * VEGAN_MENU_PRICE)

sum_total = sum_menu + sum_menu * DESERT_PERCENT + DELIVERY_PRICE
print(f"{sum_total:.02f}")
