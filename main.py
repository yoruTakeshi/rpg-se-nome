import time
import anotações

I = input("deseja jogar?\n")
if I == "sim" or "Sim":
  print ('\033c', end='')
  AM = input("escolha uma arma entre adaga, machado ou cajado\n")
  while AM != "adaga" and AM != "machado" and AM!= "cajado":
    print ('\033c', end='')
    print("por favor certifique se de escrever certo e sem letra maiscúla\n")
    time.sleep(2)
    AM = input("escolha uma arma entre adaga, machado ou cajado\n")
  print ('\033c', end='')
  print("você acorda em uma floresta com uma enorme dor de cabeça, até que derrepente dois lobos surgem")
  inimigo1 = "lobo"
  inimigo2 = "lobo"
  inimigo3 = "nada"

exit()