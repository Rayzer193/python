import os

def get_name():   
    return input('Введите Имя и Фамилию: ')

def get_number():
    return input('Введите номер телефона: ')    

def get_comment():
    return input('Введите Комментарий: ')

def actions():
    return int(input('Выберите действие:\n 1. Добавить запись.\n 2. Посмотреть книжку.\n 3. Выход. \n Действие:'))