import time
import anotações
import pickle

#SAVE SYSTEM
class SaveSystem:
    def __init__(self):
        self.save_file = 'save_data.pkl'

    def save_game(self, player_data):
        with open(self.save_file, 'wb') as file:
            pickle.dump(player_data, file)
        print("Jogo salvo com sucesso!")

    def load_game(self):
        try:
            with open(self.save_file, 'rb') as file:
                player_data = pickle.load(file)
            print("Jogo carregado com sucesso!")
            return player_data
        except FileNotFoundError:
            print("Nenhum arquivo de save encontrado.")
            return None

# Exemplo de uso
save_system = SaveSystem()

# Salvar o jogo
player_data = {
    'LV': LV,
    'PV': HP,
    'GOLD': bufunfa
}
save_system.save_game(player_data)

# Carregar o jogo
loaded_data = save_system.load_game()
if loaded_data is not None:
    print(loaded_data)

if input("deseja jogar?\n") == "sim" or "Sim":
	print ('\033c', end='')
  aInit = input("escolha uma arma entre adaga, machado ou cajado\n")
  while aInit != "adaga" and aInit != "machado" and aInit!= "cajado":
    print ('\033c', end='')
    print("por favor certifique se de escrever certo e sem letra maiscúla\n")
    time.sleep(2)
    aInit = input("escolha uma arma entre adaga, machado ou cajado\n")
  print ('\033c', end='')
  print("você acorda em uma floresta com uma enorme dor de cabeça, até que derrepente dois lobos surgem")
  inimigo1 = "lobo totorial"
  inimigo2 = "lobo totorial"
  inimigo3 = "nada"
  while anotações.HP1 >0 and anotações.HP2 >0 and anotações.HP3 >0:
    
exit()
#sai da minha conta seu safado fdp