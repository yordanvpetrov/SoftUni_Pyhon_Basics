
best_player = ""
best_score = 0
end = False


while end is False:
    name = input()

    if name == "END":
        end = True
        continue

    score = int(input())

    if score > best_score:
        best_player = name
        best_score = score

    if score >= 10:
        end = True
        continue
else:
    print(f"{best_player} is the best player!")
    if best_score >= 3:
        print(f"He has scored {best_score} goals and made a hat-trick !!!")
    else:
        print(f"He has scored {best_score} goals.")
