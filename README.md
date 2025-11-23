# Aprendendo SQL usando a linguagem python.
1 - O principal objeto desse código, é mostrar como funciona trabalhar com banco de dados usando python.

## Como funciona o código: 

# 1 - Importando a biblioteca SQLite 

<img width="158" height="23" alt="Captura de tela 2025-11-23 135001" src="https://github.com/user-attachments/assets/db714d8a-e506-46f3-8847-cf263eb6bc29" />

Acessando essa biblioteca, ela permite criar e manipular bancos de dados SQLite diretamente em Python.

# 2 - Pergunta ao usuário:
<img width="773" height="43" alt="Captura de tela 2025-11-23 135804" src="https://github.com/user-attachments/assets/31f4d688-82a8-4a54-bdb0-42f4a4fa73f1" />

Mostra um menu ao usuário onde ele escolhe a opção desejada e guarda a escolha na variável "opcoes".

# 3 - Conexão com o banco de dados:
<img width="475" height="48" alt="Captura de tela 2025-11-23 135824" src="https://github.com/user-attachments/assets/25f67795-f0e5-4f31-a6b9-1ac90963ff3d" />

connect("registro.db"): cria (caso não existir) ou abre o arquivo de banco de dados registro.db.

cursor(): permite enviar comandos SQL (como criar tabela, inserir dados etc.).

# 4 - Criando a tabela (Caso ela não existir):
<img width="547" height="138" alt="Captura de tela 2025-11-23 135903" src="https://github.com/user-attachments/assets/58e6519b-29fd-49e8-9e23-cc4484915acb" />

Cria a tabela cadastros com as colunas:

id = inteiro, chave primária, aumenta automaticamente
email, senha, data_nascimento = textos
O (IF NOT EXISTS) evita erro, caso a tabela já exista.

# 5 - Coletando os dados do usuário:
<img width="575" height="81" alt="Captura de tela 2025-11-23 135936" src="https://github.com/user-attachments/assets/15dab93d-59eb-4828-be21-52149617715b" />

Esse código vai pedir as informações do usuário, independente da opção que o úsuario escolher.

# 6 - Inserindo dados no banco:
<img width="540" height="159" alt="Captura de tela 2025-11-23 140948" src="https://github.com/user-attachments/assets/27b1c84d-7b02-4fec-946d-f48dacaaee0b" />

Se o usuário escolher a opção: 1 (Realizar cadastro):

Executa o comando INSERT na tabela

Usa placeholders (?) para evitar ataques SQL injection
commit() salva permanentemente os dados no banco.

Se o usuário escolhe 2, o código não faz nada (por enquanto).

# 7) Fechando a conexão:
<img width="186" height="50" alt="Captura de tela 2025-11-23 140959" src="https://github.com/user-attachments/assets/9c1825de-a24f-4866-b4d6-2fcc043822d8" />

Fecha o banco de dados.

# O código está em desenvolvimento em breve terá a continuação, mas já conseguimos ter uma base de como funciona.
