import psycopg2
conn = psycopg2.connect(database="estacio", user="docker",
                        password="docker", host="localhost", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()

# ? Create Table
# cur.execute(
#     '''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
# print("Tabela criada com sucesso!")

# ? Insert Data
# cur.execute("""INSERT INTO agenda ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""")

# ? Select Data
# cur.execute("""select * from agenda where "id"=1""")
# registro = cur.fetchone()
# print(registro)
# conn.commit()
# print("Seleção realizada com sucesso!")

# ? Update data
# print("Consulta antes da atualização")
# cur.execute("""select * from agenda where "id"=1""")
# registro = cur.fetchone()
# print(registro)
# # Atualização de um único registro
# cur.execute(
#     """Update agenda set "telefone"='02188888777' where "id"=1""")
# conn.commit()
# print("Registro Atualizado com sucesso! ")
# print(" Consulta depois da atualização")
# cur.execute("""select * from agenda where "id"=1""")
# registro = cur.fetchone()
# print(registro)
# print("Seleção realizada com sucesso!")

# ? Delete Data
cur.execute("""Delete from agenda where "id"=1""")
conn.commit()
cont=cur.rowcount
print(cont, "Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!");

conn.commit()
conn.close()
