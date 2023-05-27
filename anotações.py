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



#iniciativa

INI = []

if VEM[1] > VEM[0] and VEM[1] < VEM[2]:
  INI.append(3)
  INI.append(2)
  INI.append(1)
elif VEM[0] > VEM[2] and VEM[0] < VEM[1]:
  INI.append(3)
  INI.append(1)
  INI.append(2)
elif VEM[2] > VEM[0] and VEM[2] < VEM[1]:
  INI.append(1)
  INI.append(3)
  INI.append(2)
elif VEM[1] > VEM[2] and VEM[1] < VEM[0]:
  INI.append(1)
  INI.append(2)
  INI.append(3)
elif VEM[0] > VEM[2] and VEM[0] < VEM[1]:
  INI.append(2)
  INI.append(1)
  INI.append(3)
else:
  INI.append(2)
  INI.append(3)
  INI.append(1)
  
for i in range(3):
  if VE >= VEM[i]:
    INI.insert(i, 0)
    break  
if VE < VEM[2]:
  INI.insert(3, 0)
print(INI)
