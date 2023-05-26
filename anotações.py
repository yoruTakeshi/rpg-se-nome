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

# inimigos básicos:

## Lobo(Totorial)

if main.inimigo1 == "lobo totorial":
  HP1 = 10
  DA1 = 2
  VE1 = -1
if main.inimigo2 == "lobo totorial":
  HP2 = 10
  DA2 = 2
  VE2 = -1
if main.inimigo3 == "lobo totorial":
  HP3 = 10
  DA3 = 2
  VE3 = -1

#iniciativa

INI = []

# VE1 = 1 VE2 = 2 VE3 = 3

if VE2 > VE1 and VE2 < VE3:
  INI.append(3)
  INI.append(2)
  INI.append(1)
elif VE1 > VE3 and VE1 < VE2:
  INI.append(3)
  INI.append(1)
  INI.append(2)
elif VE3 > VE1 and VE3 < VE2:
  INI.append(1)
  INI.append(3)
  INI.append(2)
elif VE2 > VE3 and VE2 < VE1:
  INI.append(1)
  INI.append(2)
  INI.append(3)
elif VE1 > VE3 and VE1 < VE2:
  INI.append(2)
  INI.append(1)
  INI.append(3)
else:
  INI.append(2)
  INI.append(3)
  INI.append(1)
for I in range(3):
  if VE > INI[I]:
    INI.insert(I, 0)
    break
  elif VE <INI[I]