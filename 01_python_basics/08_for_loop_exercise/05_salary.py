FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50

open_tabs = int(input())
salary = int(input())

fine = 0

for _ in range(open_tabs):
    website_name = input()
    if website_name == "Facebook":
        fine += FACEBOOK
    elif website_name == "Instagram":
        fine += INSTAGRAM
    elif website_name == "Reddit":
        fine += REDDIT
    if salary <= fine:
        print("You have lost your salary.")
        break

if salary > fine:
    result = salary - fine
    print(result)
