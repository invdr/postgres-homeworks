"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2
from psycopg2 import Error

csv_files = ["north_data/customers_data.csv",
             "north_data/employees_data.csv",
             "north_data/orders_data.csv"]
connect_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "saada"
}


def get_tables():
    """Получаем список таблиц из БД."""
    with psycopg2.connect(**connect_params) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT relname FROM pg_class WHERE relkind='r'
                           AND relname !~ '^(pg_|sql_)';""")

            tables = [table[0] for table in cur.fetchall()][::-1]  # список таблиц в БД

            return tables


def get_csv_data(file_name):
    """Возвращает список данных из csv файла."""
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = [tuple(line) for line in reader]
        return data


def insert_data(connect, table, data):
    """Запись данных в таблицу."""

    values_count = ", ".join(["%s"] * len(data[0]))
    try:
        with connect.cursor() as cur:
            cur.executemany(f"INSERT INTO {table} VALUES ({values_count})", data)
            connect.commit()
            print(f"Данные успешно внесены в таблицу {table.upper()}")
    except Error as e:
        print(f"Произошла {e}")


# записать данных из csv файлов в соответствующие таблицы в pgAdmin
for csv_file, current_table in zip(csv_files, get_tables()):
    current_data = get_csv_data(csv_file)
    conn = psycopg2.connect(**connect_params)
    insert_data(conn, current_table, current_data)
