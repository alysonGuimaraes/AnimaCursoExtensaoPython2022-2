#1o. passo: importar a biblioteca sqlite3
import sqlite3

#1o. passo: vamos estabelecer uma conexão com o banco
conexao = sqlite3.connect("dc_universe.db")

#3o. passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o. passo: comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5o. passo: Executar o comando SQL no SQLite (no cursor)
cursor.execute(sql)

#6o. passo: exibir a consulta com todos os nomes de herois e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")
