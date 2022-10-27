# Pede o nome do aluno e sua nota (0 a 10) e, se ele tirou 10, mostra "Parabéns!!"
nome = input("Insira o seu nome: ")
nota = float(input("Digite sua nota: "))
if nota == 10:
  print(f"{nome}, Parabéns!!")
elif 6 <= nota < 10:
  print(f"{nome}, não foi tão ruim, estude mais para a próxima.")
else:
  print("Um tanto burrinho.")