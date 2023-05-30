import time
import anotações

def menuFight():
  print("1 - ")

def fight(lutadores, ini):
  for i in range(len(ini)):
    if(ini[i] == 0):
      p = i
      break
  round = 0
  while(1):
    if(ini[round] != p):
      continue
    else:
      
    round += 1

if input("Deseja jogar?\n") == "sim":
  print('\033c', end='')
  arma = input("Você pode escolher uma arma entre adaga, machado ou cajado.\n")
  jogador = anotações.Personagem(1, 0, 0, 0, 0)

  while arma != "adaga" and arma != "machado" and arma != "cajado":
    print('\033c', end='')
    print("Por favor, digite os comandos corretamente e sem letra maiscúla\n")
    time.sleep(2)
    arma = input("Você pode escolher uma arma entre adaga, machado ou cajado.\n")
  jogador.arma = arma
  print('\033c', end='')
  jogador.nome = input("Como devemos te chamar?\n")
  print("NOME REGISTRADO COM SUCESSO!")
  time.sleep(0.8)
  print('\033c', end='')
  
  print("Você acorda em uma floresta com uma dor de cabeça terrível, mas você não tem tempo para se questionar, pois dois lobos surgem na sua frente. O que você fará?") 

  inimigo1 = anotações.Monstro('Lobo', 10, 2, -1)
  inimigo2 = anotações.Monstro('Lobo', 10, 2, -1)

  ini = anotações.iniciativa([jogador.ve, inimigo1.ve, inimigo2.ve])
  print("INICIATIVA:", ini) # sijeito a mudanças
  