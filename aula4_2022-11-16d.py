import sqlite3
import aula4_2022_11_16c as bd

conexao, cursor = bd.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão: ")
tipo = input("digite 1 para herói ou 2 para vilão")

# consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if tipo == "1":
  tipo_letra = "Herói(na)"
else:
  tipo_letra = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo_letra}')"
cursor.execute(sql)
conexao.commit()
conexao.close()
