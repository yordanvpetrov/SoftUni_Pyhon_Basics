from math import floor

AD_DURATION_PERCENT = 0.20
SPECIAL_EPISODE_EXTRA = 10

movie_name = input()
season_qty = int(input())
series_qty = int(input())
episode_duration_without_ads = float(input())

episode_with_ads = (episode_duration_without_ads +
                    (episode_duration_without_ads * AD_DURATION_PERCENT))

special_episode_duration = season_qty * SPECIAL_EPISODE_EXTRA

total_time = (season_qty * series_qty) * episode_with_ads + special_episode_duration

print(f"Total time needed to watch the {movie_name} series is {floor(total_time)} minutes.")
