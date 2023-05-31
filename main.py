from time import sleep
import anotações
from random import randint

# FUNÇÃO DO MENU DE OPÇÕES DE BATALHA

def menuFight():
  while(1):
    print("\033c", end='')
    print("-------------")
    print("1 - ATACAR")
    print("2 - USAR ITEM")
    print("3 - CORRER")
    print("-------------")
    choice = int(input("__"))
    if (choice != 1 or choice != 2 or choice != 3): return choice
    else: print("ERRO: Valor de entrada ínvalido!\nDigite novamente...")
# FUNÇÃO atack NÃO TERMINADA

def atack():
  pass
# FUNÇÃO useItem NÃO TERMINADA

def useItem():
  pass
# FUNÇÃO run NÃO TERMINADA

def run():
  pass

# FUNÇÃO PARA A BATALHA OBS.: Ainda não terminado

def fight(lutadores, ini):
  size = len(ini)
  round = 0
  while(1):
    print("\033c", end='')
    if(ini[round] != 0):
      m = ini[round]
      lutadores[m].emitir_som()
      sleep(1)
      print(round)
      number = randint(1, lutadores[m].skill)
      if number == 1: lutadores[0].hp -= lutadores[m].atq1()
      elif number == 2: lutadores[0].hp -= lutadores[m].atq2()
      elif number == 3: lutadores[0].hp -= lutadores[m].atq3()
      else: lutadores[0].hp -= lutadores[m].atq4()
      sleep(1)
    else:
      choice = menuFight()
      if choice == 1:
        print("Alvo(s):")
        alvo = 0
        while(alvo < 1 or alvo >= size):
          for i in range(1, size): print(f"{i} - {lutadores[i].nome}")
          alvo = int(input("__"))
        lutadores[alvo].hp -= lutadores[0].ataque()
        sleep(2)
    round += 1
    if(round == size): round = 0

if input("Deseja jogar?\n") == "sim":
  print('\033c', end='')
  arma = input("Você pode escolher uma arma entre adaga, machado ou cajado.\n")
  jogador = anotações.Personagem(1, 0, 0, 0, 0)

  while arma != "adaga" and arma != "machado" and arma != "cajado":
    print('\033c', end='')
    print("Por favor, digite os comandos corretamente e sem letra maiscúla\n")
    sleep(2)
    arma = input("Você pode escolher uma arma entre adaga, machado ou cajado.\n")
  jogador.arma = arma
  print('\033c', end='')
  jogador.nome = input("Como devemos te chamar?\n")
  print("NOME REGISTRADO COM SUCESSO!")
  sleep(0.8)
  print('\033c', end='')
  
  print("Você acorda em uma floresta com uma dor de cabeça terrível, mas você não tem tempo para se questionar, pois dois lobos surgem na sua frente. O que você fará?") 

  inimigo1 = anotações.Wolf('Lobo', 10, 2, -1, 2)
  inimigo2 = anotações.Wolf('Lobo', 10, 2, -1, 2)

  ini = anotações.iniciativa([jogador.ve, inimigo1.ve, inimigo2.ve])
  print("INICIATIVA:", ini) # sijeito a mudanças
  sleep(1)
  fight([jogador, inimigo1, inimigo2], ini)
  