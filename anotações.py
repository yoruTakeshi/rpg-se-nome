# CLASSE PARA CONSTRUIR O PERSONAGEM #

class Personagem:
  def __init__(self, lv, co, ve, fo, int):
    self.lv = lv
    self.co = co
    self.ve = ve
    self.fo = fo
    self.int = int
    self.hp = lv * co + 20
    self.mp = lv * int + 10

# CLASSE PARA CONSTRUIR OS MONSTROS #

class Monstro:
  def __init__(self, nome, hp, da, ve):
    self.nome = nome
    self.hp = hp
    self.da = da
    self.ve = ve
  
# FUNÇÃO PARA DETERMINAR A INICIATIVA OBS.: QUASE TERMINADA

def iniciativa(ve, nm):
  ini = []
  aux = 0
  size = len(ve)
  for i in range(size):
    for c in range(size-1, 0+i, -1):
      if(ve[i] > ve[c]):
        aux = ve[i]
        ve[i] = ve[c]
        ve[c] = aux
    ini.append(ve[i])
  return ini

## PERSONAGEM ##

# CRIAÇÃO DO PERSONAGEM
boneco = Personagem(1, 0, 0, 0, 0)

## MONSTROS ##

# CRIAÇÃO DOS MONSTROS
#nomeVariavel = Monstro('nome', hp, da, ve)
lobo = Monstro('Lobo', 10, 2, -1) 


looping = "infinito"
while looping == "infinito":
  SA = 0
  SM = 0
	## danos

	### dano arma pesada (SA = statos da arma)
	DAP = FO + SA

	### dano da arma leve (SA = statos da arma)
	DAL = VE + SA

	### dano de magia (SA = status da arma; SM statos da magia)
	DAM = IN + SA + SM

	#--------------- inimigos: ----------------

	VEM = []

	## Lobo (Tutorial)

	#iniciativa

  
  if HP1 <= 0:
    inimigo1 = "Nada"
  if HP2 <= 0:
    inimigo2 = "Nada"
  if HP3 <= 0:
    inimigo3 = "Nada"
