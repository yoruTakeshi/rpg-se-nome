import time
import anotações

def menuFight():
  while(1):
    print("\033c", end='')
    print("-------------")
    print("1 - ATACAR")
    print("2 - USAR ITEM")
    print("3 - CORRER")
    print("-------------")
    choice = int(input("__"))
    if not(choice != 1 or choice != 2 or choice != 3): return choice
    else: print("ERRO: Valor de entrada ínvalido!\nDigite novamente...")
      
def fight(lutadores, ini):
  size = len(ini)
  for i in range(size):
    if(ini[i] == 0):
      p = i
      break
  round = 0
  while(1):
    if(ini[round] != p):
      continue
    else:
      choice = menuFight()
      if choice == 1:
        print("Alvo:")
        alvo = 0
        while(alvo < 1 and alvo >= size):
          for i in range(1, size): print(f"{i} - {lutadores[i].nome}")
          alvo = int(input("__"))
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
  