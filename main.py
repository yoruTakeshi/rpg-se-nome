import time
import anotações

if input("deseja jogar?\n") == "sim" or "Sim":
	print ('\033c', end='')
  aInit = input("escolha uma arma entre adaga, machado ou cajado\n")
  while aInit != "adaga" and aInit != "machado" and aInit!= "cajado":
    print ('\033c', end='')
    print("por favor certifique se de escrever certo e sem letra maiscúla\n")
    time.sleep(2)
    aInit = input("escolha uma arma entre adaga, machado ou cajado\n")
  print ('\033c', end='')
  print("Você acorda em uma floresta com uma dor de cabeça terrível, mas você não tem tempo para se questionar, pois dois lobos surgem")
  inimigo1 = "lobo totorial"
  inimigo2 = "lobo totorial"
  inimigo3 = "nada"
  while anotações.HP1 >0 and anotações.HP2 >0 and anotações.HP3 >0:
    
exit()