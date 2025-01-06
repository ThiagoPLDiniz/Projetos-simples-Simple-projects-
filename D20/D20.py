import random
import variables

answer = 1;
while(answer == 1):
	error_loop = 0;
	input("To roll the dice, click ENTER:\n");
	sort_number = random.choice(variables.dice);
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
			print ("\n\nInvalid character!\n\n");
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
