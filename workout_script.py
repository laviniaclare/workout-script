import random

EXERCISES = [
	'1 Minute Elbow Plank',
	'1 Minute Short Bridge Hold',
	'1 Minute Square Bridge Hold',
	'1 Minute Squat Hold',
	'1 minute plank',
	'1 minute wall sit',
	'2 Minute Squat Hold',
	'10 Burpees',
	'10 Calf Raises (toes pointed in)',
	'10 Calf Raises (toes pointed out)',
	'10 Calf Raises (toes straight)',
	'10 Push-ups',
	'10 Short Bridges',
	'10 Side Lunges',
	'10 Superman',
	'100 Jumping Jacks',
	'15 Burpees',
	'15 Regular Push-ups',
	'15 Hands pointed in Push-ups',
	'15 Reverse Plank',
	'15 Second Side Plank Per Side',
	'16 Front Lunges',
	'16 Rear Lunges',
	'2 minute wall sit',
	'20 Back Lunges',
	'20 Bent Knee Side Leg Raises',
	'20 Burpees',
	'20 Butterfly Sit-ups',
	'20 Butterfly side leg raises',
	'20 Crunches',
	'20 Donkey Kicks',
	'20 Firehose Leg Raises',
	'20 Front Lunges',
	'20 Good mornings',
	'20 High Knees',
	'20 Jump Squats',
	'20 Jumping Jacks',
	'20 Knee to Elbow Bicycles',
	'20 Kneel-ups',
	'20 Mountain Climbers',
	'20 Push-ups',
	'20 Reverse Plank',
	'20 Russion Twists',
	'20 Short Bridges',
	'20 Short Bridges Knees to chest',
	'20 Short Bridges kick up',
	'20 Side Lunges',
	'20 Side leg raises',
	'20 Standing Hip Abductions',
	'20 Superman',
	'20 Tricep Dips',
	'25 Burpees',
	'30 Bent knee side leg raises',
	'30 Butterfly Sit-ups',
	'30 Butterfly side leg raises',
	'30 Crunches',
	'30 Donkey Kicks',
	'30 Firehose Leg Raises',
	'30 Flutter Kicks',
	'30 Front Elevated Mountain Climbers',
	'30 Good mornings',
	'30 High Knees',
	'30 Jump Squats',
	'30 Jumping Jacks',
	'30 Knee to Elbow Bicycles',
	'30 Kneel-ups',
	'30 Leg Raises (laying on back)',
	'30 Mountain Climbers',
	'30 Russian Twists',
	'30 Second Reverse Plank Hold',
	'30 Second Short Bridge Hold',
	'30 Second Side Plank Per Side',
	'30 Second Square Bridge Hold',
	'30 Second Squat Hold',
	'30 Second Superman Hold',
	'30 Short Bridges',
	'30 Side leg raises',
	'30 Squats',
	'30 Standing Hip Abductions',
	'30 Tricep Dips',
	'40 Butterfly Sit-ups',
	'40 Donkey Kicks',
	'40 Good mornings',
	'40 High Knees',
	'40 Jumping Jacks',
	'40 Knee to Elbow Bicycles',
	'40 Mountain Climbers',
	'50 High Knees',
	'50 Jumping Jacks',
	'60 High Knees',
	'80 High Knees',
	'80 Jumping Jacks',
	'30 Second Swan Hold',
	'1 Minute Swan Hold',
	'10 Dive Through Push-ups',
	'10 Regular Push-ups',
	'20 Regular Push-ups',
	'10 Diamond Push-ups',
	'15 Dive Through Push-ups',
	'10 Pre-Handstand Toe Lift',
	'15 Pre-Handstand Toe Lift',
	'10 Pre-Handstand Toe Lift, on elbows',
	'15 Pre-Handstand Toe Lift, on elbows',
 ]

BLOCKS = [
	'30 Second Straddle Hold',
	'30 Second Butterfly Hold',
	'1 Minute Straddle Hold',
	'1 Minute Butterfly Hold',
	'10 Butterfly Pelvic Tilt',
	'10 Straddle Pelvic Tilt',
	'10 Parallette Dips',
	'10 Parallette Push-ups',
	'10 Parallette Dive Through Push-ups',
	'10 Parallette Skullcrusher Push-ups',
	'30 Second Parallette Tucked L-sit, toes touching',
	'15 Parallette Tucked L-sit Single Leg Toe Taps',
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
	'20 Standing Hip Abductions (with resistence band)',
	'30 Standing Hip Abductions (with resistence band)',
	'20 Squatting Side Steps',
	'30 Squatting Side Steps',
	'30 V Rows',
	'40 V Rows',
	'50 V Rows',
	'30 Kneeling Curl',
	'40 Kneeling Curl',
	'20 Donkey Kicks w/ Mini Band',
	'30 Donkey Kicks w/ Mini Band',
	'40 Donkey Kicks w/ Mini Band',
	'20 Resistence Band Kick Back',
	'30 Resistence Band Kick Back',
	'10 Resistence Band Deadlift',
	'20 Resistence Band Deadlift',
	'30 Resistence Band Deadlift',
	'40 Resistence Band Deadlift',
	'20 Resistence Band Jump Squats',
	'30 Resistence Band Jump Squats',
]

num_exercises = input('How many different moves do you want to do?\n')
include_band = input('Include mini band exercises? True or False\n')
include_blocks = input('Include block exercises?\n')
exercises = EXERCISES
if include_band:
	exercises += RESISTENCE_BAND
if include_blocks:
	exercises += BLOCKS
print('Your assignment is:\n')
for _ in range(num_exercises):
	move_index = random.randint(0, len(exercises)-1)
	move = exercises[move_index]
	print(' - '+move)

print('\nGood luck!')
