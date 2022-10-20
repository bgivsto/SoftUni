from math import ceil

name_of_TV_show = input()
episode_duration = int(input())
break_duration = int(input())


lunch_time = break_duration / 8
relax_time = break_duration / 4

remaining_time = break_duration - (lunch_time + relax_time)

if remaining_time >= episode_duration:
    print(f'You have enough time to watch {name_of_TV_show} and left with {ceil(remaining_time-episode_duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_TV_show}, you need {ceil(episode_duration-remaining_time)} more minutes.")


