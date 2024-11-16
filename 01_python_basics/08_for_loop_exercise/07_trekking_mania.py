iteration = int(input())

musala = 0
monblan = 0
kalimajaro = 0
k2 = 0
everest = 0

sum_people = 0

for _ in range(iteration):
    people = int(input())
    sum_people += people
    if people <= 5:
        musala += people
    elif 5 < people <= 12:
        monblan += people
    elif 12 < people <= 25:
        kalimajaro += people
    elif 25 < people <= 40:
        k2 += people
    else:
        everest += people

musala_percent = (musala / sum_people) * 100
print(f"{musala_percent:.2f}%")
monblan_percent = (monblan / sum_people) * 100
print(f"{monblan_percent:.2f}%")
kalimajaro_percent = (kalimajaro / sum_people) * 100
print(f"{kalimajaro_percent:.2f}%")
k2_percent = (k2 / sum_people) * 100
print(f"{k2_percent:.2f}%")
everest_percent = (everest / sum_people) * 100
print(f"{everest_percent:.2f}%")
