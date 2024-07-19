""" Импортируем необходимые модули"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt


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
        else:
            continue

"""Функция для вывода на экран графиков-гистограмм"""
# На вход подаем словарь со значениями, подписи обеих осей и заговолок графика
def plot_graph(my_dict, xlab, ylab, plot_title):
    key_list = list(my_dict.keys())
    value_list = list(my_dict.values())

    plt.figure(figsize=(10,5))      # построение графика
    plt.bar(key_list, value_list)

    plt.xlabel(xlab)                # добавление подписей осей и заголовка
    plt.ylabel(ylab)
    plt.title(plot_title)
    plt.xticks(rotation=45)           # наклон подписей на оси X

    plt.show()                        # вывод графика


"""Функция выводв на экран 2-х график одновременно"""
# на вход подаем 2 словаря с данными
def plot_2graph(my_dict_1, my_dict_2):
    key_list1 = list(my_dict_1.keys())
    value_list1 = list(my_dict_1.values())
    key_list2 = list(my_dict_2.keys())
    value_list2 = list(my_dict_2.values())

    # создание фигуры и подграфиков
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # Первый график
    ax1.bar(key_list1, value_list1)
    ax1.set_xlabel('Продукт')
    ax1.set_ylabel('Сумма продаж')
    ax1.set_title('Общая сумма продаж по каждому продукту')

    # Второй график
    ax2.bar(key_list2, value_list2)
    ax2.set_xlabel('Дата')
    ax2.set_ylabel('Сумма продаж')
    ax2.set_title('Общая сумма продаж')
    plt.xticks(rotation=45)

    # Вывод графиков
    plt.tight_layout()
    plt.show()

"""Логическая часть программы"""

sales_data = read_sales_data('D:\Github\Task_12_9\sales.csv')     # выполняем чтение данных из исходника

"""Вывод полученных для аналитики данных (закомментировано)"""
# print(sales_data)
# print(f'\n{total_sales_per_product(sales_data)}')
# print(f'\n{sales_over_time(sales_data)}')

total_sales_dict = total_sales_per_product(sales_data)    # Определяем переменные для дальнейшей аналитики
sales_over_time_dict = sales_over_time(sales_data)

""" Определяем продукт с наибольшей выручкой и дату с наибольшими продажами"""

print(f'\n Наибольшую выручку принес следующий продукт: {find_max_value(total_sales_dict)}, '
      f'максимальная выручка составила: {max(total_sales_dict.values())}')


print(f'\n Наибольшая сумма продаж была: {find_max_value(sales_over_time_dict)}, '
      f'суммарная выручка за день составила: {max(sales_over_time_dict.values())}')


""" Выбираем способ вывода грфиков на экран"""

while True:
    try:
        choice = int(input('\nДля вывода графиков по отдельности нажмите цифру 1\n'
                           'Для вывода 2-х графиков одновременно нажмите цифру 2 \n'))
        if choice in [1, 2]:
            break
        else:
            print('Ошибка ввода, попробуйте еще раз')   # проверяем корректность выбора
            continue
    except:
        print('Ошибка ввода, попробуйте еще раз')     # обрабатываем ошибки


"""Выводим графики в соответствии со сделанным выбором"""

if choice == 1:
    plot_graph(total_sales_dict, 'Продукт', 'Сумма продаж', 'Общая сумма продаж по каждому продукту')
    plot_graph(sales_over_time_dict, 'Дата', 'Сумма продаж', 'Общая сумма продаж')
elif choice == 2:
    plot_2graph(total_sales_dict, sales_over_time_dict)



