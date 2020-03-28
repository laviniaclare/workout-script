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
	'10 Bridges',
	'20 Bridges',
	'30 Bridges',
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

num_exercises = input("How many different moves do you want to do?\n")
print('Your assignment is:\n')
for i in range(num_exercises):
	move_index = random.randint(0, len(EXERCISES)-1)
	move = EXERCISES[move_index]
	print(' - '+move)

print("\nGood luck!")
