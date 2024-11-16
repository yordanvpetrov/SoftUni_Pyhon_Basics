student_name = input()

counter = 0
failed = 0
average_grade = 0

while counter != 12:
    grade = float(input())

    if grade >= 4:
        counter += 1
        average_grade += grade

    if grade < 4:
        failed += 1

    if failed > 1:
        print(f"{student_name} has been excluded at {counter + 1} grade")
        break
else:
    print(f"{student_name} graduated. Average grade: {average_grade / 12:.2f}")
