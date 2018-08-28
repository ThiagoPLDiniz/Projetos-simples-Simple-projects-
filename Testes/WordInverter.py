repeat=0;
undefined=3;
while(repeat == 0):
	word = input("Please, insert a word to be inverted:\n");
	inverted = word[::-1];
	print(inverted);
	answer=undefined;
	while(answer == undefined):
		answer = input("Do you want to end the program?(Answer with 'Y' to yes and 'N' to no)\n");
		answer = answer.lower();
		if(answer == 'y'):
			repeat = 1;
			break
		else:
			if(answer == 'n'):
				continue;
			else:
				print("Invalid character!");
				answer = undefined;
				continue;
