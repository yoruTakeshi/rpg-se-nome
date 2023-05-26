from main import inimigo1
from main import inimigo2
from main import inimigo3
SA = 0
SM = 0

#personagem

##status

###level
LV = 1

###constituição
CO = 0

###velocidade
VE = 0

###força
FO = 0

###intelecto
IN = 0

###vida
HP = LV * CO + 20

###mana points
MP = LV * IN + 10

##danos

###dano arma pesada (SA = statos da arma)
DAP = FO + SA

###dano da arma leve (SA = statos da arma)
DAL = VE + SA

###dano de magia (SA = statos da arma; SM statos da magia)
DAM = IN + SA + SM

#inimigos

##lobo
if inimigo1 == "lobo":
  HP1 = 10
  DA1 = 2
if inimigo2 == "lobo":
  HP2 = 10
  DA2 = 2
if inimigo3 == "lobo":
  HP3 = 10
  DA3 = 2
