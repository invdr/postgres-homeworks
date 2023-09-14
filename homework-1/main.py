"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

CUSTOMERS = "north_data/customers_data.csv"
EMPLOYEES = "north_data/employees_data.csv"
ORDERS = "north_data/orders_data.csv"


connect_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "saada"
}


# def read_csv_file(file_name):
#     with open(file_name, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         file_header = reader.fieldnames
#

# read_csv_file("north_data/customers_data.csv")

connect = psycopg2.connect(**connect_params)

with connect.cursor() as cur:
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    print(rows)

connect.close()
