#1o. passo
import sqlite3

#2o. passo
conexao = sqlite3.connect("dc_universe.db")
#3o. passo:
cursor = conexao.cursor()

#4o. passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#5o. passo: executar o comando SQL
cursor.execute(sql)

#6o. passo: confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()