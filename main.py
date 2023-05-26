import time
import anotações

#-------------------------------CODESYS:----------------------------------

linebreak = print('\033c', end='')
wait2sec = time.sleep(2)
wait3sec = time.sleep(3)
wait4sec = time.sleep(4)
wait5sec = time.sleep(5)


#--------------------------------------------------------------------------

if input("deseja jogar?\n") == "sim" or "Sim":
	linebreak
	aInit = input("Você pode escolher uma arma. Escolha entre uma adaga, machado ou um cajado.\n")
	
	while aInit != "adaga" and aInit != "machado" and aInit!= "cajado":
  		linebreak
  		print("Por favor, digite os comandos corretamente e sem letra maiscúla\n")
  		wait2sec
	aInit = input("Você pode escolher uma arma. Escolha entre uma adaga, machado ou um cajado.\n")
	linebreak
	
	print("Você acorda em uma floresta com uma dor de cabeça terrível, mas você não tem tempo para se questionar, pois dois lobos surgem na sua frente. O que você fará?")

	inimigo1 = "Lobo (Fraco)"
	inimigo2 = "Lobo (Fraco)"
	inimigo3 = "-----"
	while anotações.HP1 >0 and anotações.HP2 >0 and anotações.HP3 >0:
    
exit()