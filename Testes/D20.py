import random
dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
answer = 1;
while(answer == 1):
	error_loop = 0;
	input("To roll the dice, click ENTER:\n");
	sort_number = random.choice(dice);
	print (sort_number);
	re_roll = input("Do you want to roll the dice again?(Click 'Y' to YES and 'N' to NO)\n");
	re_roll = re_roll.lower();
	if(re_roll == 'y'):
		answer = 1;
		error_loop = 0;
	elif re_roll == 'n':
		answer = 0;
		error_loop = 0;
	else:
		error_loop = 1;
	
	while(error_loop == 1 and answer == 1):
		if(re_roll == 'y'):
			answer = 1;
			error_loop = 0;
		elif re_roll == 'n':
			answer = 0;
			error_loop = 0;
		else:
			print ("Invalid character!");
			re_roll = input("Do you want to roll the dice again?(Click 'Y' to YES and 'N' to NO)\n");
			re_roll = re_roll.lower();
			if re_roll == 'y':
				error_loop = 0;
				answer = 1;
			elif re_roll == 'n':
				error_loop = 0;
				answer = 0;
			else:
				error_loop = 1;

print("\nThank you for use this program!\n");
