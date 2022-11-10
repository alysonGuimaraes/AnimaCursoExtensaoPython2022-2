# Exemplo de laço.

# Se eu quisesse exibir números de 1 a 10.
contador = 1
while contador <= 10:
  print(contador)
  contador += 1

# Exemplo de lista
frutas = ["morango", "laranja", "manga"]
print(frutas) # Mostra tudo
print(frutas[1]) #Mostra em uma posição especifica

# Exibir quantidade de itens na lista
print(len(frutas)) # length = tamanho

# Incluir uma nova fruta
frutas.append("uva")
print(frutas)

# Usar while para printar as frutas
print("Exemplo frutas com while")
i = 0
while i < len(frutas):
  print(frutas[i])
  i += 1

# Usar for para printar frutas
print("Exemplo das frutas com for")
for fruta in frutas:
  print(fruta)