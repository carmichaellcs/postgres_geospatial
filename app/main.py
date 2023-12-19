import csv
import psycopg2
import logging

from config import settings

def logger_setup():
  logging.basicConfig(
    filename='migrate_ms_access_to_postgis.log',
    filemode='a',
    level=logging.INFO,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
  )

def db_config():
  return {
    'host': settings.DB_HOST,
    'port': settings.DB_PORT,
    'database': settings.DB_NAME,
    'user': settings.DB_USER,
    'password': settings.DB_PASSWORD
  }

def conn():
  return psycopg2.connect(**db_config())

def query(data):
  return f"""
    INSERT INTO public.contas (nome, idade, nota) 
    VALUES ('{data[0]}', {data[1]}, {data[2]})
  """

def execute(data):
  connection = conn()
  for value in data[1:]:
    logging.info(f'Registro processado: {value}')
    with connection.cursor() as cursor:
      cursor.execute(query(value))
    
    connection.commit()
    logging.info(f'Registro inserido com sucesso na base')

def reader(file_path, data):
  with open(file_path, 'r') as arquivo:
    for linha in csv.reader(arquivo):
      data.append(linha)

def main():
  logger_setup()
  file_path = 'tmp/arquivo.csv'
  data = []
  reader(file_path, data)
  execute(data)

if __name__ == "__main__":
  main()