from abc import ABC, abstractmethod
from random import randint

# CLASSE PARA CONSTRUIR O PERSONAGEM #

class Personagem:
  def __init__(self, lv, co, ve, fo, mind):
    self.nome = ''
    self.arma = ''
    self.lv = lv
    self.co = co
    self.ve = ve
    self.fo = fo
    self.mind = mind
    self.hp = lv + int(co * 2) + 20
    self.mp = lv + int(mind * 1.5) + 10

  def ataque(self):
    print(f"{self.nome} causou {1} de DANO!")
    return 1
# CLASSE ABSTRATA PARA OS MONSTROS #

class Monstro(ABC):
  def __init__(self, nome, hp, da, ve, skill):
    self.nome = nome
    self.hp = hp
    self.da = da
    self.ve = ve
    self.skill = skill
  @abstractmethod
  def emitir_som(self):
    pass
# CLASSE DO LOBO

class Wolf(Monstro):
  def emitir_som(self):
    self.number = randint(1, 3)
    if self.number == 1: print(f"{self.nome}: AUUUU!!!!")
    elif self.number == 2: print(f"{self.nome}: Au! Au!")
    else: print(f"{self.nome}: AUUUUUAUUUUUUU!!!")
  def atq1(self):
    self.dano = self.da + self.ve
    print(f"{self.nome} usou 'Arranhar', causando {self.dano} de dano!")
    return self.dano
  def atq2(self):
    self.dano = self.da
    print(f"{self.nome} usou 'Mordida', causando {self.dano} de dano!")
    return self.dano
# FUNÇÃO PARA DETERMINAR A INICIATIVA

def iniciativa(ve):
  ini = []
  vea = []
  for i in ve: vea.append(i)
  sort(ve)
  for i in ve:
    for c in range(len(vea)):
      if vea[c] == i:
          vea[c] = -99
          ini.append(c)
          break
  return ini

# FUNÇÃO PARA ORDENAR

def sort(n):
  aux = 0
  size = len(n)
  for i in range(size):
    for c in range(size-1, i, -1):
      if(n[i] < n[c]):
        aux = n[i]
        n[i] = n[c]
        n[c] = aux
  return n

# lobo = Monstro('Lobo', 10, 2, -1)
# goblin = Monstro('Goblin', 15, 6, 4)
