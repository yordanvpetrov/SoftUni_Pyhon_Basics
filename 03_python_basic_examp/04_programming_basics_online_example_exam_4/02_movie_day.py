PREPARING_TIME_PERCENT = 0.15

recording_time = int(input())
scenes_qty = int(input())
scene_duration = int(input())

preparation = recording_time * PREPARING_TIME_PERCENT
needed_time = scenes_qty * scene_duration + preparation

if recording_time >= needed_time:
    print(f"You managed to finish the movie on time! You have {round(recording_time - needed_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(needed_time - recording_time)} minutes.")
