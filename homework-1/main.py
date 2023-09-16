"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2
from psycopg2 import Error

data_dict = {
    "customers": "north_data/customers_data.csv",
    "employees": "north_data/employees_data.csv",
    "orders": "north_data/orders_data.csv"
}
connect_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "saada"
}


def get_csv_data(file_name: str) -> list:
    """Возвращает список данных из csv файла."""
    with open(file_name, newline='') as csvfile:
        # создаем объект csv для работы
        reader = csv.reader(csvfile)
        # пропускаем первую строку
        next(reader)
        return list(reader)


def insert_data(connect, table: str, data: list) -> None:
    """Запись данных в таблицу."""
    # получаем кол-во %s по кол-ву столбцов в таблице
    values_count = ", ".join(["%s"] * len(data[0]))
    try:
        # создаем курсор для работы
        with connect.cursor() as cur:
            # получаем данные data в таблицу table
            cur.executemany(f"INSERT INTO {table} VALUES ({values_count})", data)
            # заносим полученные данные в таблицу в pgAdmin
            connect.commit()
            print(f"Данные успешно внесены в таблицу {table.upper()}")
    except Error as e:
        print(f"Произошла {e}")


# записать данных из csv файлов в соответствующие таблицы в pgAdmin
for current_table, csv_file in data_dict.items():
    # получаем данные для занесения в таблицу
    current_data = get_csv_data(csv_file)
    # устанавливаем соединение с БД
    conn = psycopg2.connect(**connect_params)
    # добавляем полученные данные в текущую таблицу
    insert_data(conn, current_table, current_data)
