town = input()
sales_volume = float(input())

commission = 0

if 0 <= sales_volume <= 500:
    if town == "Sofia":
        commission = 5
    elif town == "Varna":
        commission = 4.5
    elif town == "Plovdiv":
        commission = 5.5
elif 500 < sales_volume <= 1000:
    if town == "Sofia":
        commission = 7
    elif town == "Varna":
        commission = 7.5
    elif town == "Plovdiv":
        commission = 8
elif 1000 < sales_volume <= 10000:
    if town == "Sofia":
        commission = 8
    elif town == "Varna":
        commission = 10
    elif town == "Plovdiv":
        commission = 12
elif sales_volume > 10000:
    if town == "Sofia":
        commission = 12
    elif town == "Varna":
        commission = 13
    elif town == "Plovdiv":
        commission = 14.5

if commission > 0:
    print(f"{sales_volume * commission / 100: .2f}")
else:
    print("error")
