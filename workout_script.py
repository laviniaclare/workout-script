import random

EXERCISES = [
	'1 minute plank',
	'1 minute wall sit',
	'10 Burpees',
	'10 Push-ups',
	'10 Jumping Jacks',
	'10 High Knees',
	'10 Tip toes, toes straight',
	'10 Tip toes, toes in',
	'10 Tip toes, toes out',
	'15 Back Lunges',
	'15 Burpees',
	'15 Front Lunges',
	'15 Push-ups',
	'15 Push-ups',
	'2 minute plank',
	'2 minute wall sit',
	'20 Back Lunges',
	'20 Burpees',
	'20 Crunches',
	'20 Front Lunges',
	'20 Jump Squats',
	'20 Push-ups',
	'20 Tricep Dips',
	'25 Burpees',
	'30 Crunches',
	'30 Jump Squats',
	'30 Jumping Jacks',
	'30 High Knees',
	'30 Squats',
	'30 Tricep Dips',
	'40 Jumping Jacks',
	'40 High Knees',
	'50 Calf Raises',
	'50 Jumping Jacks',
	'10 Short Bridges',
	'20 Short Bridges',
	'30 Short Bridges',
	'20 Side Lunges',
	'10 Side Lunges',
	'20 Butterfly Sit-ups',
	'30 Butterfly Sit-ups',
	'20 Kneel-ups',
	'30 Kneel-ups',
	'20 Side leg raises (10 per side)',
	'20 Bent knee leg raises (10 per side)',
	'20 Butterfly side leg raises (10 per side)',
	'30 Side leg raises (15 per side)',
	'30 Bent knee leg raises (15 per side)',
	'30 Butterfly side leg raises (15 per side)',
	'20 Donkey Kicks (10 per side)',
	'30 Donkey Kicks (15 per side)',
	'20 Firehose Leg Raises (10 per side)',
	'30 Firehose Leg Raises (15 per side)',
]

RESISTENCE_BAND = [
	'10 Side leg raises with resistence band',
	'10 Bent knee leg raises with resistence band',
	'10 Butterfly side leg raises with resistence band',
	'20 Side leg raises with resistence band',
	'20 Bent knee leg raises with resistence band',
	'20 Butterfly side leg raises with resistence band',
	'10 Short Bridges with resistence band',
	'20 Short Bridges with resistence band',
	'30 Short Bridges with resistence band',
	'20 Tricep Pulls',
	'30 Tricep Pulls',
	'20 Reverse Grip Single-Arm Curl and Row',
	'30 Reverse Grip Single-Arm Curl and Row',
	'20 Side Lateral Arm Raise',
	'30 Side Lateral Arm Raise',
	'20 Triceps Presses/extensions',
	'30 Triceps Presses/extensions',
	'20 Lat Pull-Downs',
	'30 Lat Pull-Down',
	'20 Horizontal Arm Extensions',
	'30 Horizontal Arm Extensions',
	'20 Rear Arm Extensions',
	'30 Rear Arm Extensions',
	'20 Standing Hip Abductions',
	'30 Standing Hip Abductions',
	'20 Squatting Side Steps',
	'30 Squatting Side Steps',
	'30 V Rows',
	'20 V Rows',
]

num_exercises = input('How many different moves do you want to do?\n')
include_band = str(input('Do you want to include mini band exercises? If yes, answer True\n'))
if include_band:
	exercises = EXERCISES + RESISTENCE_BAND
else:
	exercises = EXERCISES
print('Your assignment is:\n')
for i in range(num_exercises):
	move_index = random.randint(0, len(exercises)-1)
	move = exercises[move_index]
	print(' - '+move)

print('\nGood luck!')
