import sqlite3

opcoes = input("Digite a opção desejada: \n1) Realizar seu cadrastro \n2) Já sou cadastrado \n")

conexao = sqlite3.connect("registro.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS cadastros (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               email TEXT,
               senha TEXT,
               data_nascimento TEXT);
               """)

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")
data_nascimento = input("Digite sua data de nascimento: ")

if opcoes == "1":
    cursor.execute(
        """INSERT INTO cadastros (email, senha, data_nascimento)
           VALUES (?, ?, ?)""",
        (email, senha, data_nascimento)
    )
    conexao.commit()

conexao.close()

