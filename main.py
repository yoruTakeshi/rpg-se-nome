import time
import anotações
import codesys

if input("deseja jogar?\n") == "sim" or "Sim":
	codesys.linebreak
	aInit = input("escolha uma arma entre adaga, machado ou cajado\n")
	
while aInit != "adaga" and aInit != "machado" and aInit!= "cajado":
    codesys.linebreak
    print("Por favor, digite os comandos corretamente e sem letra maiscúla\n")
    time.sleep(2)
    aInit = input("Você pode escolher uma arma. Escolha entre uma adaga, machado ou um cajado.\n")

  	codesys.linebreak
  print("Você acorda em uma floresta com uma dor de cabeça terrível, mas você não tem tempo para se questionar, pois dois lobos surgem")
  inimigo1 = "lobo totorial"
  inimigo2 = "lobo totorial"
  inimigo3 = "nada"
  while anotações.HP1 >0 and anotações.HP2 >0 and anotações.HP3 >0:
    
exit()