bad_grade_threshold = int(input())

bad_counter = 0
counter = 0
grades = 0
last_problem = ""

while bad_counter < bad_grade_threshold:
    problem_name = input()

    if problem_name == "Enough":
        print(f"Average score: {grades / counter:.2f}")
        print(f"Number of problems: {counter}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        bad_counter += 1

    last_problem = problem_name
    grades += grade
    counter += 1
else:
    print(f"You need a break, {bad_counter} poor grades.")
