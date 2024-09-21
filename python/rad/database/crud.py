# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:47:20 2020

@author: smonteiro
"""
# -----------------------------------------------------------------------------
# Essa classe possui métodos CRUD
# -----------------------------------------------------------------------------
import psycopg2


class AppBD:
    def __init__(self):
        print('Método Construtor')

    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="docker",
                                               password="docker",
                                               host="localhost",
                                               port="5432",
                                               database="estacio")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
# -----------------------------------------------------------------------------
# Selecionar todos os Produtos
# -----------------------------------------------------------------------------

    def selecionarDados(self):
        try:
            self.openConnection()
            cursor = self.connection.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = """select * from products order by code asc"""

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        return registros
# -----------------------------------------------------------------------------
# Inserir Produto
# -----------------------------------------------------------------------------

    def inserirDados(self, name, price):
        try:
            self.openConnection()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO products
          (name, price) VALUES (%s,%s)"""
            record_to_insert = (name, price)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com successo na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

# -----------------------------------------------------------------------------
# Atualizar Produto
# -----------------------------------------------------------------------------
    def atualizarDados(self, code, name, price):
        try:
            self.openConnection()
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização ")
            sql_select_query = """select * from products
            where code = %s"""
            cursor.execute(sql_select_query, (code,))
            record = cursor.fetchone()
            if record is None:
                print(f"Nenhum registro encontrado com o código {code}")
                return
            print("recurso para atualizar", record)
            # Atualizar registro
            sql_update_query = """Update products set name = %s,
            price = %s where "code" = %s"""
            cursor.execute(sql_update_query, (name, price, code))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from products
            where "code" = %s"""
            cursor.execute(sql_select_query, (code,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

# -----------------------------------------------------------------------------
# Excluir Produto
# -----------------------------------------------------------------------------
    def excluirDados(self, code):
        try:
            self.openConnection()
            cursor = self.connection.cursor()
            # Atualizar registro
            sql_delete_query = """Delete from products
            where "code" = %s"""
            cursor.execute(sql_delete_query, (code))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

# -----------------------------------------------------------------------------
