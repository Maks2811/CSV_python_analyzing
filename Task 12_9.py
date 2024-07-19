""" Импортируем необходимые модули"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

""" Функция, принимающая на вход csv файл с данными и возвращающая список продаж со словарями"""
def read_sales_data(file_path):
    sales_data = []
    with open(file_path, 'r') as file:      # читаем сsv файл с данными
        reader = csv.reader(file)

        for row in reader:                  # цикл создающий списос продаж из словарей
            sales_data.append({'product_name':row[0], 'quantity':int(row[1]),
                                'price':int(row[2]), 'date': datetime.strptime(row[3], '%Y-%m-%d').date()})
            #print(row)

    return sales_data


""" Функция, принимающая на вход список продаж и возвращающая словарь {Продукт: сумма продаж для продукта}"""
def total_sales_per_product(sales_data):
    sales_dict = {}
    for product in sales_data:
        product_name = product['product_name']
        total_sales = product['quantity'] * product['price']
        if product_name in sales_dict:
            sales_dict[product_name] = sales_dict[product_name] + total_sales
        else:
            sales_dict[product_name] = total_sales

    return sales_dict


""" Функция, принимающая на вход список продаж и возвращающая словарь {Дата: сумма продаж за эту дату}"""
def sales_over_time(sales_data):
    date_sales = {}
    for d in sales_data:
        date = d['date']
        total_sales = d['quantity'] * d['price']
        if date in date_sales:
            date_sales[date] = date_sales[date] + total_sales
        else:
            date_sales[date] = total_sales

    return date_sales


""" Функция, принимающая на вход словарь и возвращающая ключ словаря, имеющий максимальное значение"""
def find_max_value(my_dict):
    max_value = max(my_dict.values())
    for key, value in my_dict.items():
        if value == max_value:
            return key
            break
        else:
            continue

sales_data = read_sales_data('D:\Github\Task_12_9\sales.csv')

print(sales_data)


print(f'\n{total_sales_per_product(sales_data)}')

print(f'\n{sales_over_time(sales_data)}')

total_sales_dict = total_sales_per_product(sales_data)
sales_over_time_dict = sales_over_time(sales_data)



print(f'\n Наибольшую выручку принес следующий продукт: {find_max_value(total_sales_dict)}, '
      f'максимальная выручка составила: {max(total_sales_dict.values())}')


print(f'\n Наибольшая сумма продаж была: {find_max_value(sales_over_time_dict)}, '
      f'суммарная выручка за день составила: {max(sales_over_time_dict.values())}')



