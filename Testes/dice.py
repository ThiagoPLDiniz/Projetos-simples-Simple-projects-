import random
dice = [1, 2, 3, 4, 5, 6];
resposta = 1;
while(resposta == 1):
	input("Para girar o dado, tecle ENTER:\n");
	num_sorteado = random.choice(dice);
	print (num_sorteado);
	continua = input("Deseja executar o programa novamente?(Digite 'S' para sim e 'N' para não)\n");
	continua = continua.lower();
	if(continua == 's'):
		resposta = 1;
	else:
		resposta = 0;