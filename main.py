import time
import anotações

#-------------------------------------------

if input("Deseja jogar?\n") == "sim" or "Sim":
	print('\033c', end='')
	aInit = input(
	 "Você pode escolher uma arma. Escolha entre uma adaga, machado ou um cajado.\n"
	)

	while aInit != "adaga" and aInit != "machado" and aInit != "cajado":
		print('\033c', end='')
		print("Por favor, digite os comandos corretamente e sem letra maiscúla\n")
		time.sleep(2)
		aInit = input(
		 "Você pode escolher uma arma. Escolha entre uma adaga, machado ou um cajado.\n"
		)
	print('\033c', end='')

	print(
	 "Você acorda em uma floresta com uma dor de cabeça terrível, mas você não tem tempo para se questionar, pois dois lobos surgem na sua frente. O que você fará?"
	)

	inimigo1 = "Lobo Tutorial"
	inimigo2 = "Lobo Tutorial"
	inimigo3 = "Nada"
	while inimigo1 != "Nada" and inimigo2 != "Nada" and inimigo3 != "Nada":
		print(
		 "--------"
    )
exit()
