# Primeira conexão Postgree com Python + GoogleCloud

import pandas as pd 
import pandas.io.sql as sqlio
import psycopg2

host = '' # Adicione o host obtido pelo ipecho e dermarque também no GCloud
user = 'postgres' # Padrão do postgree
password = '' # Password definido no momento da criação do database
database = 'northwind' # Nome do Database

conn = psycopg2.connect(database=database,
                        host=host,
                        user=user,
                        password=password
                        )

cursor = conn.cursor()
query = '''
SELECT *
FROM products;
''' # Definição da consulta SQL a ser executada

produtos = sqlio.read_sql_query(query, conn)
print(produtos) # Exibição do DataFrame Pandas contando os resultados da consulta
cursor.close() # Fechamento do cursor após a conclusão da consulta
conn.close() # Fechamento da conexão após consulta