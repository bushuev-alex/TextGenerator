recommended_to_sleep = int(input())
should_not_sleep_more = int(input())
now_ann_sleeps = int(input())

if now_ann_sleeps < recommended_to_sleep:
    print('Deficiency')
elif now_ann_sleeps > should_not_sleep_more:
    print('Excess')
else:
    print('Normal')
