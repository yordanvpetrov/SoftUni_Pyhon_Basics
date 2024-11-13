exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_time = exam_hours * 60 + exam_minutes
arrival_time = arrival_hours * 60 + arrival_minutes

time_diff = abs(exam_time - arrival_time)

hours = 0
minutes = 0

if time_diff >= 60:
    hours += time_diff // 60
    minutes += time_diff % 60

    if exam_time < arrival_time:
        print("Late")
        print(f"{hours}:{minutes:02d} hours after the start")
    elif exam_time == arrival_time:
        print("On time")
    elif exam_time > arrival_time:
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")
else:
    if exam_time < arrival_time:
        print("Late")
        print(f"{time_diff} minutes after the start")
    elif exam_time == arrival_time:
        print("On time")
    elif exam_time > arrival_time:
        if time_diff <= 30:
            print("On time")
            print(f"{time_diff} minutes before the start")
        else:
            print("Early")
            print(f"{time_diff} minutes before the start")
