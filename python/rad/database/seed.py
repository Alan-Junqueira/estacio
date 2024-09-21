from faker import Faker
import psycopg2 as pg

conn = pg.connect(database="estacio", user="docker",
                  password="docker", host="localhost", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
fake = Faker("pt_BR")

n = 10

for i in range(n):
    name = "product" + str(i+1)
    price = fake.pyfloat(left_digits=3, right_digits=2,
                         positive=True, min_value=5, max_value=1000)
    print(price)
    print(name)

    sql_command = """insert into product (name, price) values (%s, %s)"""
    register = (name, price)
    cur.execute(sql_command, register)

conn.commit()
print("Inserção realizada com sucesso!")
conn.close()

