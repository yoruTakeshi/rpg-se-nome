import time
import anotações

#--------------- inimigos: ----------------

VEM = []

## Lobo (Tutorial)

if inimigo1 == "Lobo Tutorial":
  HP1 = 10
  DA1 = 2
  VEM.append(-1)
if inimigo2 == "Lobo Tutorial":
  HP2 = 10
  DA2 = 2
  VEM.append(-1)
if inimigo3 == "Lobo Tutorial":
  HP3 = 10
  DA3 = 2
  VEM.append(-1)

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
	while HP1 > 0 and HP2 > 0 and HP3 > 0:
		print(
		 "deixei isso aq só pro programa rodar, pq se deixar vazio o programa nn roda"
    )
exit()
