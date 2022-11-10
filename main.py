# Criação de funções

preco = 1999.90

# Calcular 5% de imposto e guardar na váriavel imposto
imposto = preco * 0.05
print(imposto)

# Criar função calcular_imposto() que calcula um imposto de 5% e retorna o valor...
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05 # Caso troque o 0.05 por 0.07 será calculado 7%
  return imposto

# Aqui é o uso... aqui é imposto a calcular... e exibir na tela...
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

# Se eu quiser fazer de vários valores ao mesmo tempo
valores = [100, 24.5, 50.6, 10]
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}") # Calculado o valor em 5%.
