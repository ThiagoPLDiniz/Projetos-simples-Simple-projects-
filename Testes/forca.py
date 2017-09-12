import random
#definindo variáveis imutáveis
palavras = ["cachorro", "paralelepipedo", "conjuntos", "diarreia", "dia", "numeros", "momento", "dinheiro"]
resposta = 1

while(resposta == 1):
	#definindo variáveis mutáveis de rodada para rodada
	
	nome_jogador = input("\nOlá! Bem-vindo ao 'A Forca'. Digite seu nome:\n")
	escolhida = random.choice(palavras)
	separada = list(escolhida)
	tamanho = len(escolhida)
	cifrada = escolhida.replace(escolhida, '_' * tamanho)
	armazenada = list(cifrada)
	erros = []
	chances = 20
	i = 0
	print("\nCerto, " + str(nome_jogador) + ". A palavra escolhida contém " + str(tamanho) + " letras!Você terá 20 tentativas!\n")
	print(str(cifrada))
	letras = 1
	while(letras != 0 and chances > 0):
		j=0
		k=0
		tentativa = input("\nTente uma letra:\n")
		while(k < tamanho):
			procurando = separada[k]
			if(procurando == tentativa):
				armazenada.pop(k)
				armazenada.insert(k, tentativa)
			k = k+1

		chute = escolhida.find(tentativa)
		if(chute < 0):
			print("A palavra não contém a letra " + str(tentativa) + ".\n")
			erros.insert(i, tentativa)
			print(erros)
			chances = chances - 1
			print("Você ainda tem " + str(chances) + " chances!\n")
			i = i+1
			
			
		teste = ''.join(armazenada)
		print("\n" + str(teste))
		testando = teste.find('_')
		if(chances < 1):
			print("Acabaram suas chances! Boa sorte na próxima!\n")
			break

		if(testando == -1):
			print("Parabéns, você acertou a palavra!\n")
			print("Você marcou " + str(chances * 10) + " pontos!\n")
			letra = 0
			break
		else:
			continue
		
			
			


	#encerramento do programa
	perguntando = input("Deseja jogar novamente?(RESPONDA COM '0' para NÃO OU '1' para SIM)\n")
	resposta = int(perguntando)
	if(resposta == 0):
		print("Obrigado por jogar 'A Forca'.\n")
