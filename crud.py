# CRUD MySQL em python

# SCRIPT CRUD PARA EDIÇÕES
# comando = ''
# cursor.execute(comando)
# conexao.commit() # Edita o banco de dados.

# SCRIPT CRUD PARA LEITURAS
# comando = ''
# cursor.execute(comando)
# resultado = cursor.fetchall() # Lê o banco de dados.


# Importo o conector de MySQL
import mysql.connector

# Crio um objeto para realizar a conexão e lhe atribuo as informações padrões necessárias.
conexao = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='9Eminhasous@3',
    database = 'bd_crud',
    )
   
# Imprimo o estado da conexão.                                     
print(conexao)

# Crio um cursor para executar os comandos que serão utilizados.
cursor = conexao.cursor()
   
# CREATE
nome_produto = 'Chocolate',
valor = 10.0
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}",{valor})'
cursor.execute(comando) # Manda o cursor executar o comando.
conexao.commit() # Edita o banco de dados.

# # READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall # Lê o banco de dados.
# print(resultado)

# # UPDATE
# nome_produto = "Chocolate"
# valor = 6.0
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # Edita o banco de dados.   
   
# # DELETE
# nome_produto = "Barrinha de cereal"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()
                
# São criados os cursores para fechar/encerrar os objetos cursor e conexao.
cursor.close()
conexao.close()