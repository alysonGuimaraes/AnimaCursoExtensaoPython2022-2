# Comando Input(): quero permitir que o usuário digite algo...
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
print(f"Olá {nome}, você tem {idade} anos.")

# Dobro da idade;
dobro = idade * 2
print(f"O dobro da idade informada é {dobro}")

# Estrutura if (se);
# Se for maior de idade pode beber e tirar a carteira
if idade >= 18:
  print(f"Já que você tem {idade} anos, você já pode beber e já pode tirar a carteira de motorista.")
else:
  print(f"Você tem só {idade}, você não pode beber e nem tirar a carteira de motorista.")

# Perguntar se o gênero (Masculino ou Feminino)
# Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = str.upper(input("Insira o seu gênero (M/F): "))

# Condicional composta
if genero == "M" and idade >= 18:
  print("...e você também precisa/precisou prestar o serviço militar obrigatório")
else:
  print("Você não precisa/precisou prestar serviço militar obrigatório.")
