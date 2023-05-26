import main
SA = 0
SM = 0

# personagem

## status:

### level
LV = 1

### constituição
CO = 0

### velocidade
VE = 0

### força
FO = 0

### intelecto
IN = 0

### vida
HP = LV * CO + 20

### mana
MP = LV * IN + 10

## danos

### dano arma pesada (SA = statos da arma)
DAP = FO + SA

### dano da arma leve (SA = statos da arma)
DAL = VE + SA

### dano de magia (SA = status da arma; SM statos da magia)
DAM = IN + SA + SM

# Inimigos básicos:

## Lobo(Totorial)
if main.inimigo1 == "lobo totorial":
  HP1 = 10
  DA1 = 2
  VE1 = -1
if main.inimigo2 == "lobo totorial":
  HP2 = 10
  DA2 = 2
  VE2
if main.inimigo3 == "lobo totorial":
  HP3 = 10
  DA3 = 2
  VE3 = -1

#não sei oque escrever
JI = VE
N1I = VE1
N2I 
N3I